# # Heart Disease — Zone-Structured Ensemble (Open-Source)
# 
# This notebook replicates the **WSRF v8 Dual-Tree Architecture** using only standard open-source libraries:
# - `scikit-learn` — RandomForest, DecisionTree, IsotonicRegression
# - `numpy` / `pandas` — data handling
# 
# ### The Approach
# 
# Instead of one global model, we split the feature space into **hyperdimensional zones** based on natural boundaries, then train **separate ensembles per zone**. Each zone gets the complexity it needs:
# 
# | Component | Purpose | Library |
# |-----------|---------|--------|
# | Zone discovery | Boundary splits on key features | Manual (from WSRF auto_discover) |
# | Prediction trees | Adaptive RF per zone | `RandomForestClassifier` |
# | OOB calibration | Isotonic regression on OOB probs | `IsotonicRegression` |
# | Export trees | Fixed shallow trees for rules | `DecisionTreeClassifier` |
# 
# Based on the Williams Structured Random Forest, invented by William Lars Rocha, 2011.

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.isotonic import IsotonicRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import warnings
warnings.filterwarnings('ignore')

RANDOM_STATE = 42


# ## Load Data

train = pd.read_csv('train.csv')
test  = pd.read_csv('test.csv')

feature_cols = [c for c in train.columns if c not in ['id', 'Heart Disease']]

X_train = train[feature_cols].values
y_train = (train['Heart Disease'] == 'Presence').astype(int).values
X_test  = test[feature_cols].values

print(f'Train: {X_train.shape[0]:,} x {X_train.shape[1]}')
print(f'Test:  {X_test.shape[0]:,} x {X_test.shape[1]}')
print(f'Features: {feature_cols}')
print(f'Target balance: {np.bincount(y_train)}')


# ## Zone Assignment
# 
# WSRF's auto_discover found 4 zones using 2 boundary features:
# - **Number of vessels fluro** (index 11): split at 1.5
# - **Thallium** (index 12): split at 3.2
# 
# This creates a 2x2 hyperdimensional grid — 4 distinct patient populations.

IDX_VESSELS  = feature_cols.index('Number of vessels fluro')  # 11
IDX_THALLIUM = feature_cols.index('Thallium')                 # 12

VESSELS_THRESHOLD  = 1.5
THALLIUM_THRESHOLD = 3.2


def assign_zones(X):
    """Assign samples to zones based on discovered boundaries."""
    vessels_region  = (X[:, IDX_VESSELS]  > VESSELS_THRESHOLD).astype(int)
    thallium_region = (X[:, IDX_THALLIUM] > THALLIUM_THRESHOLD).astype(int)
    # Zone = vessels_bit * 2 + thallium_bit  -> 0, 1, 2, 3
    return vessels_region * 2 + thallium_region


zones_train = assign_zones(X_train)
zones_test  = assign_zones(X_test)

print('Zone distribution (train):')
for z in sorted(np.unique(zones_train)):
    mask = zones_train == z
    n = mask.sum()
    pos_rate = y_train[mask].mean()
    print(f'  Zone {z}: {n:>7,} samples ({n/len(y_train)*100:5.1f}%), '
          f'positive rate = {pos_rate:.3f}')


# ## Adaptive Complexity per Zone
# 
# Pure zones (high/low positive rate) get fewer, shallower trees. Impure zones get the heavy treatment. This mirrors WSRF's friendly/unfriendly deck logic.

def compute_zone_complexity(y_zone, n_zones, base_trees=100, base_depth=15):
    """
    Adaptive complexity: scale trees and depth by zone purity.
    Mirrors WSRF v7.2 friendly/unfriendly deck logic.
    """
    purity = max(y_zone.mean(), 1 - y_zone.mean())
    zone_size = len(y_zone)
    avg_size = len(y_zone)  # will be overridden per-call
    size_factor = min(1.5, max(0.5, zone_size / max(avg_size, 1)))

    if purity > 0.9:
        # Friendly deck — easy zone
        tree_mult, depth_adj = 0.3, -3
    elif purity > 0.7:
        # Standard zone
        tree_mult, depth_adj = 1.0, 0
    else:
        # Unfriendly deck — hard zone
        tree_mult, depth_adj = 1.5, 3

    n_trees = max(10, int(base_trees * tree_mult * size_factor))
    max_depth = max(3, int(base_depth + depth_adj))
    return n_trees, max_depth, purity


