# Submission Notes — Williams Structured Random Forest

**Kaggle Playground Series S6E2 | Public Score: 0.94969**

These notes provide the detailed analysis behind the README's claims — feature importance inversion, regime findings, version comparisons, and the architectural deep dive that the README only summarizes.

---

## Architecture Overview

### Dual-Tree System

The WSRF uses two separate tree populations per zone:

1. **Prediction Trees** — Adaptive complexity RandomForests tuned for maximum discrimination. Tree count, depth, and other hyperparameters scale based on zone purity (see [Adaptive Complexity](#adaptive-complexity)).
2. **Export Trees** — Fixed 10 shallow trees per zone (depth 5), generating human-readable IF-THEN rules. These are the 1,275 rules in `doctor_rules_opensource.txt`.

### Zone Assignment

Patients are split into a 2×2 grid using two diagnostic thresholds:

- **Number of vessels fluro**: split at 1.5
- **Thallium**: split at 3.2

This creates 4 zones before any tree is trained. Each zone gets its own forest, its own calibration, and its own decision boundaries.

### Calibration Pipeline

1. Each zone's prediction trees produce out-of-bag (OOB) probability estimates
2. Isotonic regression is fitted on OOB predictions per zone — honest calibration on data the trees never saw
3. Zone prior blending mixes the calibrated probability with the zone's base disease rate (weight 0.05 in max power config)
4. Final prediction: average across 5 random seeds

---

## Version Comparison

Two open-source configurations exist, plus the internal WSRF version:

| | Standard (notebook) | Max Power (repo submission) | WSRF Internal |
|---|---|---|---|
| Trees per zone | 100 | 300 | Different config |
| Max depth | 15 | 20 | — |
| Seeds | 1 | 5 | — |
| CV AUC | 0.95180 | 0.95131 | 0.953 |
| Public LB | 0.94792 | **0.94969** | — |
| Export rules | 1,275 | 1,275 | 1,256 |

The max power config trades a marginal CV score decrease for a higher leaderboard score through variance reduction (5-seed averaging) and deeper trees that generalize better to the test distribution.

---

## Zone Statistics

From the actual training data:

| Zone | Patients | Share | Disease Rate | OOB AUC | Character |
|------|----------|-------|-------------|---------|-----------|
| 0 | 352,546 | 56.0% | 17.0% | 0.9072 | Mostly healthy — low vessels, low thallium |
| 1 | 200,294 | 31.8% | 76.5% | 0.8876 | Warning signs — low vessels, high thallium |
| 2 | 19,740 | 3.1% | 70.2% | 0.9015 | Rare but risky — high vessels, low thallium |
| 3 | 57,420 | 9.1% | 96.5% | 0.8599 | Almost certain — high vessels, high thallium |

```
                        Thallium
                     Low (≤3.2)      High (>3.2)
                   ┌───────────────┬──────────────────┐
                   │               │                  │
  Vessels     ≤1.5 │  ZONE 0       │  ZONE 1          │
  Fluro            │  352,546 pts  │  200,294 pts     │
                   │  17.0% risk   │  76.5% risk      │
                   │  AUC 0.9072   │  AUC 0.8876      │
                   ├───────────────┼──────────────────┤
               >1.5│  ZONE 2       │  ZONE 3          │
                   │  19,740 pts   │  57,420 pts      │
                   │  70.2% risk   │  96.5% risk      │
                   │  AUC 0.9015   │  AUC 0.8599      │
                   └───────────────┴──────────────────┘
```

Zone 3's OOB AUC (0.8599) is the lowest despite having the highest disease rate. This makes sense — when 96.5% of patients are positive, there's very little variation left to model. The adaptive complexity system correctly responds by reducing tree count for this zone.

---

## The Killer Finding — Feature Importance Inversion

This is the central insight of the zone-structured approach, and the reason a flat model leaves signal on the table.

### What the rules reveal

The first split in each zone's decision trees tells you what the forest considers most discriminative for that population:

| Zone | 1st split | 2nd split | 3rd split | Population |
|------|-----------|-----------|-----------|------------|
| 0 | Slope of ST | Age | Exercise angina | 56% of patients |
| 1 | Sex | Chest pain type | Slope of ST | 32% of patients |
| 2 | ST depression | Max HR | Chest pain type | 3% of patients |
| 3 | **Sex** | **Max HR** | **Slope of ST** | 9% of patients |

### The inversion

In **Zones 0–1** (87% of patients):
- Slope of ST, Age, Exercise angina, and Chest pain type dominate
- These are the "classic" cardiology predictors — exercise response, symptoms, demographics
- A flat model trained on all data will learn primarily these patterns because they cover the vast majority of patients

In **Zone 3** (9% of patients, the metabolic regime):
- **Sex, Max HR, Slope of ST, and Cholesterol** take over
- Chest pain type — the dominant predictor in most patients — drops to a secondary role
- The first rule in Zone 3 is `IF Sex ≤ 0.50 AND Max HR ≤ 161.50 AND Slope of ST ≤ 1.50 AND Cholesterol ≤ 229.50 AND Max HR ≤ 140.50 THEN Presence (0.95)`
- Cholesterol appears at the 4th level of Zone 3 rules — it barely appears in Zone 0 rules at all

### Why this matters

A flat model sees 87% of its training data dominated by chest pain and exercise response. The metabolic signal in Zone 3 — where sex, cholesterol, and max HR drive the prediction — gets **diluted** across the majority population. The flat model learns a compromise that serves neither population optimally.

The zone-structured approach lets Zone 3's metabolic signal speak for itself, undiluted by the 352K patients in Zone 0 where different features matter.

This is not a subtle effect. The **top-level split feature changes completely** between zones — from Slope of ST (Zone 0) to Sex (Zone 1, Zone 3) to ST depression (Zone 2). A single tree can't have four different root nodes.

---

## Per-Zone Top Predictors

Derived from the decision tree root splits and first three levels of the 1,275 export rules:

### Zone 0 — The Healthy Majority (352K patients, 17% disease rate)

**Top predictors:** Slope of ST, Age, Exercise angina

The trees first check whether the ST segment slope indicates abnormality, then stratify by age (54.5 threshold), then by exercise-induced angina. Chest pain type appears at level 4. This zone is about exercise physiology — can the heart handle stress?

**Example rule:**
```
IF Slope of ST ≤ 1.50
   AND Age ≤ 54.50
   AND Exercise angina ≤ 0.50
   AND Chest pain type ≤ 3.50
   AND Cholesterol ≤ 235.50
THEN Absence (confidence=0.98)
```

### Zone 1 — Warning Signs (200K patients, 77% disease rate)

**Top predictors:** Sex, Chest pain type, Slope of ST

With elevated thallium already indicating trouble, the trees differentiate by sex first, then chest pain presentation. EKG results appear at level 4-5. This zone is about symptom presentation on top of an already abnormal diagnostic marker.

### Zone 2 — Rare but Risky (20K patients, 70% disease rate)

**Top predictors:** ST depression, Max HR, Chest pain type

High vessel count with normal thallium is unusual. The trees focus on exercise ECG findings (ST depression magnitude, maximum heart rate achieved) before considering symptoms. This zone is about cardiac function under stress in patients with structural disease.

### Zone 3 — The Metabolic Regime (57K patients, 97% disease rate)

**Top predictors:** Sex, Max HR, Slope of ST, Cholesterol

Both diagnostic markers are elevated. Nearly everyone is positive. The trees focus on metabolic and demographic factors to identify the rare negatives. Cholesterol — almost irrelevant in Zone 0 — becomes a key differentiator. This is a fundamentally different decision boundary.

---

## Rule Structure

### Summary

- **Total rules:** 1,275 (open-source version)
- **Per zone:** Zone 0: 320, Zone 1: 320, Zone 2: 319, Zone 3: 316
- **Max depth:** 5 conditions per rule
- **Format:** `IF [condition_1 AND condition_2 AND ... AND condition_5] THEN Presence/Absence (confidence=X, samples=Y)`

### How rules are generated

The export trees (10 per zone, depth 5) are traversed leaf-to-leaf. Each leaf becomes one rule. With 10 binary trees of depth 5, each tree produces 2^5 = 32 leaves, giving ~320 rules per zone.

### Reading a rule

```
IF Slope of ST > 1.50
   AND ST depression ≤ 0.95
   AND Chest pain type ≤ 3.50
   AND Exercise angina ≤ 0.50
   AND Number of vessels fluro ≤ 0.50
THEN Absence (confidence=0.94, samples=1)
```

This says: if the ST slope is elevated but ST depression is low, chest pain isn't the worst type, no exercise angina, and no vessel blockage visible on fluoroscopy — predict absence with 94% confidence. A cardiologist would nod along.

---

## Adaptive Complexity

The system allocates modeling power inversely to zone purity:

| Zone | Base Rate | Purity | Trees (Max Power) | Depth | Rationale |
|------|-----------|--------|-------------------|-------|-----------|
| 0 | 0.170 | Low | 300 | 20 | Hard zone — 83/17 split needs deep exploration |
| 1 | 0.765 | Medium | 300 | 20 | Hard zone — 77/23 split, many borderline cases |
| 2 | 0.702 | Medium | 300 | 20 | Hard zone — 70/30 split, small sample |
| 3 | 0.965 | High (>0.9) | 90 | 15 | Easy zone — 97/3 split, answer is almost always "yes" |

**Scaling rules:**
- Purity > 0.9 → 0.3× trees, depth −3 (Zone 3)
- Purity 0.7–0.9 → 1× trees, standard depth (Zones 1, 2)
- Purity < 0.7 → 1.5× trees, depth +3 (Zone 0)

Zone 3 doesn't need 300 trees to figure out that 97% of patients are positive. It needs just enough to identify the 3% who aren't. Giving it the same resources as Zone 0 would be wasteful and risks overfitting on the small negative class.

---

## Cross-Validation Results

### 5-Fold CV (Standard Config: 100 trees, depth 15)

| Fold | AUC |
|------|-----|
| 1 | 0.95217 |
| 2 | 0.95139 |
| 3 | 0.95203 |
| 4 | 0.95129 |
| 5 | 0.95212 |
| **Mean** | **0.95180 ± 0.00038** |
| Train AUC | 0.96916 |

The extremely tight standard deviation (0.00038) across folds demonstrates that the zone-structured approach is stable — it's not finding a lucky split on one fold. The ~1.7% gap between train and CV AUC indicates mild overfitting, well within acceptable range for a tree ensemble.

### Max Power Config (300 trees, depth 20, 5 seeds)

- Quick 3-fold validation AUC: 0.95131
- **Public leaderboard: 0.94969**

The max power config slightly underperforms on CV compared to standard (0.95131 vs 0.95180) but outperforms on the public leaderboard (0.94969 vs 0.94792). The 5-seed averaging reduces variance on unseen data, which is exactly what you want for a competition submission.

---

## Why This Matters

### For clinicians

1,275 human-readable IF-THEN rules. No black box. Every prediction is traceable to a specific chain of clinical conditions. A cardiologist can read a rule, verify it against their clinical experience, and either trust it or flag it. Try doing that with a gradient-boosted ensemble of 10,000 trees.

### For data scientists

The feature importance inversion is proof that one-size-fits-all modeling leaves signal on the table. When different subpopulations have genuinely different decision boundaries, a flat model learns a compromise. The zone-structured approach lets each subpopulation find its own decision surface.

### For the field

Zone-structured modeling isn't limited to heart disease. Any domain where:
- Known diagnostic markers can segment the population
- Different subpopulations have different feature-outcome relationships
- Interpretability matters alongside accuracy

...can benefit from this architecture. The key insight is simple: **the zone IS the prediction**. By the time you've assigned a patient to Zone 3 (high vessels, high thallium), you've already done 90% of the diagnostic work. The zone-specific forest handles the remaining 10% with the right features for that population.

---

*Williams Structured Random Forest — William Lars Rocha, 2011*
