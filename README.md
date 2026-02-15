# Heart Disease Prediction — Zone-Structured Ensemble

**Kaggle Playground Series S6E2 | Public Score: 0.94969**

One model? Nah. We split patients into **4 hyperdimensional zones** and give each zone its own army of decision trees. Hard zones get more firepower. Easy zones get the express lane. Every probability gets isotonic-calibrated on out-of-bag estimates. Then we average 5 random seeds because variance is the enemy.

No black boxes. 1,275 human-readable IF-THEN rules. A doctor could read them over coffee.

Built on the **Williams Structured Random Forest** architecture, invented by William Lars Rocha, 2011.

---

## How It Works

```
Patient comes in
        |
        v
  [Zone Assignment]
  Vessels fluro > 1.5?  x  Thallium > 3.2?
        |
   4 zones (2x2 grid)
        |
        v
  [Adaptive Random Forest per zone]
  Zone 0: 300 trees, depth 20  (hard zone, full power)
  Zone 1: 300 trees, depth 20  (hard zone, full power)
  Zone 2: 300 trees, depth 20  (hard zone, full power)
  Zone 3:  90 trees, depth 15  (easy zone, express lane)
        |
        v
  [OOB Isotonic Calibration]
        |
        v
  [5-seed averaging]
        |
        v
  Probability of heart disease
```

## The Zones

| Zone | Vessels | Thallium | Patients | Disease Rate | Vibe |
|------|---------|----------|----------|-------------|------|
| 0 | low | low | 352K (56%) | 17% | Mostly healthy |
| 1 | low | high | 200K (32%) | 77% | Warning signs |
| 2 | high | low | 20K (3%) | 70% | Rare but risky |
| 3 | high | high | 57K (9%) | 97% | Almost certain |

## Results

| Version | Config | CV AUC | Public LB |
|---------|--------|--------|-----------|
| Standard | 100 trees, depth 15, 1 seed | 0.95180 | 0.94792 |
| **Max Power** | **300 trees, depth 20, 5 seeds** | **0.95131** | **0.94969** |

## Files

| File | What It Does |
|------|-------------|
| `wsrf_opensource_kaggle.ipynb` | Full notebook with outputs — run it, read it, learn from it |
| `wsrf_opensource_kaggle.py` | Same thing as plain Python if notebooks aren't your thing |
| `wsrf_maxpower.py` | The 300-tree, 5-seed beast mode submission generator |
| `doctor_rules_opensource.txt` | 1,275 human-readable rules a doctor can actually use |
| `standalone_predict_opensource.py` | Pure Python predictor — zero ML libraries needed |
| `submission_maxpower.csv` | The Kaggle submission (0.94969) |
| `submission_opensource.csv` | Standard config submission |

## Run It

```bash
# Standard version (notebook or script)
python3 wsrf_opensource_kaggle.py

# Max power (300 trees x 5 seeds, ~4 minutes)
python3 wsrf_maxpower.py
```

Requires: `scikit-learn`, `numpy`, `pandas`. That's it.

## The Key Ideas

**Zones > Global.** Heart disease patients aren't one population. Someone with 3 blocked vessels and abnormal thallium is a completely different case than someone with clear vessels and normal thallium. Treating them the same wastes signal.

**Adaptive complexity.** Pure zones where the answer is obvious (Zone 3: 97% disease rate) don't need 300 deep trees. They get a lighter model. The hard zones where the class balance is close get the heavy treatment.

**OOB calibration.** Random Forests are notoriously bad at probability estimates. We fix that with isotonic regression fitted on out-of-bag predictions — honest probabilities that the model never trained on.

**Multi-seed averaging.** Train the same architecture 5 times with different random seeds. Average the predictions. Free variance reduction, zero overfitting risk.

---

*William Lars Rocha, 2011 — The zone IS the prediction. The math IS the model.*