# Preview the adaptive settings
print('Adaptive complexity per zone:')
for z in sorted(np.unique(zones_train)):
    mask = zones_train == z
    n_trees, max_depth, purity = compute_zone_complexity(y_train[mask], 4)
    print(f'  Zone {z}: purity={purity:.3f} -> {n_trees} trees, depth {max_depth}')


# ## Train Zone-Structured Ensemble
# 
# For each zone:
# 1. Adaptive-complexity `RandomForestClassifier` (prediction)
# 2. OOB probabilities collected for calibration
# 3. Fixed `DecisionTreeClassifier` x10 at depth 5 (export/rules)

EXPORT_TREES_PER_ZONE = 10
EXPORT_MAX_DEPTH = 5


def train_zoned_model(X, y, zones, base_trees=100, base_depth=15, seed=42):
    """
    Train the full zone-structured dual-tree model.

    Returns
    -------
    pred_models : dict[int, RandomForestClassifier]
    export_trees : dict[int, list[DecisionTreeClassifier]]
    calibrator : IsotonicRegression
    zone_priors : dict[int, float]
    zone_reputations : dict[int, float]
    """
    unique_zones = sorted(np.unique(zones))
    pred_models = {}
    export_trees = {}
    zone_priors = {}
    zone_reputations = {}

    # Collect OOB predictions for calibration
    oob_proba = np.full(len(y), np.nan)

    for z in unique_zones:
        mask = zones == z
        X_z, y_z = X[mask], y[mask]

        # Zone prior (base rate)
        zone_priors[z] = y_z.mean()

        # Skip pure zones
        if len(np.unique(y_z)) <= 1:
            pred_models[z] = None
            export_trees[z] = []
            zone_reputations[z] = 0.5
            oob_proba[mask] = y_z[0]
            continue

        # --- Prediction trees (adaptive complexity) ---
        n_trees, max_depth, purity = compute_zone_complexity(
            y_z, len(unique_zones), base_trees, base_depth
        )

        rf = RandomForestClassifier(
            n_estimators=n_trees,
            max_depth=max_depth,
            min_samples_split=5,
            min_samples_leaf=2,
            max_features='sqrt',
            oob_score=True,
            random_state=seed,
            n_jobs=-1,
        )
        rf.fit(X_z, y_z)
        pred_models[z] = rf

        # OOB predictions for this zone
        if hasattr(rf, 'oob_decision_function_'):
            oob_proba[mask] = rf.oob_decision_function_[:, 1]
        elif hasattr(rf, 'oob_score_'):
            oob_proba[mask] = rf.predict_proba(X_z)[:, 1]

        # Zone reputation (OOB AUC)
        zone_oob = oob_proba[mask]
        if not np.any(np.isnan(zone_oob)) and len(np.unique(y_z)) > 1:
            zone_reputations[z] = roc_auc_score(y_z, zone_oob)
        else:
            zone_reputations[z] = 0.5

        # --- Export trees (fixed: 10 trees, depth 5) ---
        export_rng = np.random.RandomState(seed + 1_000_000)
        zone_export = []
        for t in range(EXPORT_TREES_PER_ZONE):
            # Bootstrap sample
            idx = export_rng.choice(len(y_z), size=len(y_z), replace=True)
            dt = DecisionTreeClassifier(
                max_depth=EXPORT_MAX_DEPTH,
                min_samples_split=5,
                min_samples_leaf=2,
                max_features='sqrt',
                random_state=export_rng.randint(0, 2**31),
            )
            dt.fit(X_z[idx], y_z[idx])
            zone_export.append(dt)
        export_trees[z] = zone_export

        print(f'  Zone {z}: pred={n_trees} trees (depth {max_depth}), '
              f'export={EXPORT_TREES_PER_ZONE} trees (depth {EXPORT_MAX_DEPTH}), '
              f'OOB AUC={zone_reputations[z]:.4f}')

    # --- OOB Isotonic Calibration ---
    valid = ~np.isnan(oob_proba)
    calibrator = IsotonicRegression(out_of_bounds='clip')
    calibrator.fit(oob_proba[valid], y[valid])
    print(f'\n  Calibrator fitted on {valid.sum():,} OOB samples')

    return pred_models, export_trees, calibrator, zone_priors, zone_reputations


