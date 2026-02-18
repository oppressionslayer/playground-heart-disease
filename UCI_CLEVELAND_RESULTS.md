# UCI Cleveland Heart Disease — WSRF P2 Results

Ran the full wsrf-hlib pipeline on the **original UCI Cleveland dataset**
(297 patients after dropping NaN, 13 features, binary classification).

---

### How zones are discovered

5-phase pipeline. On UCI Cleveland:

**Phase 1 — Feature screening.** Rank all 13 features by how cleanly a
single threshold separates disease/no-disease:
https://github.com/oppressionslayer/playground-heart-disease/blob/main/SHOWCASE_TREE.md
| Rank | Feature | Purity |
|------|---------|--------|
| 1 | thal (thalassemia type) | **0.764** |
| 2 | cp (chest pain type) | 0.754 |
| 3 | ca (vessels colored by fluoroscopy) | 0.744 |
| 4 | exang (exercise angina) | 0.710 |
| 5 | oldpeak (ST depression) | 0.694 |

**Phase 2 — P2 boundary scan.** Only test thresholds at powers of 2.
These are the 2^k values in each numeric feature's range:

| Feature | Range | P2 thresholds |
|---------|-------|---------------|
| age | [29, 77] | **32** (=2^5), **64** (=2^6) |
| resting BP | [94, 200] | **128** (=2^7) |
| cholesterol | [126, 564] | 128, **256** (=2^8), 512 |
| max HR | [71, 202] | 64, **128** (=2^7) |
| ST depression | [0, 6.2] | 1, 2, 4 |

On UCI Cleveland, the best 2-feature combo was **thalassemia type** and
**vessel count**:
- thal: {normal, fixed defect} vs {reversible defect}
- ca: 0-1 vessels vs 2+

That gives **4 zones** at purity 0.778:

| Zone | N | No Disease | Disease | Purity | What it means |
|------|---|-----------|---------|--------|---------------|
| 0 | 156 | 125 | 31 | 80% | Normal/fixed thal + few vessels → mostly healthy |
| 1 | 26 | 8 | 18 | 69% | Normal/fixed thal + 2+ vessels → leans disease |
| 2 | 83 | 25 | 58 | 70% | Reversible defect + few vessels → leans disease |
| 3 | 32 | 2 | 30 | **94%** | Reversible defect + 2+ vessels → almost certain disease |

Zone 3 is 94% disease from just two variables. Reversible thalassemia defect
with multiple diseased vessels — textbook high-risk subgroup.

**Phase 3 — Parity.** XOR on binary features (sex, fbs, exang). Found a
pattern (purity 0.700) but didn't beat Phase 2.

**Phase 4 — Interaction energy.** Pairwise feature interactions. Strongest:
chest pain ↔ cholesterol (1.35), chest pain ↔ resting ECG (1.31).

**Phase 5 — Selection.** Highest purity wins → 4 zones from Phase 2.

### What drives threshold selection

Powers of 2 that fall within each feature's data range. Not grid search, not
random — a small math-driven candidate set. The system tries all 2^k values
per feature, tests single and multi-feature combos, keeps whatever improves
purity. For categoricals like thal, the P2 encoding maps categories to
bitmask positions so thresholds land at category boundaries.

### Why 4 zones / does it vary

Zone count is **discovered from the data**:

| Dataset | Samples | Zones |
|---------|---------|-------|
| UCI Cleveland | 297 | **4** |
| Kaggle S6E2 (subsample) | 20,000 | **14** |
| Kaggle S6E2 (full) | 630,000 | **14** |

More data → more detectable structure → more zones. Different features →
different boundaries.

### Same P2 patterns as S6E2?

Same P2 reference points in both:
- age: **64** (=2^6) — both datasets
- BP: **128** (=2^7) — both datasets
- cholesterol: **256** (=2^8) — both datasets
- max HR: **128** (=2^7) — both datasets

These come from 2^k values falling within the feature range — same math,
same reference points, regardless of dataset. Zone boundaries differ because
the feature distributions differ, but the P2 structure is consistent.

### Performance on UCI Cleveland

P2 auto-generates 59 features from 13 raw. Zero manual engineering — just
an expert schema defining feature types and ranges.

