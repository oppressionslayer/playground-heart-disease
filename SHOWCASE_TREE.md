# The Unblackboxed Tree

A single decision tree from **Zone 13** of a WSRF HyperForest trained on
the Kaggle Heart Disease dataset (S6E2). This zone has 38 patients and
uses P2-structured features — the same equidistant distance math from
the original randomness experiments, now inside an actual ML model.

## The Tree

```
                        ┌─────────────────────┐
                        │  Age_dist_64 ≤ 0.28 │
                        │                     │
                        │  "Is this patient's  │
                        │   age close to 64?"  │
                        └──────────┬──────────┘
                          YES ╱         ╲ NO
                             ╱           ╲
                ┌────────────────┐  ┌────────────────┐
                │ Max HR_norm    │  │ BP_norm ≤ 0.48 │
                │    ≤ 0.82     │  │                │
                │               │  │ "Is blood      │
                │ "Is max heart │  │  pressure in    │
                │  rate < 82%   │  │  the lower      │
                │  of range?"   │  │  half?"         │
                └───────┬───────┘  └───────┬────────┘
                  YES ╱   ╲ NO       YES ╱   ╲ NO
                     ╱     ╲            ╱     ╲
          ┌──────────┐  ┌──────┐  ┌──────┐  ┌─────────┐
          │ Age_mod  │  │      │  │      │  │         │
          │  ≤ 0.09  │  │  ○   │  │  ○   │  │    ●    │
          │          │  │      │  │      │  │         │
          │ "Where   │  │ No   │  │ No   │  │ Heart   │
          │  in the  │  │ HD   │  │ HD   │  │ Disease │
          │  P2 cycle│  │      │  │      │  │         │
          │  is age?"│  └──────┘  └──────┘  └─────────┘
          └────┬─────┘
        YES ╱     ╲ NO
           ╱       ╲
      ┌──────┐  ┌─────────┐
      │      │  │         │
      │  ○   │  │    ●    │
      │      │  │         │
      │ No   │  │ Heart   │
      │ HD   │  │ Disease │
      │      │  │         │
      └──────┘  └─────────┘
```

**○ = Absence** (No Heart Disease)
**● = Presence** (Heart Disease)

## Reading the Tree

This tree makes a diagnosis in **3-4 questions**:

1. **Is the patient's age close to 64?** (`Age_dist_64 ≤ 0.28`)
   The P2 distance feature measures how close the age is to 64 (= 2^6),
   normalized by the feature range. Ages 46-82 are "close" (within 28%
   of range).

2. **If yes → check max heart rate.** (`Max HR_norm ≤ 0.82`)
   Normalized max HR below 82% of range suggests lower exercise capacity.

3. **If low HR → where in the P2 cycle is the age?** (`Age_mod ≤ 0.09`)
   The mod position captures cyclic structure. `Age_mod` is
   `(age - 20) % 44 / 44` — the position within the primary P2 step.
   Very low mod position (near a P2 boundary) → No Heart Disease.
   Higher mod position → Heart Disease.

4. **If age NOT close to 64 → check blood pressure.** (`BP_norm ≤ 0.48`)
   Low-normal BP → No Heart Disease. High BP → Heart Disease.

## Why This Tree Matters

This isn't a standalone model — it's one tree inside **Zone 13**, which
itself is one of 14 zones discovered by the P2 zone engine. The full
model has 298 trees and 21,669 splits, but this zone only needed
**24 splits across 7 trees** because the zone boundary already filtered
the data down to a specific patient subgroup.

The tree uses **P2-structured features** that traditional models don't have:

| Feature        | What It Is                                | Origin              |
|---------------|-------------------------------------------|---------------------|
| `Age_dist_64` | Distance from age to 64 (= 2^6)          | P2 Distance         |
| `Max HR_norm` | Max HR normalized to [0, 1]               | Normalization       |
| `Age_mod`     | Position within the P2 age cycle          | Equidistant Mod     |
| `BP_norm`     | Blood pressure normalized to [0, 1]       | Normalization       |

These features come from `P2Encoder.transform_augmented()` — auto-generated
from the expert schema. The same math that proves random numbers have
structure (distance from equidistant reference points) now helps trees
make better splits.

## The Big Picture

```
                    ┌──────────────┐
     Raw Data ───>  │   P2 Encoder │ ──> 55 augmented features
     (13 feat)      │  (auto-gen)  │     (raw + P2 distances +
                    └──────────────┘      mod positions + XOR parity)
                           │
                           v
                    ┌──────────────┐
                    │ Zone Discovery│ ──> 14 zones at P2 boundaries
                    │  (auto P2)   │     (Age>64, BP>128, Chol>256...)
                    └──────────────┘
                           │
              ┌────────────┼────────────────┐
              v            v                v
        ┌──────────┐ ┌──────────┐    ┌──────────┐
        │  Zone 3  │ │  Zone 4  │    │ Zone 13  │  ...14 zones
        │ 1770 pts │ │ 10726 pts│    │  38 pts  │
        │ 96% pure │ │ 85% pure │    │ 79% pure │
        │          │ │          │    │          │
        │ 10 trees │ │ 25 trees │    │ 7 trees  │
        │ depth: 3 │ │ depth: 10│    │ depth: 4 │
        │ 62 splits│ │7859 split│    │ 24 splits│  <── THIS TREE
        │          │ │          │    │          │
        │ "Almost  │ │ "Hard    │    │ "Small   │
        │  solved  │ │  cases,  │    │  group,  │
        │  by zone │ │  need    │    │  compact │
        │  routing"│ │  deep    │    │  P2 tree │
        │          │ │  trees"  │    │  decides"│
        └──────────┘ └──────────┘    └──────────┘

     Pure zones: 1-6 splits/tree    Impure: 54-314 splits/tree
     ────────────────────────────    ────────────────────────────
     Zone boundary already solved    Trees do the heavy lifting
     the classification. Trees       with full depth and many
     just confirm the obvious.       decision rules.
```

**Total: 298 trees, 21,669 splits — concentrated where they matter.**

Zone 3 has 1,770 patients but only needs 62 splits.
Zone 4 has 10,726 patients and needs 7,859 splits.

That's adaptive complexity: fewer, smarter if/then/elses.