print('Training zone-structured ensemble...')
pred_models, export_trees, calibrator, zone_priors, zone_reputations = \
    train_zoned_model(X_train, y_train, zones_train)


# ## Predict with Calibration + Zone Prior Blending

ZONE_PRIOR_WEIGHT = 0.1


def predict_proba_zoned(X, zones, pred_models, calibrator,
                        zone_priors, zone_reputations,
                        prior_weight=ZONE_PRIOR_WEIGHT):
    """
    Predict probabilities with zone routing, prior blending, and calibration.
    Mirrors WSRF v7.2 predict_proba flow.
    """
    proba = np.zeros(len(X))
    unique_zones = sorted(np.unique(zones))

    for z in unique_zones:
        mask = zones == z
        if not mask.any():
            continue

        model = pred_models.get(z)
        prior = zone_priors.get(z, 0.5)

        if model is None:
            # Pure zone — use the prior directly
            proba[mask] = prior
        else:
            # RF prediction
            raw = model.predict_proba(X[mask])[:, 1]
            # Blend with zone prior (Bayesian)
            blended = (1 - prior_weight) * raw + prior_weight * prior
            proba[mask] = blended

    # Isotonic calibration
    proba = calibrator.predict(proba)
    return np.clip(proba, 1e-7, 1 - 1e-7)


# Quick sanity check on train
train_proba = predict_proba_zoned(
    X_train, zones_train, pred_models, calibrator, zone_priors, zone_reputations
)
train_auc = roc_auc_score(y_train, train_proba)
print(f'Train AUC (in-sample, sanity check): {train_auc:.5f}')


# ## Cross-Validation

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=RANDOM_STATE)
fold_aucs = []

for fold, (tr_idx, va_idx) in enumerate(skf.split(X_train, y_train)):
    X_tr, X_va = X_train[tr_idx], X_train[va_idx]
    y_tr, y_va = y_train[tr_idx], y_train[va_idx]
    z_tr, z_va = assign_zones(X_tr), assign_zones(X_va)

    pm, et, cal, zp, zr = train_zoned_model(
        X_tr, y_tr, z_tr, base_trees=100, base_depth=15, seed=RANDOM_STATE
    )

    va_proba = predict_proba_zoned(X_va, z_va, pm, cal, zp, zr)
    auc = roc_auc_score(y_va, va_proba)
    fold_aucs.append(auc)
    print(f'Fold {fold+1}: AUC = {auc:.5f}\n')

print(f'Mean AUC: {np.mean(fold_aucs):.5f} +/- {np.std(fold_aucs):.5f}')


# ## Extract Doctor Rules (Export Trees)
# 
# The export trees are fixed shallow decision trees (depth 5). We extract human-readable IF-THEN rules from each.

def extract_rules_from_tree(tree, feature_names, tree_idx=0):
    """Extract IF-THEN rules from a fitted DecisionTreeClassifier."""
    tree_ = tree.tree_
    rules = []

    def recurse(node, conditions):
        if tree_.children_left[node] == tree_.children_right[node]:
            # Leaf node
            values = tree_.value[node][0]
            total = values.sum()
            prediction = int(np.argmax(values))
            confidence = values[prediction] / total if total > 0 else 0
            rules.append({
                'conditions': list(conditions),
                'prediction': prediction,
                'confidence': confidence,
                'n_samples': int(total),
                'tree_index': tree_idx,
            })
            return

        feat = tree_.feature[node]
        thresh = tree_.threshold[node]
        name = feature_names[feat] if feat < len(feature_names) else f'f{feat}'

        # Left: feature <= threshold
        recurse(tree_.children_left[node],
                conditions + [f'{name} <= {thresh:.2f}'])
        # Right: feature > threshold
        recurse(tree_.children_right[node],
                conditions + [f'{name} > {thresh:.2f}'])

    recurse(0, [])
    return rules