| Method | Accuracy (5-CV) | AUC (5-CV) |
|--------|-----------------|------------|
| Traditional RF (13 raw features) | 0.805 ± 0.053 | 0.895 ± 0.043 |
| RF + P2 features (59) | 0.805 ± 0.062 | 0.892 ± 0.039 |
| LightGBM + P2 features (59) | 0.805 ± 0.051 | 0.875 ± 0.049 |
| **XGBoost + P2 features (59)** | **0.832 ± 0.040** | 0.889 ± 0.048 |

XGBoost with P2 features hits **0.832 accuracy** — 2.7 points above
traditional RF. AUC is in the same 0.89 range across the board. The
P2 features are auto-generated from the schema, no hand-crafting.

On the full Kaggle S6E2 (630K samples), the same P2 features + zone routing
+ LGB/XGB/HGB ensemble → **0.955 blended OOF AUC**.

### Per-zone feature importance — the "importance flip"

Different patient subgroups rely on different features. Traditional RF
averages this into one flat ranking and loses the subgroup structure:

| | Zone 0 (156 pts, healthy-leaning) | Zone 3 (32 pts, high-risk) | Zone 5 (49 pts, mixed) |
|-|----------------------------------|---------------------------|----------------------|
| #1 | ca (vessels) 0.084 | thalach_mod (HR cycle) **0.377** | age_dist_64 0.127 |
| #2 | age_mod (P2 cycle) 0.066 | trestbps (resting BP) 0.167 | age_norm 0.125 |
| #3 | age_dist_64 0.065 | trestbps_norm 0.167 | oldpeak_norm 0.073 |
| #4 | thalach_mod 0.056 | restecg_is_0 0.063 | chol_dist_256 0.069 |

`ca` (vessel count) is #1 in Zone 0, absent in Zone 3. `thalach_mod` (max HR
P2 cycle position) is #1 in Zone 3 at 0.377 importance, #4 in Zone 0.

### Adaptive complexity

Pure zones need almost nothing. Impure zones get the full treatment:

| Zone | Samples | Trees | Splits | Max Depth |
|------|---------|-------|--------|-----------|
| 0 (impure) | 156 | 25 | 347 | 10 |
| 3 (pure) | 32 | 6 | 7 | 2 |
| 4 (pure) | 14 | 3 | **1** | 1 |
| 5 (moderate) | 49 | 9 | 38 | 5 |

Zone 4: **1 split across 3 trees**. The boundary already solved it.
Zone 0: 347 splits — that's where the hard cases live.

### Patient-level explanations

```
Patient #0 — Actual: No disease
  Predicted: No disease (probability: 0.93)
  Zone 0 (normal thal, 0 vessels)
  Age=63, BP=145, Cholesterol=233, Max HR=150

Patient #1 — Actual: Disease
  Predicted: Disease (probability: 0.98)
  Zone 4 (3 vessels, exercise angina)
  Age=67, BP=160, Cholesterol=286, Max HR=108
```

Zone assignment, confidence, and which features mattered for that specific
subgroup. That's what you can't get from a flat model.

---

## Full Results Appendix

### Dataset

```
Samples:    297 (6 dropped for NaN in ca/thal)
Features:   13
No disease: 160 (53.9%)
Disease:    137 (46.1%)
```

| Feature | Min | Max | Mean | Type |
|---------|-----|-----|------|------|
| age | 29 | 77 | 54.5 | NUMERIC |
| sex | 0 | 1 | 0.7 | BINARY |
| cp (chest pain) | 1 | 4 | 3.2 | CATEGORICAL |
| trestbps (resting BP) | 94 | 200 | 131.7 | NUMERIC |
| chol (cholesterol) | 126 | 564 | 247.4 | NUMERIC |
| fbs (blood sugar > 120) | 0 | 1 | 0.1 | BINARY |
| restecg (resting ECG) | 0 | 2 | 1.0 | CATEGORICAL |
| thalach (max HR) | 71 | 202 | 149.6 | NUMERIC |
| exang (exercise angina) | 0 | 1 | 0.3 | BINARY |
| oldpeak (ST depression) | 0 | 6.2 | 1.1 | NUMERIC |
| slope (ST slope) | 1 | 3 | 1.6 | CATEGORICAL |
| ca (vessels colored) | 0 | 3 | 0.7 | ORDINAL |
| thal (thalassemia) | 3 | 7 | 4.7 | CATEGORICAL |

