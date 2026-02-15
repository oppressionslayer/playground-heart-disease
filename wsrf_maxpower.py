"""
WSRF Open-Source — MAX POWER Edition
=====================================
Cranks everything to the max for the highest possible public score.

Strategy:
1. 300 trees/zone, depth 20, aggressive adaptive complexity
2. Train 5 models with different seeds on full data
3. Average all predictions (ensemble of ensembles)
4. Quick 3-fold CV to validate before submission

Memory management: train seeds sequentially, collect predictions, free model.
"""
import gc
import os
import sys
import time
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.isotonic import IsotonicRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_auc_score
import warnings
warnings.filterwarnings('ignore')

# ─── MAX POWER CONFIG ────────────────────────────────────────
BASE_TREES     = 300      # was 100
BASE_DEPTH     = 20       # was 15
PRIOR_WEIGHT   = 0.05     # was 0.1 — let the trees speak
N_SEEDS        = 5        # average 5 different random seeds
SEEDS          = [42, 123, 456, 789, 2025]
CV_FOLDS       = 3        # quick validation
MEMORY_LIMIT   = 0.80     # stop if memory hits 80%

EXPORT_TREES   = 10
EXPORT_DEPTH   = 5

# Feature indices for zone boundaries
IDX_VESSELS  = 11  # Number of vessels fluro
IDX_THALLIUM = 12  # Thallium
VESSELS_THRESH  = 1.5
THALLIUM_THRESH = 3.2


def check_memory():
    """Return memory usage fraction. Abort if over limit."""
    try:
        with open('/proc/meminfo') as f:
            lines = f.readlines()
        total = int(lines[0].split()[1])
        available = int(lines[2].split()[1])
        used_frac = 1.0 - (available / total)
        return used_frac
    except:
        return 0.0


def memory_guard(label=""):
    """Check memory and abort if too high."""
    usage = check_memory()
    gb_used = usage * 30  # approximate
    print(f'  [MEM] {label}: {usage*100:.1f}% ({gb_used:.1f}GB/30GB)')
    if usage > MEMORY_LIMIT:
        print(f'  [MEM] OVER {MEMORY_LIMIT*100:.0f}% LIMIT — stopping to protect system')
        sys.exit(1)
    return usage


def assign_zones(X):
    """Assign samples to zones based on discovered boundaries."""
    vessels_region  = (X[:, IDX_VESSELS]  > VESSELS_THRESH).astype(int)
    thallium_region = (X[:, IDX_THALLIUM] > THALLIUM_THRESH).astype(int)
    return vessels_region * 2 + thallium_region


def compute_zone_complexity(y_zone, base_trees=BASE_TREES, base_depth=BASE_DEPTH):
    """Adaptive complexity with MAX POWER settings."""
    purity = max(y_zone.mean(), 1 - y_zone.mean())
    zone_size = len(y_zone)
    size_factor = min(1.5, max(0.5, 1.0))  # neutral for now

    if purity > 0.9:
        tree_mult, depth_adj = 0.3, -5
    elif purity > 0.7:
        tree_mult, depth_adj = 1.0, 0
    else:
        tree_mult, depth_adj = 1.5, 3

    n_trees = max(20, int(base_trees * tree_mult * size_factor))
    max_depth = max(5, int(base_depth + depth_adj))
    return n_trees, max_depth, purity


def train_single_seed(X, y, zones, seed, verbose=True):
    """Train one full model with a given seed. Returns models + calibrator."""
    unique_zones = sorted(np.unique(zones))
    pred_models = {}
    zone_priors = {}
    oob_proba = np.full(len(y), np.nan)

    for z in unique_zones:
        mask = zones == z
        X_z, y_z = X[mask], y[mask]
        zone_priors[z] = y_z.mean()

        if len(np.unique(y_z)) <= 1:
            pred_models[z] = None
            oob_proba[mask] = y_z[0]
            continue

        n_trees, max_depth, purity = compute_zone_complexity(y_z)

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

        if hasattr(rf, 'oob_decision_function_'):
            oob_proba[mask] = rf.oob_decision_function_[:, 1]
        else:
            oob_proba[mask] = rf.predict_proba(X_z)[:, 1]

        if verbose:
            oob_auc = roc_auc_score(y_z, oob_proba[mask]) if len(np.unique(y_z)) > 1 else 0
            print(f'    Zone {z}: {n_trees} trees (depth {max_depth}), OOB AUC={oob_auc:.4f}')

    valid = ~np.isnan(oob_proba)
    calibrator = IsotonicRegression(out_of_bounds='clip')
    calibrator.fit(oob_proba[valid], y[valid])

    return pred_models, calibrator, zone_priors