def extract_all_rules(export_trees, feature_names):
    """Extract rules from all export trees across all zones."""
    all_rules = {}
    total = 0
    max_depth = 0

    for zone, trees in sorted(export_trees.items()):
        zone_rules = []
        for t_idx, dt in enumerate(trees):
            zone_rules.extend(extract_rules_from_tree(dt, feature_names, t_idx))
        all_rules[zone] = zone_rules
        zone_max = max((len(r['conditions']) for r in zone_rules), default=0)
        max_depth = max(max_depth, zone_max)
        total += len(zone_rules)
        print(f'  Zone {zone}: {len(zone_rules)} rules, max depth {zone_max}')

    print(f'\n  Total: {total} rules, max depth {max_depth}')
    return all_rules, total, max_depth


print('Extracting rules from export trees...')
all_rules, total_rules, max_rule_depth = extract_all_rules(export_trees, feature_cols)


# Show top rules per zone (by sample coverage)
for zone, rules in sorted(all_rules.items()):
    print(f'\n--- Zone {zone} (top 5 rules) ---')
    top = sorted(rules, key=lambda r: r['n_samples'], reverse=True)[:5]
    for i, r in enumerate(top):
        conds = ' AND '.join(r['conditions'])
        label = 'Presence' if r['prediction'] == 1 else 'Absence'
        print(f'  #{i+1}: IF {conds}')
        print(f'        THEN {label} (conf={r["confidence"]:.2f}, n={r["n_samples"]})')


# ## Save Doctor Rules

def format_doctor_rules(all_rules, zone_priors, zone_reputations, feature_cols):
    """Format rules as a human-readable doctor report."""
    lines = []
    lines.append('=' * 60)
    lines.append('HEART DISEASE PREDICTION — DOCTOR RULES')
    lines.append('Zone-Structured Ensemble (Open-Source Replication)')
    lines.append('=' * 60)
    lines.append('')
    lines.append('Zone boundaries:')
    lines.append(f'  Number of vessels fluro: split at 1.5')
    lines.append(f'  Thallium: split at 3.2')
    lines.append('')

    total = 0
    for zone, rules in sorted(all_rules.items()):
        prior = zone_priors.get(zone, 0.5)
        rep = zone_reputations.get(zone, 0.5)
        lines.append(f'--- Zone {zone} ({len(rules)} rules) ---')
        lines.append(f'  Base rate: {prior:.3f}, Reputation: {rep:.4f}')
        lines.append('')

        for i, r in enumerate(sorted(rules, key=lambda x: x['n_samples'], reverse=True)):
            conds = ' AND '.join(r['conditions'])
            label = 'Presence' if r['prediction'] == 1 else 'Absence'
            lines.append(f'  Rule {i+1}: IF {conds}')
            lines.append(f'           THEN {label} '
                         f'(confidence={r["confidence"]:.2f}, samples={r["n_samples"]})')
        lines.append('')
        total += len(rules)

    lines.append(f'Total rules: {total}')
    return '\n'.join(lines)


report = format_doctor_rules(all_rules, zone_priors, zone_reputations, feature_cols)

with open('doctor_rules_opensource.txt', 'w') as f:
    f.write(report)

print(f'Saved {total_rules} rules to doctor_rules_opensource.txt')
print()
# Preview first 30 lines
for line in report.split('\n')[:30]:
    print(line)


# ## Export Sklearn Tree Visualizations

# Show sklearn's built-in text representation for the first export tree per zone
for zone, trees in sorted(export_trees.items()):
    if trees:
        print(f'\n=== Zone {zone} — Export Tree #1 ===')
        print(export_text(trees[0], feature_names=feature_cols,
                          class_names=['Absence', 'Presence'], max_depth=5))


# ## Generate Standalone Prediction Code
# 
# Pure Python — no ML libraries required.