---

### Traditional RF Feature Importances

| Rank | Feature | Importance |
|------|---------|------------|
| 1 | Thalassemia (thal) | 0.130 |
| 2 | Chest pain type (cp) | 0.123 |
| 3 | Max heart rate (thalach) | 0.121 |
| 4 | Vessels colored (ca) | 0.120 |
| 5 | ST depression (oldpeak) | 0.103 |
| 6 | Age | 0.093 |
| 7 | Cholesterol (chol) | 0.079 |
| 8 | Resting BP (trestbps) | 0.073 |
| 9 | Exercise angina (exang) | 0.050 |
| 10 | ST slope | 0.046 |
| 11 | Sex | 0.033 |
| 12 | Resting ECG | 0.021 |
| 13 | Fasting blood sugar | 0.009 |

---

### Zone Discovery — 5-Phase Pipeline

#### P2 Thresholds in Clinical Feature Space

| Feature | Range | P2 Thresholds |
|---------|-------|---------------|
| age | [29, 77] | 32 (=2^5), 64 (=2^6) |
| trestbps | [94, 200] | 128 (=2^7) |
| chol | [126, 564] | 128 (=2^7), 256 (=2^8), 512 (=2^9) |
| thalach | [71, 202] | 128 (=2^7) |
| oldpeak | [0, 6.2] | 1 (=2^0), 2 (=2^1), 4 (=2^2) |

#### Phase 1 — Feature Screening

| Rank | Feature | Purity |
|------|---------|--------|
| 1 | thal (thalassemia) | **0.764** |
| 2 | cp (chest pain) | 0.754 |
| 3 | ca (vessels) | 0.744 |
| 4 | exang (exercise angina) | 0.710 |
| 5 | oldpeak (ST depression) | 0.694 |
| 6 | slope (ST slope) | 0.687 |
| 7 | thalach (max HR) | 0.633 |
| 8 | sex | 0.616 |
| 9 | restecg | 0.586 |
| 10 | chol | 0.569 |
| 11 | age | 0.539 |
| 12 | trestbps | 0.539 |
| 13 | fbs | 0.539 |

#### Phase 2 — P2 Boundary Scan

**4 zones**, purity = **0.778**

Boundaries:
- **Thalassemia**: {normal (3), fixed defect (6)} vs {reversible defect (7)}
- **Vessels colored**: 0-1 vs 2-3

| Zone | N | No Disease | Disease | Purity | Profile |
|------|---|-----------|---------|--------|---------|
| 0 | 156 | 125 | 31 | 80.1% | Mostly healthy |
| 1 | 26 | 8 | 18 | 69.2% | Mostly disease |
| 2 | 83 | 25 | 58 | 69.9% | Mostly disease |
| 3 | 32 | 2 | 30 | **93.8%** | Almost certain disease |

#### Phase 3 — Parity Detection

```
Method: XOR
Features: age, thal
Purity: 0.700 → doesn't beat Phase 2
```

#### Phase 4 — Feature Interaction Energy

| Feature A | Feature B | Energy |
|-----------|-----------|--------|
| Chest pain type | Cholesterol | 1.347 |
| Chest pain type | Resting ECG | 1.313 |
| Fasting blood sugar | ST slope | 1.276 |
| Chest pain type | Thalassemia | 1.168 |
| ST depression | ST slope | 1.034 |
| Sex | Chest pain type | 0.987 |

---

### P2 Augmented Features (13 → 59)

| Category | Count | Examples |
|----------|-------|---------|
| Raw values | 13 | age, sex, cp, trestbps, chol, ... |
| Normalized [0,1] | 5 | age_norm, trestbps_norm, chol_norm, ... |
| P2 Distance | 10 | age_dist_32, age_dist_64, trestbps_dist_128, chol_dist_256, ... |
| P2 Indicator | 10 | age_gt_32, age_gt_64, trestbps_gt_128, chol_gt_256, ... |
| Mod Position | 5 | age_mod, trestbps_mod, chol_mod, thalach_mod, oldpeak_mod |
| One-Hot | 13 | cp_is_1, cp_is_2, cp_is_3, cp_is_4, ... |
| Parity XOR | 3 | xor_sex_fbs, xor_sex_exang, xor_fbs_exang |

---

### Full Model Comparison