def predict_single(X, zones, pred_models, calibrator, zone_priors):
    """Predict with a single model."""
    proba = np.zeros(len(X))
    for z in sorted(np.unique(zones)):
        mask = zones == z
        if not mask.any():
            continue
        model = pred_models.get(z)
        prior = zone_priors.get(z, 0.5)
        if model is None:
            proba[mask] = prior
        else:
            raw = model.predict_proba(X[mask])[:, 1]
            proba[mask] = (1 - PRIOR_WEIGHT) * raw + PRIOR_WEIGHT * prior
    proba = calibrator.predict(proba)
    return np.clip(proba, 1e-7, 1 - 1e-7)


def main():
    t_start = time.time()
    print('=' * 60)
    print('WSRF OPEN-SOURCE — MAX POWER EDITION')
    print(f'Config: {BASE_TREES} trees, depth {BASE_DEPTH}, {N_SEEDS} seeds')
    print('=' * 60)

    memory_guard('startup')

    # Load data
    train = pd.read_csv('train.csv')
    test  = pd.read_csv('test.csv')
    feature_cols = [c for c in train.columns if c not in ['id', 'Heart Disease']]
    X = train[feature_cols].values
    y = (train['Heart Disease'] == 'Presence').astype(int).values
    X_test = test[feature_cols].values
    zones = assign_zones(X)
    zones_test = assign_zones(X_test)

    print(f'\nData: {X.shape[0]:,} train, {X_test.shape[0]:,} test')
    memory_guard('data loaded')

    # ─── Quick 3-fold CV ─────────────────────────────────────
    print(f'\n--- Quick {CV_FOLDS}-fold CV (single seed) ---')
    skf = StratifiedKFold(n_splits=CV_FOLDS, shuffle=True, random_state=42)
    cv_aucs = []

    for fold, (tr_idx, va_idx) in enumerate(skf.split(X, y)):
        memory_guard(f'CV fold {fold+1} start')

        pm, cal, zp = train_single_seed(
            X[tr_idx], y[tr_idx], assign_zones(X[tr_idx]), seed=42, verbose=False
        )
        va_proba = predict_single(X[va_idx], assign_zones(X[va_idx]), pm, cal, zp)
        auc = roc_auc_score(y[va_idx], va_proba)
        cv_aucs.append(auc)
        print(f'  Fold {fold+1}: AUC = {auc:.5f}')

        del pm, cal, zp, va_proba
        gc.collect()

    mean_auc = np.mean(cv_aucs)
    print(f'  Mean CV AUC: {mean_auc:.5f} +/- {np.std(cv_aucs):.5f}')
    memory_guard('CV done')

    # ─── Multi-seed full training ────────────────────────────
    print(f'\n--- Multi-seed ensemble ({N_SEEDS} seeds) ---')
    test_probas = []
    seed_aucs = []

    for i, seed in enumerate(SEEDS):
        t0 = time.time()
        print(f'\n  Seed {i+1}/{N_SEEDS} (seed={seed}):')
        memory_guard(f'seed {seed} start')

        pm, cal, zp = train_single_seed(X, y, zones, seed=seed, verbose=True)

        # Train AUC (sanity)
        train_proba = predict_single(X, zones, pm, cal, zp)
        train_auc = roc_auc_score(y, train_proba)
        seed_aucs.append(train_auc)
        print(f'    Train AUC: {train_auc:.5f}')
        del train_proba

        # Test predictions
        test_proba = predict_single(X_test, zones_test, pm, cal, zp)
        test_probas.append(test_proba)

        elapsed = time.time() - t0
        total_elapsed = time.time() - t_start
        print(f'    Seed time: {elapsed:.0f}s, Total: {total_elapsed:.0f}s')

        # Free memory
        del pm, cal, zp, test_proba
        gc.collect()
        memory_guard(f'seed {seed} done')

    # ─── Average predictions ─────────────────────────────────
    print(f'\n--- Averaging {N_SEEDS} seed predictions ---')
    final_proba = np.mean(test_probas, axis=0)
    final_proba = np.clip(final_proba, 1e-7, 1 - 1e-7)

    print(f'  Prob range: [{final_proba.min():.4f}, {final_proba.max():.4f}]')
    print(f'  Mean prob:  {final_proba.mean():.4f}')

    # ─── Save submission ─────────────────────────────────────
    submission = pd.DataFrame({
        'id': test['id'],
        'Heart Disease': final_proba,
    })
    submission.to_csv('submission_maxpower.csv', index=False)

    # ─── Summary ─────────────────────────────────────────────
    total_time = time.time() - t_start
    print(f'\n{"=" * 60}')
    print('MAX POWER RESULTS')
    print(f'{"=" * 60}')
    print(f'Config:      {BASE_TREES} trees, depth {BASE_DEPTH}, prior weight {PRIOR_WEIGHT}')
    print(f'Seeds:       {SEEDS}')
    print(f'CV AUC:      {mean_auc:.5f} +/- {np.std(cv_aucs):.5f}')
    print(f'Train AUCs:  {[f"{a:.5f}" for a in seed_aucs]}')
    print(f'Submission:  submission_maxpower.csv')
    print(f'Total time:  {total_time/60:.1f} minutes')
    memory_guard('final')
    print(f'STATUS: DONE')


if __name__ == '__main__':
    main()