def generate_standalone_code(all_rules, zone_priors, feature_cols):
    """Generate pure-Python prediction code from extracted rules."""
    lines = []
    lines.append('"""')
    lines.append('Standalone Heart Disease Prediction')
    lines.append('Generated from zone-structured ensemble export trees.')
    lines.append('No ML libraries required.')
    lines.append('"""')
    lines.append('')
    lines.append('')
    lines.append('def assign_zone(features):')
    lines.append('    """Assign patient to zone based on feature boundaries."""')
    lines.append(f'    vessels = features[{IDX_VESSELS}]   # Number of vessels fluro')
    lines.append(f'    thallium = features[{IDX_THALLIUM}]  # Thallium')
    lines.append(f'    return (1 if vessels > {VESSELS_THRESHOLD} else 0) * 2 + '
                 f'(1 if thallium > {THALLIUM_THRESHOLD} else 0)')
    lines.append('')
    lines.append('')

    # Generate a predict function per zone
    for zone, rules in sorted(all_rules.items()):
        lines.append(f'def predict_zone_{zone}(features):')
        lines.append(f'    """Predict for zone {zone}. {len(rules)} rules, majority vote."""')
        lines.append(f'    votes_0, votes_1 = 0, 0')

        for i, r in enumerate(rules):
            # Build condition string
            cond_parts = []
            for c in r['conditions']:
                # Parse "Feature Name <= 1.50" -> features[idx] <= 1.50
                for fi, fname in enumerate(feature_cols):
                    if c.startswith(fname):
                        rest = c[len(fname):].strip()
                        cond_parts.append(f'features[{fi}] {rest}')
                        break

            if cond_parts:
                cond_str = ' and '.join(cond_parts)
                pred_var = 'votes_1' if r['prediction'] == 1 else 'votes_0'
                lines.append(f'    if {cond_str}:')
                lines.append(f'        {pred_var} += 1')

        lines.append(f'    total = votes_0 + votes_1')
        lines.append(f'    if total == 0:')
        lines.append(f'        return {zone_priors.get(zone, 0.5):.4f}')
        lines.append(f'    return votes_1 / total')
        lines.append('')
        lines.append('')

    # Main predict function
    lines.append('def predict(features):')
    lines.append('    """Predict heart disease probability for a patient."""')
    lines.append('    zone = assign_zone(features)')
    zone_cases = ', '.join(
        f'{z}: predict_zone_{z}' for z in sorted(all_rules.keys())
    )
    lines.append(f'    zone_fn = {{{zone_cases}}}')
    lines.append('    return zone_fn.get(zone, lambda f: 0.5)(features)')
    lines.append('')

    return '\n'.join(lines)


standalone = generate_standalone_code(all_rules, zone_priors, feature_cols)

with open('standalone_predict_opensource.py', 'w') as f:
    f.write(standalone)

print(f'Saved standalone code ({len(standalone.splitlines())} lines)')
print()
# Preview
for line in standalone.split('\n')[:25]:
    print(line)


# ## Generate Submission

test_proba = predict_proba_zoned(
    X_test, zones_test, pred_models, calibrator, zone_priors, zone_reputations
)

submission = pd.DataFrame({
    'id': test['id'],
    'Heart Disease': test_proba,
})

submission.to_csv('submission_opensource.csv', index=False)

print(f'Submission: {submission.shape}')
print(f'Prob range: [{test_proba.min():.4f}, {test_proba.max():.4f}]')
print(f'Mean prob:  {test_proba.mean():.4f}')
print()
print(submission.head(10))


# ## Summary

print('=' * 60)
print('ZONE-STRUCTURED ENSEMBLE SUMMARY')
print('=' * 60)
print(f'Zones:             {len(pred_models)}')
print(f'Boundary features: Number of vessels fluro (>1.5), Thallium (>3.2)')
print(f'CV AUC:            {np.mean(fold_aucs):.5f} +/- {np.std(fold_aucs):.5f}')
print(f'Export rules:      {total_rules}')
print(f'Max rule depth:    {max_rule_depth}')
print()
for z in sorted(pred_models.keys()):
    pm = pred_models[z]
    n_pred = pm.n_estimators if pm else 0
    n_exp = len(export_trees.get(z, []))
    rep = zone_reputations.get(z, 0)
    print(f'  Zone {z}: pred={n_pred} trees (adaptive), '
          f'export={n_exp} trees (depth {EXPORT_MAX_DEPTH}), '
          f'reputation={rep:.4f}')
print()
print('Libraries: scikit-learn, numpy, pandas')
print('Done.')