| Method | Accuracy (5-CV) | AUC (5-CV) |
|--------|-----------------|------------|
| Traditional RF (13 raw) | 0.805 ± 0.053 | 0.895 ± 0.043 |
| RF + P2 features (59) | 0.805 ± 0.062 | 0.892 ± 0.039 |
| LightGBM + P2 features (59) | 0.805 ± 0.051 | 0.875 ± 0.049 |
| **XGBoost + P2 features (59)** | **0.832 ± 0.040** | 0.889 ± 0.048 |

---

### Full Zone Stats (After Refinement)

| Zone | Samples | Trees | Splits | Avg Depth | Max Depth |
|------|---------|-------|--------|-----------|-----------|
| 0 | 156 | 25 | 347 | 6.7 | 10 |
| 1 | 12 | 3 | 4 | 1.3 | 2 |
| 2 | 13 | 3 | 4 | 1.3 | 2 |
| 3 | 32 | 6 | 7 | 1.2 | 2 |
| 4 | 14 | 3 | 1 | 0.3 | 1 |
| 5 | 49 | 9 | 38 | 3.7 | 5 |
| 6 | 7 | 3 | 4 | 1.3 | 2 |
| 7 | 14 | 3 | 5 | 1.7 | 2 |
| **Total** | **297** | **55** | **410** | | |

---

### Per-Zone Feature Importance (All Zones)

**Zone 0** (156 samples, 25 trees):

| Feature | Importance |
|---------|------------|https://github.com/oppressionslayer/playground-heart-disease/blob/main/SHOWCASE_TREE.md
| ca (vessels) | 0.084 |
| age_mod | 0.066 |
| age_dist_64 | 0.065 |
| thalach_mod | 0.056 |
| thalach | 0.053 |
| sex | 0.047 |

**Zone 1** (12 samples, 3 trees):

| Feature | Importance |
|---------|------------|
| trestbps_norm | 0.333 |
| ca (vessels) | 0.333 |
| thalach | 0.238 |

**Zone 2** (13 samples, 3 trees):

| Feature | Importance |
|---------|------------|
| age_mod | 0.333 |
| cp_is_2 | 0.333 |
| thalach_mod | 0.202 |
| chol_dist_256 | 0.131 |

**Zone 3** (32 samples, 6 trees):

| Feature | Importance |
|---------|------------|
| thalach_mod | 0.377 |
| trestbps | 0.167 |
| trestbps_norm | 0.167 |
| restecg_is_0 | 0.063 |
| age_dist_64 | 0.059 |

**Zone 4** (14 samples, 3 trees):

| Feature | Importance |
|---------|------------|
| age_dist_64 | 0.333 |

**Zone 5** (49 samples, 9 trees):

| Feature | Importance |
|---------|------------|
| age_dist_64 | 0.127 |
| age_norm | 0.125 |
| oldpeak_norm | 0.073 |
| chol_dist_256 | 0.069 |
| oldpeak | 0.060 |

**Zone 6** (7 samples, 3 trees):

| Feature | Importance |
|---------|------------|
| thalach_norm | 0.333 |
| thalach_mod | 0.333 |
| chol_dist_256 | 0.178 |
| slope | 0.156 |

**Zone 7** (14 samples, 3 trees):

| Feature | Importance |
|---------|------------|
| chol_dist_512 | 0.333 |
| ca | 0.240 |
| thalach_mod | 0.227 |
| trestbps_mod | 0.106 |

---

### UCI Cleveland vs Kaggle S6E2

| | UCI Cleveland | Kaggle S6E2 |
|-|---------------|-------------|
| Samples | 297 | 630,000 |
| Origin | Real clinical data | Synthetic (from UCI) |
| Zones discovered | 4 | 14 |
| Total trees | 55 | 298 |
| Total splits | 410 | 21,669 |
| P2 augmented features | 59 | 59 |
| Best P2 accuracy (5-CV) | **0.832** (XGB) | — |
| Blended OOF AUC | — | **0.955** |
| P2 thresholds (age) | 32, 64 | 32, 64 |
| P2 thresholds (BP) | 128 | 128 |
| P2 thresholds (chol) | 128, 256, 512 | 128, 256, 512 |
| P2 thresholds (max HR) | 64, 128 | 64, 128 |

Same P2 reference points on both datasets. Same math, same auto-generated
features, different data, consistent structure.
