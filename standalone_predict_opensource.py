"""
Standalone Heart Disease Prediction
Generated from zone-structured ensemble export trees.
No ML libraries required.
"""


def assign_zone(features):
    """Assign patient to zone based on feature boundaries."""
    vessels = features[11]   # Number of vessels fluro
    thallium = features[12]  # Thallium
    return (1 if vessels > 1.5 else 0) * 2 + (1 if thallium > 3.2 else 0)


def predict_zone_0(features):
    """Predict for zone 0. 320 rules, majority vote."""
    votes_0, votes_1 = 0, 0
    if features[10] <= 1.50 and features[0] <= 54.50 and features[8] <= 0.50 and features[2] <= 3.50 and features[4] <= 235.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 54.50 and features[8] <= 0.50 and features[2] <= 3.50 and features[4] > 235.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 54.50 and features[8] <= 0.50 and features[2] > 3.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 54.50 and features[8] <= 0.50 and features[2] > 3.50 and features[11] > 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 54.50 and features[8] > 0.50 and features[7] <= 147.50 and features[6] <= 1.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 54.50 and features[8] > 0.50 and features[7] <= 147.50 and features[6] > 1.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[0] <= 54.50 and features[8] > 0.50 and features[7] > 147.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 54.50 and features[8] > 0.50 and features[7] > 147.50 and features[1] > 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 54.50 and features[7] <= 146.50 and features[8] <= 0.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 54.50 and features[7] <= 146.50 and features[8] <= 0.50 and features[1] > 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 54.50 and features[7] <= 146.50 and features[8] > 0.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 54.50 and features[7] <= 146.50 and features[8] > 0.50 and features[1] > 0.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[0] > 54.50 and features[7] > 146.50 and features[8] <= 0.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 54.50 and features[7] > 146.50 and features[8] <= 0.50 and features[1] > 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 54.50 and features[7] > 146.50 and features[8] > 0.50 and features[0] <= 56.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 54.50 and features[7] > 146.50 and features[8] > 0.50 and features[0] > 56.50:
        votes_0 += 1
    if features[10] > 1.50 and features[9] <= 0.95 and features[2] <= 3.50 and features[8] <= 0.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[9] <= 0.95 and features[2] <= 3.50 and features[8] <= 0.50 and features[11] > 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[9] <= 0.95 and features[2] <= 3.50 and features[8] > 0.50 and features[7] <= 146.50:
        votes_1 += 1
    if features[10] > 1.50 and features[9] <= 0.95 and features[2] <= 3.50 and features[8] > 0.50 and features[7] > 146.50:
        votes_0 += 1
    if features[10] > 1.50 and features[9] <= 0.95 and features[2] > 3.50 and features[11] <= 0.50 and features[6] <= 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[9] <= 0.95 and features[2] > 3.50 and features[11] <= 0.50 and features[6] > 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[9] <= 0.95 and features[2] > 3.50 and features[11] > 0.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[10] > 1.50 and features[9] <= 0.95 and features[2] > 3.50 and features[11] > 0.50 and features[0] > 53.50:
        votes_1 += 1
    if features[10] > 1.50 and features[9] > 0.95 and features[11] <= 0.50 and features[7] <= 147.50 and features[9] <= 1.95:
        votes_1 += 1
    if features[10] > 1.50 and features[9] > 0.95 and features[11] <= 0.50 and features[7] <= 147.50 and features[9] > 1.95:
        votes_1 += 1
    if features[10] > 1.50 and features[9] > 0.95 and features[11] <= 0.50 and features[7] > 147.50 and features[9] <= 1.95:
        votes_0 += 1
    if features[10] > 1.50 and features[9] > 0.95 and features[11] <= 0.50 and features[7] > 147.50 and features[9] > 1.95:
        votes_0 += 1
    if features[10] > 1.50 and features[9] > 0.95 and features[11] > 0.50 and features[7] <= 160.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[9] > 0.95 and features[11] > 0.50 and features[7] <= 160.50 and features[1] > 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[9] > 0.95 and features[11] > 0.50 and features[7] > 160.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[9] > 0.95 and features[11] > 0.50 and features[7] > 160.50 and features[8] > 0.50:
        votes_1 += 1
    if features[0] <= 54.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[6] <= 0.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[6] <= 0.50 and features[11] > 0.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[6] > 0.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[6] > 0.50 and features[10] > 1.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] <= 43.50 and features[7] <= 135.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] <= 43.50 and features[7] > 135.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] > 43.50 and features[9] <= 1.05:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] > 43.50 and features[9] > 1.05:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] > 3.50 and features[9] <= 0.95 and features[6] <= 1.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] > 3.50 and features[9] <= 0.95 and features[6] <= 1.50 and features[10] > 1.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] > 3.50 and features[9] <= 0.95 and features[6] > 1.50 and features[0] <= 48.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] > 3.50 and features[9] <= 0.95 and features[6] > 1.50 and features[0] > 48.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] > 3.50 and features[9] > 0.95 and features[0] <= 53.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[0] <= 54.50 and features[2] > 3.50 and features[9] > 0.95 and features[0] <= 53.50 and features[1] > 0.50:
        votes_1 += 1
    if features[0] <= 54.50 and features[2] > 3.50 and features[9] > 0.95 and features[0] > 53.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[0] <= 54.50 and features[2] > 3.50 and features[9] > 0.95 and features[0] > 53.50 and features[11] > 0.50:
        votes_1 += 1
    if features[0] > 54.50 and features[7] <= 147.50 and features[2] <= 3.50 and features[4] <= 255.50 and features[7] <= 110.00:
        votes_1 += 1
    if features[0] > 54.50 and features[7] <= 147.50 and features[2] <= 3.50 and features[4] <= 255.50 and features[7] > 110.00:
        votes_0 += 1
    if features[0] > 54.50 and features[7] <= 147.50 and features[2] <= 3.50 and features[4] > 255.50 and features[6] <= 1.50:
        votes_0 += 1
    if features[0] > 54.50 and features[7] <= 147.50 and features[2] <= 3.50 and features[4] > 255.50 and features[6] > 1.50:
        votes_0 += 1
    if features[0] > 54.50 and features[7] <= 147.50 and features[2] > 3.50 and features[9] <= 0.95 and features[4] <= 227.00:
        votes_1 += 1
    if features[0] > 54.50 and features[7] <= 147.50 and features[2] > 3.50 and features[9] <= 0.95 and features[4] > 227.00:
        votes_1 += 1
    if features[0] > 54.50 and features[7] <= 147.50 and features[2] > 3.50 and features[9] > 0.95 and features[8] <= 0.50:
        votes_1 += 1
    if features[0] > 54.50 and features[7] <= 147.50 and features[2] > 3.50 and features[9] > 0.95 and features[8] > 0.50:
        votes_1 += 1
    if features[0] > 54.50 and features[7] > 147.50 and features[8] <= 0.50 and features[11] <= 0.50 and features[7] <= 161.50:
        votes_0 += 1
    if features[0] > 54.50 and features[7] > 147.50 and features[8] <= 0.50 and features[11] <= 0.50 and features[7] > 161.50:
        votes_0 += 1
    if features[0] > 54.50 and features[7] > 147.50 and features[8] <= 0.50 and features[11] > 0.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[0] > 54.50 and features[7] > 147.50 and features[8] <= 0.50 and features[11] > 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[0] > 54.50 and features[7] > 147.50 and features[8] > 0.50 and features[1] <= 0.50 and features[4] <= 235.50:
        votes_0 += 1
    if features[0] > 54.50 and features[7] > 147.50 and features[8] > 0.50 and features[1] <= 0.50 and features[4] > 235.50:
        votes_0 += 1
    if features[0] > 54.50 and features[7] > 147.50 and features[8] > 0.50 and features[1] > 0.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[0] > 54.50 and features[7] > 147.50 and features[8] > 0.50 and features[1] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[11] <= 0.50 and features[4] <= 242.50 and features[8] <= 0.50 and features[2] <= 3.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] <= 242.50 and features[8] <= 0.50 and features[2] <= 3.50 and features[1] > 0.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] <= 242.50 and features[8] <= 0.50 and features[2] > 3.50 and features[7] <= 147.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] <= 242.50 and features[8] <= 0.50 and features[2] > 3.50 and features[7] > 147.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] <= 242.50 and features[8] > 0.50 and features[7] <= 147.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] <= 242.50 and features[8] > 0.50 and features[7] <= 147.50 and features[2] > 3.50:
        votes_1 += 1
    if features[11] <= 0.50 and features[4] <= 242.50 and features[8] > 0.50 and features[7] > 147.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] <= 242.50 and features[8] > 0.50 and features[7] > 147.50 and features[1] > 0.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] > 242.50 and features[1] <= 0.50 and features[2] <= 3.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] > 242.50 and features[1] <= 0.50 and features[2] <= 3.50 and features[10] > 1.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] > 242.50 and features[1] <= 0.50 and features[2] > 3.50 and features[9] <= 1.15:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] > 242.50 and features[1] <= 0.50 and features[2] > 3.50 and features[9] > 1.15:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] > 242.50 and features[1] > 0.50 and features[10] <= 1.50 and features[9] <= 1.25:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] > 242.50 and features[1] > 0.50 and features[10] <= 1.50 and features[9] > 1.25:
        votes_0 += 1
    if features[11] <= 0.50 and features[4] > 242.50 and features[1] > 0.50 and features[10] > 1.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[11] <= 0.50 and features[4] > 242.50 and features[1] > 0.50 and features[10] > 1.50 and features[7] > 147.50:
        votes_0 += 1
    if features[11] > 0.50 and features[10] <= 1.50 and features[8] <= 0.50 and features[0] <= 53.50 and features[9] <= 2.25:
        votes_0 += 1
    if features[11] > 0.50 and features[10] <= 1.50 and features[8] <= 0.50 and features[0] <= 53.50 and features[9] > 2.25:
        votes_1 += 1
    if features[11] > 0.50 and features[10] <= 1.50 and features[8] <= 0.50 and features[0] > 53.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[11] > 0.50 and features[10] <= 1.50 and features[8] <= 0.50 and features[0] > 53.50 and features[1] > 0.50:
        votes_0 += 1
    if features[11] > 0.50 and features[10] <= 1.50 and features[8] > 0.50 and features[4] <= 241.00 and features[0] <= 51.50:
        votes_0 += 1
    if features[11] > 0.50 and features[10] <= 1.50 and features[8] > 0.50 and features[4] <= 241.00 and features[0] > 51.50:
        votes_1 += 1
    if features[11] > 0.50 and features[10] <= 1.50 and features[8] > 0.50 and features[4] > 241.00 and features[7] <= 147.50:
        votes_1 += 1
    if features[11] > 0.50 and features[10] <= 1.50 and features[8] > 0.50 and features[4] > 241.00 and features[7] > 147.50:
        votes_0 += 1
    if features[11] > 0.50 and features[10] > 1.50 and features[3] <= 179.00 and features[7] <= 160.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[11] > 0.50 and features[10] > 1.50 and features[3] <= 179.00 and features[7] <= 160.50 and features[2] > 3.50:
        votes_1 += 1
    if features[11] > 0.50 and features[10] > 1.50 and features[3] <= 179.00 and features[7] > 160.50 and features[9] <= 0.95:
        votes_0 += 1
    if features[11] > 0.50 and features[10] > 1.50 and features[3] <= 179.00 and features[7] > 160.50 and features[9] > 0.95:
        votes_1 += 1
    if features[11] > 0.50 and features[10] > 1.50 and features[3] > 179.00 and features[2] <= 3.50 and features[0] <= 53.50:
        votes_0 += 1
    if features[11] > 0.50 and features[10] > 1.50 and features[3] > 179.00 and features[2] <= 3.50 and features[0] > 53.50:
        votes_0 += 1
    if features[11] > 0.50 and features[10] > 1.50 and features[3] > 179.00 and features[2] > 3.50 and features[7] <= 170.50:
        votes_1 += 1
    if features[11] > 0.50 and features[10] > 1.50 and features[3] > 179.00 and features[2] > 3.50 and features[7] > 170.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[9] <= 1.15 and features[7] <= 110.00 and features[0] <= 49.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[9] <= 1.15 and features[7] <= 110.00 and features[0] > 49.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[9] <= 1.15 and features[7] > 110.00 and features[7] <= 130.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[9] <= 1.15 and features[7] > 110.00 and features[7] > 130.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[9] > 1.15 and features[10] <= 1.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[9] > 1.15 and features[10] <= 1.50 and features[11] > 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[9] > 1.15 and features[10] > 1.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[9] > 1.15 and features[10] > 1.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[1] <= 0.50 and features[4] <= 238.00 and features[9] <= 2.15:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[1] <= 0.50 and features[4] <= 238.00 and features[9] > 2.15:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[1] <= 0.50 and features[4] > 238.00 and features[9] <= 1.25:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[1] <= 0.50 and features[4] > 238.00 and features[9] > 1.25:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[1] > 0.50 and features[10] <= 1.50 and features[7] <= 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[1] > 0.50 and features[10] <= 1.50 and features[7] > 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[1] > 0.50 and features[10] > 1.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[1] > 0.50 and features[10] > 1.50 and features[8] > 0.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[3] <= 139.00 and features[11] <= 0.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[3] <= 139.00 and features[11] <= 0.50 and features[1] > 0.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[3] <= 139.00 and features[11] > 0.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[3] <= 139.00 and features[11] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[3] > 139.00 and features[1] <= 0.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[3] > 139.00 and features[1] <= 0.50 and features[11] > 0.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[3] > 139.00 and features[1] > 0.50 and features[0] <= 54.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[3] > 139.00 and features[1] > 0.50 and features[0] > 54.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[8] <= 0.50 and features[10] <= 1.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[8] <= 0.50 and features[10] <= 1.50 and features[7] > 147.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[8] <= 0.50 and features[10] > 1.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[8] <= 0.50 and features[10] > 1.50 and features[0] > 53.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[8] > 0.50 and features[7] <= 160.50 and features[9] <= 1.85:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[8] > 0.50 and features[7] <= 160.50 and features[9] > 1.85:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[8] > 0.50 and features[7] > 160.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[8] > 0.50 and features[7] > 160.50 and features[10] > 1.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[5] <= 0.50 and features[0] <= 54.50 and features[4] <= 245.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[5] <= 0.50 and features[0] <= 54.50 and features[4] > 245.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[5] <= 0.50 and features[0] > 54.50 and features[7] <= 147.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[5] <= 0.50 and features[0] > 54.50 and features[7] > 147.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[5] > 0.50 and features[7] <= 147.50 and features[9] <= 0.45:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[5] > 0.50 and features[7] <= 147.50 and features[9] > 0.45:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[5] > 0.50 and features[7] > 147.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[5] > 0.50 and features[7] > 147.50 and features[2] > 3.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[8] <= 0.50 and features[3] <= 139.00 and features[6] <= 1.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[8] <= 0.50 and features[3] <= 139.00 and features[6] > 1.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[8] <= 0.50 and features[3] > 139.00 and features[9] <= 0.95:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[8] <= 0.50 and features[3] > 139.00 and features[9] > 0.95:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[8] > 0.50 and features[1] <= 0.50 and features[6] <= 1.00:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[8] > 0.50 and features[1] <= 0.50 and features[6] > 1.00:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] <= 247.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] > 247.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] <= 140.50 and features[7] <= 110.00:
        votes_1 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] <= 140.50 and features[7] > 110.00:
        votes_0 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] > 140.50 and features[6] <= 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] > 140.50 and features[6] > 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[8] > 0.50 and features[11] <= 0.50 and features[4] <= 237.50:
        votes_0 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[8] > 0.50 and features[11] <= 0.50 and features[4] > 237.50:
        votes_0 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[8] > 0.50 and features[11] > 0.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[8] > 0.50 and features[11] > 0.50 and features[6] > 1.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[11] <= 0.50 and features[7] <= 147.50 and features[9] <= 0.95:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[11] <= 0.50 and features[7] <= 147.50 and features[9] > 0.95:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[11] <= 0.50 and features[7] > 147.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[11] <= 0.50 and features[7] > 147.50 and features[8] > 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[11] > 0.50 and features[7] <= 160.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[11] > 0.50 and features[7] <= 160.50 and features[8] > 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[11] > 0.50 and features[7] > 160.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[11] > 0.50 and features[7] > 160.50 and features[8] > 0.50:
        votes_1 += 1
    if features[6] <= 1.50 and features[10] <= 1.50 and features[7] <= 147.50 and features[4] <= 255.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] <= 1.50 and features[7] <= 147.50 and features[4] <= 255.50 and features[8] > 0.50:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] <= 1.50 and features[7] <= 147.50 and features[4] > 255.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] <= 1.50 and features[7] <= 147.50 and features[4] > 255.50 and features[2] > 3.50:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] <= 1.50 and features[7] > 147.50 and features[7] <= 161.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] <= 1.50 and features[7] > 147.50 and features[7] <= 161.50 and features[8] > 0.50:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] <= 1.50 and features[7] > 147.50 and features[7] > 161.50 and features[9] <= 1.95:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] <= 1.50 and features[7] > 147.50 and features[7] > 161.50 and features[9] > 1.95:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] > 1.50 and features[7] <= 147.50 and features[2] <= 3.50 and features[7] <= 121.00:
        votes_1 += 1
    if features[6] <= 1.50 and features[10] > 1.50 and features[7] <= 147.50 and features[2] <= 3.50 and features[7] > 121.00:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] > 1.50 and features[7] <= 147.50 and features[2] > 3.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[6] <= 1.50 and features[10] > 1.50 and features[7] <= 147.50 and features[2] > 3.50 and features[1] > 0.50:
        votes_1 += 1
    if features[6] <= 1.50 and features[10] > 1.50 and features[7] > 147.50 and features[4] <= 204.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] > 1.50 and features[7] > 147.50 and features[4] <= 204.50 and features[1] > 0.50:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] > 1.50 and features[7] > 147.50 and features[4] > 204.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[6] <= 1.50 and features[10] > 1.50 and features[7] > 147.50 and features[4] > 204.50 and features[1] > 0.50:
        votes_0 += 1
    if features[6] > 1.50 and features[11] <= 0.50 and features[8] <= 0.50 and features[7] <= 147.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[6] > 1.50 and features[11] <= 0.50 and features[8] <= 0.50 and features[7] <= 147.50 and features[2] > 3.50:
        votes_1 += 1
    if features[6] > 1.50 and features[11] <= 0.50 and features[8] <= 0.50 and features[7] > 147.50 and features[9] <= 1.05:
        votes_0 += 1
    if features[6] > 1.50 and features[11] <= 0.50 and features[8] <= 0.50 and features[7] > 147.50 and features[9] > 1.05:
        votes_0 += 1
    if features[6] > 1.50 and features[11] <= 0.50 and features[8] > 0.50 and features[7] <= 147.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[6] > 1.50 and features[11] <= 0.50 and features[8] > 0.50 and features[7] <= 147.50 and features[0] > 53.50:
        votes_1 += 1
    if features[6] > 1.50 and features[11] <= 0.50 and features[8] > 0.50 and features[7] > 147.50 and features[4] <= 255.50:
        votes_0 += 1
    if features[6] > 1.50 and features[11] <= 0.50 and features[8] > 0.50 and features[7] > 147.50 and features[4] > 255.50:
        votes_0 += 1
    if features[6] > 1.50 and features[11] > 0.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] <= 140.50:
        votes_0 += 1
    if features[6] > 1.50 and features[11] > 0.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] > 140.50:
        votes_0 += 1
    if features[6] > 1.50 and features[11] > 0.50 and features[2] <= 3.50 and features[8] > 0.50 and features[9] <= 0.75:
        votes_0 += 1
    if features[6] > 1.50 and features[11] > 0.50 and features[2] <= 3.50 and features[8] > 0.50 and features[9] > 0.75:
        votes_1 += 1
    if features[6] > 1.50 and features[11] > 0.50 and features[2] > 3.50 and features[9] <= 0.45 and features[7] <= 147.50:
        votes_1 += 1
    if features[6] > 1.50 and features[11] > 0.50 and features[2] > 3.50 and features[9] <= 0.45 and features[7] > 147.50:
        votes_0 += 1
    if features[6] > 1.50 and features[11] > 0.50 and features[2] > 3.50 and features[9] > 0.45 and features[0] <= 53.50:
        votes_1 += 1
    if features[6] > 1.50 and features[11] > 0.50 and features[2] > 3.50 and features[9] > 0.45 and features[0] > 53.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[7] <= 137.50 and features[7] <= 110.00 and features[1] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[7] <= 137.50 and features[7] <= 110.00 and features[1] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[7] <= 137.50 and features[7] > 110.00 and features[1] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[7] <= 137.50 and features[7] > 110.00 and features[1] > 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[7] > 137.50 and features[9] <= 1.95 and features[7] <= 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[7] > 137.50 and features[9] <= 1.95 and features[7] > 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[7] > 137.50 and features[9] > 1.95 and features[0] <= 55.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[7] > 137.50 and features[9] > 1.95 and features[0] > 55.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[1] <= 0.50 and features[0] <= 51.50 and features[9] <= 1.35:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[1] <= 0.50 and features[0] <= 51.50 and features[9] > 1.35:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[1] <= 0.50 and features[0] > 51.50 and features[6] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[1] <= 0.50 and features[0] > 51.50 and features[6] > 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] <= 255.50 and features[6] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] <= 255.50 and features[6] > 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] > 255.50 and features[0] <= 53.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] > 255.50 and features[0] > 53.50:
        votes_0 += 1
    if features[2] > 3.50 and features[10] <= 1.50 and features[8] <= 0.50 and features[1] <= 0.50 and features[7] <= 147.50:
        votes_0 += 1
    if features[2] > 3.50 and features[10] <= 1.50 and features[8] <= 0.50 and features[1] <= 0.50 and features[7] > 147.50:
        votes_0 += 1
    if features[2] > 3.50 and features[10] <= 1.50 and features[8] <= 0.50 and features[1] > 0.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[2] > 3.50 and features[10] <= 1.50 and features[8] <= 0.50 and features[1] > 0.50 and features[11] > 0.50:
        votes_0 += 1
    if features[2] > 3.50 and features[10] <= 1.50 and features[8] > 0.50 and features[11] <= 0.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[2] > 3.50 and features[10] <= 1.50 and features[8] > 0.50 and features[11] <= 0.50 and features[7] > 147.50:
        votes_0 += 1
    if features[2] > 3.50 and features[10] <= 1.50 and features[8] > 0.50 and features[11] > 0.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[10] <= 1.50 and features[8] > 0.50 and features[11] > 0.50 and features[1] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[10] > 1.50 and features[4] <= 241.00 and features[8] <= 0.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[2] > 3.50 and features[10] > 1.50 and features[4] <= 241.00 and features[8] <= 0.50 and features[11] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[10] > 1.50 and features[4] <= 241.00 and features[8] > 0.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[10] > 1.50 and features[4] <= 241.00 and features[8] > 0.50 and features[11] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[10] > 1.50 and features[4] > 241.00 and features[1] <= 0.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[2] > 3.50 and features[10] > 1.50 and features[4] > 241.00 and features[1] <= 0.50 and features[7] > 147.50:
        votes_0 += 1
    if features[2] > 3.50 and features[10] > 1.50 and features[4] > 241.00 and features[1] > 0.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[2] > 3.50 and features[10] > 1.50 and features[4] > 241.00 and features[1] > 0.50 and features[7] > 147.50:
        votes_1 += 1
    if features[11] <= 0.50 and features[6] <= 1.50 and features[7] <= 146.50 and features[1] <= 0.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] <= 1.50 and features[7] <= 146.50 and features[1] <= 0.50 and features[2] > 3.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] <= 1.50 and features[7] <= 146.50 and features[1] > 0.50 and features[9] <= 0.95:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] <= 1.50 and features[7] <= 146.50 and features[1] > 0.50 and features[9] > 0.95:
        votes_1 += 1
    if features[11] <= 0.50 and features[6] <= 1.50 and features[7] > 146.50 and features[10] <= 1.50 and features[9] <= 1.95:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] <= 1.50 and features[7] > 146.50 and features[10] <= 1.50 and features[9] > 1.95:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] <= 1.50 and features[7] > 146.50 and features[10] > 1.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] <= 1.50 and features[7] > 146.50 and features[10] > 1.50 and features[2] > 3.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] > 1.50 and features[9] <= 0.95 and features[2] <= 3.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] > 1.50 and features[9] <= 0.95 and features[2] <= 3.50 and features[1] > 0.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] > 1.50 and features[9] <= 0.95 and features[2] > 3.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] > 1.50 and features[9] <= 0.95 and features[2] > 3.50 and features[10] > 1.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] > 1.50 and features[9] > 0.95 and features[3] <= 147.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] > 1.50 and features[9] > 0.95 and features[3] <= 147.50 and features[1] > 0.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] > 1.50 and features[9] > 0.95 and features[3] > 147.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[11] <= 0.50 and features[6] > 1.50 and features[9] > 0.95 and features[3] > 147.50 and features[8] > 0.50:
        votes_1 += 1
    if features[11] > 0.50 and features[7] <= 147.50 and features[9] <= 0.95 and features[1] <= 0.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[11] > 0.50 and features[7] <= 147.50 and features[9] <= 0.95 and features[1] <= 0.50 and features[8] > 0.50:
        votes_1 += 1
    if features[11] > 0.50 and features[7] <= 147.50 and features[9] <= 0.95 and features[1] > 0.50 and features[0] <= 53.50:
        votes_0 += 1
    if features[11] > 0.50 and features[7] <= 147.50 and features[9] <= 0.95 and features[1] > 0.50 and features[0] > 53.50:
        votes_1 += 1
    if features[11] > 0.50 and features[7] <= 147.50 and features[9] > 0.95 and features[1] <= 0.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[11] > 0.50 and features[7] <= 147.50 and features[9] > 0.95 and features[1] <= 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[11] > 0.50 and features[7] <= 147.50 and features[9] > 0.95 and features[1] > 0.50 and features[3] <= 119.00:
        votes_1 += 1
    if features[11] > 0.50 and features[7] <= 147.50 and features[9] > 0.95 and features[1] > 0.50 and features[3] > 119.00:
        votes_1 += 1
    if features[11] > 0.50 and features[7] > 147.50 and features[1] <= 0.50 and features[8] <= 0.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[11] > 0.50 and features[7] > 147.50 and features[1] <= 0.50 and features[8] <= 0.50 and features[10] > 1.50:
        votes_0 += 1
    if features[11] > 0.50 and features[7] > 147.50 and features[1] <= 0.50 and features[8] > 0.50 and features[9] <= 1.15:
        votes_0 += 1
    if features[11] > 0.50 and features[7] > 147.50 and features[1] <= 0.50 and features[8] > 0.50 and features[9] > 1.15:
        votes_1 += 1
    if features[11] > 0.50 and features[7] > 147.50 and features[1] > 0.50 and features[0] <= 53.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[11] > 0.50 and features[7] > 147.50 and features[1] > 0.50 and features[0] <= 53.50 and features[2] > 3.50:
        votes_0 += 1
    if features[11] > 0.50 and features[7] > 147.50 and features[1] > 0.50 and features[0] > 53.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[11] > 0.50 and features[7] > 147.50 and features[1] > 0.50 and features[0] > 53.50 and features[7] > 160.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] <= 0.50 and features[2] <= 3.50 and features[0] <= 48.50 and features[7] <= 110.00:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] <= 0.50 and features[2] <= 3.50 and features[0] <= 48.50 and features[7] > 110.00:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] <= 0.50 and features[2] <= 3.50 and features[0] > 48.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] <= 0.50 and features[2] <= 3.50 and features[0] > 48.50 and features[10] > 1.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] <= 0.50 and features[2] > 3.50 and features[9] <= 1.05 and features[7] <= 147.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] <= 0.50 and features[2] > 3.50 and features[9] <= 1.05 and features[7] > 147.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] <= 0.50 and features[2] > 3.50 and features[9] > 1.05 and features[4] <= 265.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] <= 0.50 and features[2] > 3.50 and features[9] > 1.05 and features[4] > 265.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] > 0.50 and features[7] <= 147.50 and features[10] <= 1.50 and features[9] <= 0.95:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] > 0.50 and features[7] <= 147.50 and features[10] <= 1.50 and features[9] > 0.95:
        votes_1 += 1
    if features[0] <= 53.50 and features[8] > 0.50 and features[7] <= 147.50 and features[10] > 1.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] > 0.50 and features[7] <= 147.50 and features[10] > 1.50 and features[2] > 3.50:
        votes_1 += 1
    if features[0] <= 53.50 and features[8] > 0.50 and features[7] > 147.50 and features[2] <= 3.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] > 0.50 and features[7] > 147.50 and features[2] <= 3.50 and features[1] > 0.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] > 0.50 and features[7] > 147.50 and features[2] > 3.50 and features[9] <= 0.95:
        votes_0 += 1
    if features[0] <= 53.50 and features[8] > 0.50 and features[7] > 147.50 and features[2] > 3.50 and features[9] > 0.95:
        votes_1 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[7] <= 146.50 and features[8] <= 0.50 and features[7] <= 110.00:
        votes_1 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[7] <= 146.50 and features[8] <= 0.50 and features[7] > 110.00:
        votes_0 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[7] <= 146.50 and features[8] > 0.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[7] <= 146.50 and features[8] > 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[7] > 146.50 and features[2] <= 3.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[7] > 146.50 and features[2] <= 3.50 and features[1] > 0.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[7] > 146.50 and features[2] > 3.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[7] > 146.50 and features[2] > 3.50 and features[8] > 0.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[2] <= 3.50 and features[10] <= 1.50 and features[7] <= 146.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[2] <= 3.50 and features[10] <= 1.50 and features[7] > 146.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[2] <= 3.50 and features[10] > 1.50 and features[2] <= 2.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[2] <= 3.50 and features[10] > 1.50 and features[2] > 2.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[2] > 3.50 and features[1] <= 0.50 and features[9] <= 1.85:
        votes_0 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[2] > 3.50 and features[1] <= 0.50 and features[9] > 1.85:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[2] > 3.50 and features[1] > 0.50 and features[3] <= 123.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[2] > 3.50 and features[1] > 0.50 and features[3] > 123.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[0] <= 54.50 and features[11] <= 0.50 and features[6] <= 1.50 and features[6] <= 0.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] <= 54.50 and features[11] <= 0.50 and features[6] <= 1.50 and features[6] > 0.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] <= 54.50 and features[11] <= 0.50 and features[6] > 1.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] <= 54.50 and features[11] <= 0.50 and features[6] > 1.50 and features[2] > 3.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] <= 54.50 and features[11] > 0.50 and features[9] <= 1.05 and features[10] <= 1.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] <= 54.50 and features[11] > 0.50 and features[9] <= 1.05 and features[10] > 1.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] <= 54.50 and features[11] > 0.50 and features[9] > 1.05 and features[10] <= 1.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] <= 54.50 and features[11] > 0.50 and features[9] > 1.05 and features[10] > 1.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[0] > 54.50 and features[10] <= 1.50 and features[2] <= 3.50 and features[4] <= 257.00:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] > 54.50 and features[10] <= 1.50 and features[2] <= 3.50 and features[4] > 257.00:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] > 54.50 and features[10] <= 1.50 and features[2] > 3.50 and features[6] <= 1.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] > 54.50 and features[10] <= 1.50 and features[2] > 3.50 and features[6] > 1.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] > 54.50 and features[10] > 1.50 and features[1] <= 0.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] > 54.50 and features[10] > 1.50 and features[1] <= 0.50 and features[11] > 0.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] > 54.50 and features[10] > 1.50 and features[1] > 0.50 and features[0] <= 63.50:
        votes_0 += 1
    if features[8] <= 0.50 and features[0] > 54.50 and features[10] > 1.50 and features[1] > 0.50 and features[0] > 63.50:
        votes_0 += 1
    if features[8] > 0.50 and features[1] <= 0.50 and features[11] <= 0.50 and features[2] <= 3.50 and features[6] <= 1.50:
        votes_0 += 1
    if features[8] > 0.50 and features[1] <= 0.50 and features[11] <= 0.50 and features[2] <= 3.50 and features[6] > 1.50:
        votes_0 += 1
    if features[8] > 0.50 and features[1] <= 0.50 and features[11] <= 0.50 and features[2] > 3.50 and features[7] <= 146.50:
        votes_1 += 1
    if features[8] > 0.50 and features[1] <= 0.50 and features[11] <= 0.50 and features[2] > 3.50 and features[7] > 146.50:
        votes_0 += 1
    if features[8] > 0.50 and features[1] <= 0.50 and features[11] > 0.50 and features[0] <= 56.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[8] > 0.50 and features[1] <= 0.50 and features[11] > 0.50 and features[0] <= 56.50 and features[7] > 147.50:
        votes_0 += 1
    if features[8] > 0.50 and features[1] <= 0.50 and features[11] > 0.50 and features[0] > 56.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[8] > 0.50 and features[1] <= 0.50 and features[11] > 0.50 and features[0] > 56.50 and features[2] > 3.50:
        votes_1 += 1
    if features[8] > 0.50 and features[1] > 0.50 and features[2] <= 3.50 and features[7] <= 147.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[8] > 0.50 and features[1] > 0.50 and features[2] <= 3.50 and features[7] <= 147.50 and features[10] > 1.50:
        votes_1 += 1
    if features[8] > 0.50 and features[1] > 0.50 and features[2] <= 3.50 and features[7] > 147.50 and features[9] <= 1.15:
        votes_0 += 1
    if features[8] > 0.50 and features[1] > 0.50 and features[2] <= 3.50 and features[7] > 147.50 and features[9] > 1.15:
        votes_0 += 1
    if features[8] > 0.50 and features[1] > 0.50 and features[2] > 3.50 and features[0] <= 53.50 and features[0] <= 47.50:
        votes_1 += 1
    if features[8] > 0.50 and features[1] > 0.50 and features[2] > 3.50 and features[0] <= 53.50 and features[0] > 47.50:
        votes_1 += 1
    if features[8] > 0.50 and features[1] > 0.50 and features[2] > 3.50 and features[0] > 53.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[8] > 0.50 and features[1] > 0.50 and features[2] > 3.50 and features[0] > 53.50 and features[6] > 1.50:
        votes_1 += 1
    total = votes_0 + votes_1
    if total == 0:
        return 0.1698
    return votes_1 / total


def predict_zone_1(features):
    """Predict for zone 1. 320 rules, majority vote."""
    votes_0, votes_1 = 0, 0
    if features[1] <= 0.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[12] <= 6.50 and features[6] <= 1.00:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[12] <= 6.50 and features[6] > 1.00:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[12] > 6.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[12] > 6.50 and features[11] > 0.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[10] > 1.50 and features[6] <= 1.50 and features[0] <= 51.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[10] > 1.50 and features[6] <= 1.50 and features[0] > 51.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[10] > 1.50 and features[6] > 1.50 and features[9] <= 0.95:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[10] > 1.50 and features[6] > 1.50 and features[9] > 0.95:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[7] <= 160.50 and features[0] <= 53.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[7] <= 160.50 and features[0] <= 53.50 and features[11] > 0.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[7] <= 160.50 and features[0] > 53.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[7] <= 160.50 and features[0] > 53.50 and features[8] > 0.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[7] > 160.50 and features[8] <= 0.50 and features[4] <= 312.00:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[7] > 160.50 and features[8] <= 0.50 and features[4] > 312.00:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[7] > 160.50 and features[8] > 0.50 and features[0] <= 47.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[7] > 160.50 and features[8] > 0.50 and features[0] > 47.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] <= 1.50 and features[9] <= 0.85 and features[8] <= 0.50 and features[5] <= 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] <= 1.50 and features[9] <= 0.85 and features[8] <= 0.50 and features[5] > 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] <= 1.50 and features[9] <= 0.85 and features[8] > 0.50 and features[2] <= 3.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] <= 1.50 and features[9] <= 0.85 and features[8] > 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] <= 1.50 and features[9] > 0.85 and features[8] <= 0.50 and features[9] <= 1.95:
        votes_1 += 1
    if features[1] > 0.50 and features[10] <= 1.50 and features[9] > 0.85 and features[8] <= 0.50 and features[9] > 1.95:
        votes_1 += 1
    if features[1] > 0.50 and features[10] <= 1.50 and features[9] > 0.85 and features[8] > 0.50 and features[2] <= 3.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] <= 1.50 and features[9] > 0.85 and features[8] > 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] > 1.50 and features[12] <= 6.50 and features[4] <= 196.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] > 1.50 and features[12] <= 6.50 and features[4] <= 196.50 and features[11] > 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] > 1.50 and features[12] <= 6.50 and features[4] > 196.50 and features[9] <= 0.85:
        votes_1 += 1
    if features[1] > 0.50 and features[10] > 1.50 and features[12] <= 6.50 and features[4] > 196.50 and features[9] > 0.85:
        votes_1 += 1
    if features[1] > 0.50 and features[10] > 1.50 and features[12] > 6.50 and features[8] <= 0.50 and features[9] <= 0.95:
        votes_1 += 1
    if features[1] > 0.50 and features[10] > 1.50 and features[12] > 6.50 and features[8] <= 0.50 and features[9] > 0.95:
        votes_1 += 1
    if features[1] > 0.50 and features[10] > 1.50 and features[12] > 6.50 and features[8] > 0.50 and features[4] <= 198.50:
        votes_1 += 1
    if features[1] > 0.50 and features[10] > 1.50 and features[12] > 6.50 and features[8] > 0.50 and features[4] > 198.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] <= 3.50 and features[11] <= 0.50 and features[2] <= 1.50 and features[7] <= 145.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] <= 3.50 and features[11] <= 0.50 and features[2] <= 1.50 and features[7] > 145.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[2] <= 3.50 and features[11] <= 0.50 and features[2] > 1.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[2] <= 3.50 and features[11] <= 0.50 and features[2] > 1.50 and features[1] > 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[2] <= 3.50 and features[11] > 0.50 and features[0] <= 54.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[2] <= 3.50 and features[11] > 0.50 and features[0] <= 54.50 and features[8] > 0.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] <= 3.50 and features[11] > 0.50 and features[0] > 54.50 and features[2] <= 2.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] <= 3.50 and features[11] > 0.50 and features[0] > 54.50 and features[2] > 2.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] > 3.50 and features[8] <= 0.50 and features[0] <= 53.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] > 3.50 and features[8] <= 0.50 and features[0] <= 53.50 and features[7] > 147.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[2] > 3.50 and features[8] <= 0.50 and features[0] > 53.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] > 3.50 and features[8] <= 0.50 and features[0] > 53.50 and features[7] > 160.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] > 3.50 and features[8] > 0.50 and features[11] <= 0.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] > 3.50 and features[8] > 0.50 and features[11] <= 0.50 and features[0] > 53.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] > 3.50 and features[8] > 0.50 and features[11] > 0.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[2] > 3.50 and features[8] > 0.50 and features[11] > 0.50 and features[7] > 160.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[9] <= 0.95 and features[1] <= 0.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[9] <= 0.95 and features[1] <= 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[9] <= 0.95 and features[1] > 0.50 and features[2] <= 3.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[9] <= 0.95 and features[1] > 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[9] > 0.95 and features[1] <= 0.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[9] > 0.95 and features[1] <= 0.50 and features[11] > 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[9] > 0.95 and features[1] > 0.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[9] > 0.95 and features[1] > 0.50 and features[7] > 160.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[11] <= 0.50 and features[2] <= 3.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[11] <= 0.50 and features[2] <= 3.50 and features[1] > 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[11] <= 0.50 and features[2] > 3.50 and features[7] <= 179.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[11] <= 0.50 and features[2] > 3.50 and features[7] > 179.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[11] > 0.50 and features[2] <= 3.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[11] > 0.50 and features[2] <= 3.50 and features[7] > 160.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[11] > 0.50 and features[2] > 3.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[11] > 0.50 and features[2] > 3.50 and features[1] > 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] <= 1.50 and features[2] <= 3.50 and features[7] <= 140.50 and features[2] <= 1.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] <= 1.50 and features[2] <= 3.50 and features[7] <= 140.50 and features[2] > 1.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] <= 1.50 and features[2] <= 3.50 and features[7] > 140.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[7] <= 160.50 and features[10] <= 1.50 and features[2] <= 3.50 and features[7] > 140.50 and features[11] > 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] <= 1.50 and features[2] > 3.50 and features[7] <= 147.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] <= 1.50 and features[2] > 3.50 and features[7] <= 147.50 and features[8] > 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] <= 1.50 and features[2] > 3.50 and features[7] > 147.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] <= 1.50 and features[2] > 3.50 and features[7] > 147.50 and features[8] > 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] > 1.50 and features[9] <= 0.95 and features[1] <= 0.50 and features[4] <= 235.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] > 1.50 and features[9] <= 0.95 and features[1] <= 0.50 and features[4] > 235.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] > 1.50 and features[9] <= 0.95 and features[1] > 0.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] > 1.50 and features[9] <= 0.95 and features[1] > 0.50 and features[8] > 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] > 1.50 and features[9] > 0.95 and features[6] <= 0.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] > 1.50 and features[9] > 0.95 and features[6] <= 0.50 and features[8] > 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] > 1.50 and features[9] > 0.95 and features[6] > 0.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[10] > 1.50 and features[9] > 0.95 and features[6] > 0.50 and features[1] > 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[0] <= 53.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[0] <= 53.50 and features[11] > 0.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[0] > 53.50 and features[9] <= 1.05:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[0] > 53.50 and features[9] > 1.05:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[1] <= 0.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[1] <= 0.50 and features[10] > 1.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[1] > 0.50 and features[6] <= 1.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[1] > 0.50 and features[6] > 1.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[11] <= 0.50 and features[3] <= 147.00 and features[8] <= 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[11] <= 0.50 and features[3] <= 147.00 and features[8] > 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[11] <= 0.50 and features[3] > 147.00 and features[0] <= 48.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[11] <= 0.50 and features[3] > 147.00 and features[0] > 48.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[11] > 0.50 and features[8] <= 0.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[11] > 0.50 and features[8] <= 0.50 and features[6] > 1.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[11] > 0.50 and features[8] > 0.50 and features[9] <= 0.55:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[11] > 0.50 and features[8] > 0.50 and features[9] > 0.55:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] <= 0.50 and features[2] <= 3.50 and features[11] <= 0.50 and features[7] <= 147.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[8] <= 0.50 and features[2] <= 3.50 and features[11] <= 0.50 and features[7] > 147.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[8] <= 0.50 and features[2] <= 3.50 and features[11] > 0.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[8] <= 0.50 and features[2] <= 3.50 and features[11] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] <= 0.50 and features[2] > 3.50 and features[11] <= 0.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] <= 0.50 and features[2] > 3.50 and features[11] <= 0.50 and features[12] > 6.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] <= 0.50 and features[2] > 3.50 and features[11] > 0.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] <= 0.50 and features[2] > 3.50 and features[11] > 0.50 and features[7] > 160.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] > 0.50 and features[7] <= 160.50 and features[10] <= 1.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] > 0.50 and features[7] <= 160.50 and features[10] <= 1.50 and features[0] > 53.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] > 0.50 and features[7] <= 160.50 and features[10] > 1.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] > 0.50 and features[7] <= 160.50 and features[10] > 1.50 and features[7] > 147.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] > 0.50 and features[7] > 160.50 and features[0] <= 49.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[8] > 0.50 and features[7] > 160.50 and features[0] <= 49.50 and features[2] > 3.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] > 0.50 and features[7] > 160.50 and features[0] > 49.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[8] > 0.50 and features[7] > 160.50 and features[0] > 49.50 and features[6] > 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[1] <= 0.50 and features[11] <= 0.50 and features[7] <= 146.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[1] <= 0.50 and features[11] <= 0.50 and features[7] > 146.50:
        votes_0 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[1] <= 0.50 and features[11] > 0.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[1] <= 0.50 and features[11] > 0.50 and features[7] > 160.50:
        votes_0 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[1] > 0.50 and features[10] <= 1.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[1] > 0.50 and features[10] <= 1.50 and features[11] > 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[1] > 0.50 and features[10] > 1.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[1] > 0.50 and features[10] > 1.50 and features[6] > 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[1] <= 0.50 and features[8] <= 0.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[1] <= 0.50 and features[8] <= 0.50 and features[0] > 53.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[1] <= 0.50 and features[8] > 0.50 and features[6] <= 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[1] <= 0.50 and features[8] > 0.50 and features[6] > 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[1] > 0.50 and features[10] <= 1.50 and features[7] <= 161.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[1] > 0.50 and features[10] <= 1.50 and features[7] > 161.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[1] > 0.50 and features[10] > 1.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[1] > 0.50 and features[10] > 1.50 and features[7] > 160.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[1] <= 0.50 and features[6] <= 0.50 and features[9] <= 1.25:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[1] <= 0.50 and features[6] <= 0.50 and features[9] > 1.25:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[1] <= 0.50 and features[6] > 0.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[1] <= 0.50 and features[6] > 0.50 and features[7] > 147.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[1] > 0.50 and features[2] <= 3.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[1] > 0.50 and features[2] <= 3.50 and features[8] > 0.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[1] > 0.50 and features[2] > 3.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] <= 0.50 and features[1] > 0.50 and features[2] > 3.50 and features[6] > 1.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[4] <= 241.00 and features[8] <= 0.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[4] <= 241.00 and features[8] <= 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[4] <= 241.00 and features[8] > 0.50 and features[2] <= 3.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[4] <= 241.00 and features[8] > 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[4] > 241.00 and features[2] <= 3.50 and features[4] <= 296.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[4] > 241.00 and features[2] <= 3.50 and features[4] > 296.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[4] > 241.00 and features[2] > 3.50 and features[6] <= 0.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[11] > 0.50 and features[4] > 241.00 and features[2] > 3.50 and features[6] > 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] <= 0.50 and features[6] <= 0.50 and features[7] <= 160.50 and features[2] <= 3.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] <= 0.50 and features[6] <= 0.50 and features[7] <= 160.50 and features[2] > 3.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] <= 0.50 and features[6] <= 0.50 and features[7] > 160.50 and features[9] <= 0.85:
        votes_0 += 1
    if features[10] > 1.50 and features[11] <= 0.50 and features[6] <= 0.50 and features[7] > 160.50 and features[9] > 0.85:
        votes_1 += 1
    if features[10] > 1.50 and features[11] <= 0.50 and features[6] > 0.50 and features[8] <= 0.50 and features[2] <= 3.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] <= 0.50 and features[6] > 0.50 and features[8] <= 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] <= 0.50 and features[6] > 0.50 and features[8] > 0.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] <= 0.50 and features[6] > 0.50 and features[8] > 0.50 and features[7] > 160.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] > 0.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[7] <= 170.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] > 0.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[7] > 170.50:
        votes_0 += 1
    if features[10] > 1.50 and features[11] > 0.50 and features[2] <= 3.50 and features[1] > 0.50 and features[9] <= 0.15:
        votes_1 += 1
    if features[10] > 1.50 and features[11] > 0.50 and features[2] <= 3.50 and features[1] > 0.50 and features[9] > 0.15:
        votes_1 += 1
    if features[10] > 1.50 and features[11] > 0.50 and features[2] > 3.50 and features[1] <= 0.50 and features[10] <= 2.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] > 0.50 and features[2] > 3.50 and features[1] <= 0.50 and features[10] > 2.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] > 0.50 and features[2] > 3.50 and features[1] > 0.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[11] > 0.50 and features[2] > 3.50 and features[1] > 0.50 and features[8] > 0.50:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[9] <= 0.65 and features[11] <= 0.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[9] <= 0.65 and features[11] > 0.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[9] > 0.65 and features[9] <= 1.95:
        votes_0 += 1
    if features[0] <= 53.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[9] > 0.65 and features[9] > 1.95:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] <= 3.50 and features[10] > 1.50 and features[1] <= 0.50 and features[2] <= 2.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[2] <= 3.50 and features[10] > 1.50 and features[1] <= 0.50 and features[2] > 2.50:
        votes_0 += 1
    if features[0] <= 53.50 and features[2] <= 3.50 and features[10] > 1.50 and features[1] > 0.50 and features[4] <= 235.50:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] <= 3.50 and features[10] > 1.50 and features[1] > 0.50 and features[4] > 235.50:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] > 3.50 and features[10] <= 1.50 and features[7] <= 147.50 and features[9] <= 0.62:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] > 3.50 and features[10] <= 1.50 and features[7] <= 147.50 and features[9] > 0.62:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] > 3.50 and features[10] <= 1.50 and features[7] > 147.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] > 3.50 and features[10] <= 1.50 and features[7] > 147.50 and features[11] > 0.50:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] > 3.50 and features[10] > 1.50 and features[11] <= 0.50 and features[4] <= 241.50:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] > 3.50 and features[10] > 1.50 and features[11] <= 0.50 and features[4] > 241.50:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] > 3.50 and features[10] > 1.50 and features[11] > 0.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[0] <= 53.50 and features[2] > 3.50 and features[10] > 1.50 and features[11] > 0.50 and features[8] > 0.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[12] <= 6.50 and features[2] <= 3.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[12] <= 6.50 and features[2] <= 3.50 and features[11] > 0.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[12] <= 6.50 and features[2] > 3.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[12] <= 6.50 and features[2] > 3.50 and features[10] > 1.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[12] > 6.50 and features[2] <= 3.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[12] > 6.50 and features[2] <= 3.50 and features[7] > 147.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[12] > 6.50 and features[2] > 3.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] <= 0.95 and features[12] > 6.50 and features[2] > 3.50 and features[10] > 1.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[10] <= 1.50 and features[8] <= 0.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[10] <= 1.50 and features[8] <= 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[10] <= 1.50 and features[8] > 0.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[10] <= 1.50 and features[8] > 0.50 and features[11] > 0.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[10] > 1.50 and features[8] <= 0.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[10] > 1.50 and features[8] <= 0.50 and features[12] > 6.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[10] > 1.50 and features[8] > 0.50 and features[6] <= 0.50:
        votes_1 += 1
    if features[0] > 53.50 and features[9] > 0.95 and features[10] > 1.50 and features[8] > 0.50 and features[6] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[6] <= 0.50 and features[10] <= 1.50 and features[7] <= 129.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[6] <= 0.50 and features[10] <= 1.50 and features[7] > 129.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[6] <= 0.50 and features[10] > 1.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[6] <= 0.50 and features[10] > 1.50 and features[1] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[6] > 0.50 and features[4] <= 244.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[6] > 0.50 and features[4] <= 244.50 and features[11] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[6] > 0.50 and features[4] > 244.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] <= 147.50 and features[6] > 0.50 and features[4] > 244.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[10] <= 1.50 and features[11] <= 0.50 and features[7] <= 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[10] <= 1.50 and features[11] <= 0.50 and features[7] > 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[10] <= 1.50 and features[11] > 0.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[10] <= 1.50 and features[11] > 0.50 and features[1] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[10] > 1.50 and features[11] <= 0.50 and features[9] <= 0.95:
        votes_0 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[10] > 1.50 and features[11] <= 0.50 and features[9] > 0.95:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[10] > 1.50 and features[11] > 0.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[7] > 147.50 and features[10] > 1.50 and features[11] > 0.50 and features[6] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] <= 0.50 and features[1] <= 0.50 and features[0] <= 53.50 and features[12] <= 6.50:
        votes_0 += 1
    if features[2] > 3.50 and features[11] <= 0.50 and features[1] <= 0.50 and features[0] <= 53.50 and features[12] > 6.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] <= 0.50 and features[1] <= 0.50 and features[0] > 53.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] <= 0.50 and features[1] <= 0.50 and features[0] > 53.50 and features[7] > 160.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] <= 0.50 and features[1] > 0.50 and features[9] <= 0.95 and features[6] <= 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] <= 0.50 and features[1] > 0.50 and features[9] <= 0.95 and features[6] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] <= 0.50 and features[1] > 0.50 and features[9] > 0.95 and features[9] <= 1.95:
        votes_1 += 1
    if features[2] > 3.50 and features[11] <= 0.50 and features[1] > 0.50 and features[9] > 0.95 and features[9] > 1.95:
        votes_1 += 1
    if features[2] > 3.50 and features[11] > 0.50 and features[4] <= 239.50 and features[7] <= 160.50 and features[7] <= 137.00:
        votes_1 += 1
    if features[2] > 3.50 and features[11] > 0.50 and features[4] <= 239.50 and features[7] <= 160.50 and features[7] > 137.00:
        votes_1 += 1
    if features[2] > 3.50 and features[11] > 0.50 and features[4] <= 239.50 and features[7] > 160.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] > 0.50 and features[4] <= 239.50 and features[7] > 160.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] > 0.50 and features[4] > 239.50 and features[10] <= 1.50 and features[7] <= 165.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] > 0.50 and features[4] > 239.50 and features[10] <= 1.50 and features[7] > 165.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] > 0.50 and features[4] > 239.50 and features[10] > 1.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[11] > 0.50 and features[4] > 239.50 and features[10] > 1.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 53.50 and features[8] <= 0.50 and features[1] <= 0.50 and features[7] <= 146.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 53.50 and features[8] <= 0.50 and features[1] <= 0.50 and features[7] > 146.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 53.50 and features[8] <= 0.50 and features[1] > 0.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 53.50 and features[8] <= 0.50 and features[1] > 0.50 and features[11] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 53.50 and features[8] > 0.50 and features[10] <= 1.50 and features[7] <= 146.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 53.50 and features[8] > 0.50 and features[10] <= 1.50 and features[7] > 146.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 53.50 and features[8] > 0.50 and features[10] > 1.50 and features[2] <= 1.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 53.50 and features[8] > 0.50 and features[10] > 1.50 and features[2] > 1.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 53.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[1] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] > 53.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[1] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 53.50 and features[7] <= 160.50 and features[9] > 0.95 and features[11] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 53.50 and features[7] <= 160.50 and features[9] > 0.95 and features[11] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 53.50 and features[7] > 160.50 and features[10] <= 1.50 and features[7] <= 179.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] > 53.50 and features[7] > 160.50 and features[10] <= 1.50 and features[7] > 179.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] > 53.50 and features[7] > 160.50 and features[10] > 1.50 and features[12] <= 6.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] > 53.50 and features[7] > 160.50 and features[10] > 1.50 and features[12] > 6.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[0] <= 53.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[0] <= 53.50 and features[11] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[0] > 53.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[0] > 53.50 and features[7] > 147.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[9] > 0.95 and features[1] <= 0.50 and features[3] <= 179.00:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[9] > 0.95 and features[1] <= 0.50 and features[3] > 179.00:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[9] > 0.95 and features[1] > 0.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[9] > 0.95 and features[1] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[11] <= 0.50 and features[0] <= 53.50 and features[9] <= 0.95:
        votes_0 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[11] <= 0.50 and features[0] <= 53.50 and features[9] > 0.95:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[11] <= 0.50 and features[0] > 53.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[11] <= 0.50 and features[0] > 53.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[11] > 0.50 and features[8] <= 0.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[11] > 0.50 and features[8] <= 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[11] > 0.50 and features[8] > 0.50 and features[9] <= 1.05:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[11] > 0.50 and features[8] > 0.50 and features[9] > 1.05:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[6] <= 1.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] <= 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[6] > 1.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] <= 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[1] > 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 160.50 and features[2] > 3.50 and features[0] <= 53.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 160.50 and features[2] > 3.50 and features[0] <= 53.50 and features[8] > 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 160.50 and features[2] > 3.50 and features[0] > 53.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 160.50 and features[2] > 3.50 and features[0] > 53.50 and features[10] > 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 160.50 and features[8] <= 0.50 and features[11] <= 0.50 and features[7] <= 179.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 160.50 and features[8] <= 0.50 and features[11] <= 0.50 and features[7] > 179.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 160.50 and features[8] <= 0.50 and features[11] > 0.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 160.50 and features[8] <= 0.50 and features[11] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 160.50 and features[8] > 0.50 and features[10] <= 1.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 160.50 and features[8] > 0.50 and features[10] <= 1.50 and features[11] > 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 160.50 and features[8] > 0.50 and features[10] > 1.50 and features[2] <= 3.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 160.50 and features[8] > 0.50 and features[10] > 1.50 and features[2] > 3.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] <= 0.50 and features[2] <= 3.50 and features[7] <= 158.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] <= 0.50 and features[2] <= 3.50 and features[7] <= 158.50 and features[1] > 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] <= 0.50 and features[2] <= 3.50 and features[7] > 158.50 and features[11] <= 0.50:
        votes_0 += 1
    if features[9] > 0.95 and features[8] <= 0.50 and features[2] <= 3.50 and features[7] > 158.50 and features[11] > 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] <= 0.50 and features[2] > 3.50 and features[1] <= 0.50 and features[7] <= 148.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] <= 0.50 and features[2] > 3.50 and features[1] <= 0.50 and features[7] > 148.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] <= 0.50 and features[2] > 3.50 and features[1] > 0.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] <= 0.50 and features[2] > 3.50 and features[1] > 0.50 and features[12] > 6.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] > 0.50 and features[11] <= 0.50 and features[2] <= 3.50 and features[9] <= 1.95:
        votes_1 += 1
    if features[9] > 0.95 and features[8] > 0.50 and features[11] <= 0.50 and features[2] <= 3.50 and features[9] > 1.95:
        votes_1 += 1
    if features[9] > 0.95 and features[8] > 0.50 and features[11] <= 0.50 and features[2] > 3.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] > 0.50 and features[11] <= 0.50 and features[2] > 3.50 and features[7] > 160.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] > 0.50 and features[11] > 0.50 and features[2] <= 3.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] > 0.50 and features[11] > 0.50 and features[2] <= 3.50 and features[7] > 160.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] > 0.50 and features[11] > 0.50 and features[2] > 3.50 and features[0] <= 46.50:
        votes_1 += 1
    if features[9] > 0.95 and features[8] > 0.50 and features[11] > 0.50 and features[2] > 3.50 and features[0] > 46.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] <= 147.50 and features[9] <= 0.35:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] <= 147.50 and features[9] > 0.35:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] > 147.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[2] <= 3.50 and features[8] <= 0.50 and features[7] > 147.50 and features[10] > 1.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[2] <= 3.50 and features[8] > 0.50 and features[7] <= 147.50 and features[11] <= 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] <= 3.50 and features[8] > 0.50 and features[7] <= 147.50 and features[11] > 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] <= 3.50 and features[8] > 0.50 and features[7] > 147.50 and features[0] <= 56.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[2] <= 3.50 and features[8] > 0.50 and features[7] > 147.50 and features[0] > 56.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] > 3.50 and features[11] <= 0.50 and features[3] <= 171.00 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] > 3.50 and features[11] <= 0.50 and features[3] <= 171.00 and features[8] > 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] > 3.50 and features[11] <= 0.50 and features[3] > 171.00 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] > 3.50 and features[11] <= 0.50 and features[3] > 171.00 and features[8] > 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] > 3.50 and features[11] > 0.50 and features[7] <= 160.50 and features[7] <= 146.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] > 3.50 and features[11] > 0.50 and features[7] <= 160.50 and features[7] > 146.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] > 3.50 and features[11] > 0.50 and features[7] > 160.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[2] > 3.50 and features[11] > 0.50 and features[7] > 160.50 and features[8] > 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[6] <= 1.50 and features[8] <= 0.50 and features[7] <= 156.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[6] <= 1.50 and features[8] <= 0.50 and features[7] > 156.50:
        votes_0 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[6] <= 1.50 and features[8] > 0.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[6] <= 1.50 and features[8] > 0.50 and features[7] > 160.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[6] > 1.50 and features[8] <= 0.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[6] > 1.50 and features[8] <= 0.50 and features[0] > 53.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[6] > 1.50 and features[8] > 0.50 and features[5] <= 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] <= 3.50 and features[6] > 1.50 and features[8] > 0.50 and features[5] > 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[7] <= 160.50 and features[11] <= 0.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[7] <= 160.50 and features[11] <= 0.50 and features[7] > 147.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[7] <= 160.50 and features[11] > 0.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[7] <= 160.50 and features[11] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[7] > 160.50 and features[10] <= 1.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[7] > 160.50 and features[10] <= 1.50 and features[6] > 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[7] > 160.50 and features[10] > 1.50 and features[9] <= 1.95:
        votes_1 += 1
    if features[9] > 0.95 and features[2] > 3.50 and features[7] > 160.50 and features[10] > 1.50 and features[9] > 1.95:
        votes_1 += 1
    total = votes_0 + votes_1
    if total == 0:
        return 0.7654
    return votes_1 / total


def predict_zone_2(features):
    """Predict for zone 2. 319 rules, majority vote."""
    votes_0, votes_1 = 0, 0
    if features[9] <= 0.95 and features[7] <= 147.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[0] <= 53.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] <= 147.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[0] > 53.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 147.50 and features[2] <= 3.50 and features[10] > 1.50 and features[4] <= 209.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] <= 147.50 and features[2] <= 3.50 and features[10] > 1.50 and features[4] > 209.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 147.50 and features[2] > 3.50 and features[8] <= 0.50 and features[0] <= 44.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 147.50 and features[2] > 3.50 and features[8] <= 0.50 and features[0] > 44.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 147.50 and features[2] > 3.50 and features[8] > 0.50 and features[7] <= 119.00:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 147.50 and features[2] > 3.50 and features[8] > 0.50 and features[7] > 119.00:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 147.50 and features[0] <= 53.50 and features[2] <= 3.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 147.50 and features[0] <= 53.50 and features[2] <= 3.50 and features[8] > 0.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 147.50 and features[0] <= 53.50 and features[2] > 3.50 and features[6] <= 1.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 147.50 and features[0] <= 53.50 and features[2] > 3.50 and features[6] > 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 147.50 and features[0] > 53.50 and features[2] <= 3.50 and features[7] <= 170.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 147.50 and features[0] > 53.50 and features[2] <= 3.50 and features[7] > 170.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 147.50 and features[0] > 53.50 and features[2] > 3.50 and features[7] <= 174.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 147.50 and features[0] > 53.50 and features[2] > 3.50 and features[7] > 174.50:
        votes_0 += 1
    if features[9] > 0.95 and features[9] <= 1.95 and features[1] <= 0.50 and features[11] <= 2.50 and features[3] <= 103.50:
        votes_0 += 1
    if features[9] > 0.95 and features[9] <= 1.95 and features[1] <= 0.50 and features[11] <= 2.50 and features[3] > 103.50:
        votes_1 += 1
    if features[9] > 0.95 and features[9] <= 1.95 and features[1] <= 0.50 and features[11] > 2.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[9] > 0.95 and features[9] <= 1.95 and features[1] <= 0.50 and features[11] > 2.50 and features[2] > 3.50:
        votes_1 += 1
    if features[9] > 0.95 and features[9] <= 1.95 and features[1] > 0.50 and features[2] <= 3.50 and features[7] <= 161.50:
        votes_1 += 1
    if features[9] > 0.95 and features[9] <= 1.95 and features[1] > 0.50 and features[2] <= 3.50 and features[7] > 161.50:
        votes_0 += 1
    if features[9] > 0.95 and features[9] <= 1.95 and features[1] > 0.50 and features[2] > 3.50 and features[3] <= 139.00:
        votes_1 += 1
    if features[9] > 0.95 and features[9] <= 1.95 and features[1] > 0.50 and features[2] > 3.50 and features[3] > 139.00:
        votes_1 += 1
    if features[9] > 0.95 and features[9] > 1.95 and features[7] <= 161.50 and features[2] <= 3.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[9] > 1.95 and features[7] <= 161.50 and features[2] <= 3.50 and features[10] > 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[9] > 1.95 and features[7] <= 161.50 and features[2] > 3.50 and features[0] <= 41.50:
        votes_1 += 1
    if features[9] > 0.95 and features[9] > 1.95 and features[7] <= 161.50 and features[2] > 3.50 and features[0] > 41.50:
        votes_1 += 1
    if features[9] > 0.95 and features[9] > 1.95 and features[7] > 161.50 and features[6] <= 1.00 and features[2] <= 3.50:
        votes_0 += 1
    if features[9] > 0.95 and features[9] > 1.95 and features[7] > 161.50 and features[6] <= 1.00 and features[2] > 3.50:
        votes_1 += 1
    if features[9] > 0.95 and features[9] > 1.95 and features[7] > 161.50 and features[6] > 1.00 and features[1] <= 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[9] > 1.95 and features[7] > 161.50 and features[6] > 1.00 and features[1] > 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 146.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] <= 146.50 and features[2] <= 3.50 and features[10] <= 1.50 and features[8] > 0.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 146.50 and features[2] <= 3.50 and features[10] > 1.50 and features[6] <= 1.00:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 146.50 and features[2] <= 3.50 and features[10] > 1.50 and features[6] > 1.00:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 146.50 and features[2] > 3.50 and features[8] <= 0.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 146.50 and features[2] > 3.50 and features[8] <= 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 146.50 and features[2] > 3.50 and features[8] > 0.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] <= 146.50 and features[2] > 3.50 and features[8] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 146.50 and features[1] <= 0.50 and features[7] <= 162.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 146.50 and features[1] <= 0.50 and features[7] <= 162.50 and features[8] > 0.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 146.50 and features[1] <= 0.50 and features[7] > 162.50 and features[3] <= 127.00:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 146.50 and features[1] <= 0.50 and features[7] > 162.50 and features[3] > 127.00:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 146.50 and features[1] > 0.50 and features[8] <= 0.50 and features[7] <= 161.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 146.50 and features[1] > 0.50 and features[8] <= 0.50 and features[7] > 161.50:
        votes_0 += 1
    if features[9] <= 0.95 and features[7] > 146.50 and features[1] > 0.50 and features[8] > 0.50 and features[7] <= 178.50:
        votes_1 += 1
    if features[9] <= 0.95 and features[7] > 146.50 and features[1] > 0.50 and features[8] > 0.50 and features[7] > 178.50:
        votes_0 += 1
    if features[9] > 0.95 and features[4] <= 230.50 and features[8] <= 0.50 and features[7] <= 144.50 and features[2] <= 3.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] <= 230.50 and features[8] <= 0.50 and features[7] <= 144.50 and features[2] > 3.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] <= 230.50 and features[8] <= 0.50 and features[7] > 144.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[9] > 0.95 and features[4] <= 230.50 and features[8] <= 0.50 and features[7] > 144.50 and features[1] > 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] <= 230.50 and features[8] > 0.50 and features[7] <= 162.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] <= 230.50 and features[8] > 0.50 and features[7] <= 162.50 and features[10] > 1.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] <= 230.50 and features[8] > 0.50 and features[7] > 162.50 and features[6] <= 1.00:
        votes_1 += 1
    if features[9] > 0.95 and features[4] <= 230.50 and features[8] > 0.50 and features[7] > 162.50 and features[6] > 1.00:
        votes_1 += 1
    if features[9] > 0.95 and features[4] > 230.50 and features[6] <= 1.50 and features[9] <= 2.45 and features[2] <= 3.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] > 230.50 and features[6] <= 1.50 and features[9] <= 2.45 and features[2] > 3.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] > 230.50 and features[6] <= 1.50 and features[9] > 2.45 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] > 230.50 and features[6] <= 1.50 and features[9] > 2.45 and features[8] > 0.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] > 230.50 and features[6] > 1.50 and features[0] <= 41.50 and features[7] <= 168.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] > 230.50 and features[6] > 1.50 and features[0] <= 41.50 and features[7] > 168.50:
        votes_0 += 1
    if features[9] > 0.95 and features[4] > 230.50 and features[6] > 1.50 and features[0] > 41.50 and features[2] <= 3.50:
        votes_1 += 1
    if features[9] > 0.95 and features[4] > 230.50 and features[6] > 1.50 and features[0] > 41.50 and features[2] > 3.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[1] <= 0.50 and features[10] <= 1.50 and features[4] <= 284.50 and features[4] <= 249.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[1] <= 0.50 and features[10] <= 1.50 and features[4] <= 284.50 and features[4] > 249.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[1] <= 0.50 and features[10] <= 1.50 and features[4] > 284.50 and features[9] <= 1.70:
        votes_0 += 1
    if features[2] <= 3.50 and features[1] <= 0.50 and features[10] <= 1.50 and features[4] > 284.50 and features[9] > 1.70:
        votes_1 += 1
    if features[2] <= 3.50 and features[1] <= 0.50 and features[10] > 1.50 and features[8] <= 0.50 and features[0] <= 65.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[1] <= 0.50 and features[10] > 1.50 and features[8] <= 0.50 and features[0] > 65.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[1] <= 0.50 and features[10] > 1.50 and features[8] > 0.50 and features[11] <= 2.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[1] <= 0.50 and features[10] > 1.50 and features[8] > 0.50 and features[11] > 2.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[1] > 0.50 and features[9] <= 0.85 and features[8] <= 0.50 and features[7] <= 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[1] > 0.50 and features[9] <= 0.85 and features[8] <= 0.50 and features[7] > 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[1] > 0.50 and features[9] <= 0.85 and features[8] > 0.50 and features[4] <= 311.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[1] > 0.50 and features[9] <= 0.85 and features[8] > 0.50 and features[4] > 311.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[1] > 0.50 and features[9] > 0.85 and features[8] <= 0.50 and features[9] <= 1.95:
        votes_0 += 1
    if features[2] <= 3.50 and features[1] > 0.50 and features[9] > 0.85 and features[8] <= 0.50 and features[9] > 1.95:
        votes_1 += 1
    if features[2] <= 3.50 and features[1] > 0.50 and features[9] > 0.85 and features[8] > 0.50 and features[0] <= 64.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[1] > 0.50 and features[9] > 0.85 and features[8] > 0.50 and features[0] > 64.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[0] <= 54.50 and features[6] <= 1.50 and features[7] <= 147.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[0] <= 54.50 and features[6] <= 1.50 and features[7] > 147.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[0] <= 54.50 and features[6] > 1.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[0] <= 54.50 and features[6] > 1.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[0] > 54.50 and features[6] <= 0.50 and features[7] <= 150.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[0] > 54.50 and features[6] <= 0.50 and features[7] > 150.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[0] > 54.50 and features[6] > 0.50 and features[3] <= 106.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.95 and features[0] > 54.50 and features[6] > 0.50 and features[3] > 106.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[1] <= 0.50 and features[5] <= 0.50 and features[9] <= 4.90:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[1] <= 0.50 and features[5] <= 0.50 and features[9] > 4.90:
        votes_0 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[1] <= 0.50 and features[5] > 0.50 and features[0] <= 51.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[1] <= 0.50 and features[5] > 0.50 and features[0] > 51.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[1] > 0.50 and features[0] <= 51.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[1] > 0.50 and features[0] <= 51.50 and features[10] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[1] > 0.50 and features[0] > 51.50 and features[7] <= 179.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.95 and features[1] > 0.50 and features[0] > 51.50 and features[7] > 179.50:
        votes_0 += 1
    if features[4] <= 243.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[10] <= 1.50 and features[9] <= 1.95:
        votes_0 += 1
    if features[4] <= 243.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[10] <= 1.50 and features[9] > 1.95:
        votes_0 += 1
    if features[4] <= 243.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[10] > 1.50 and features[6] <= 1.00:
        votes_0 += 1
    if features[4] <= 243.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[10] > 1.50 and features[6] > 1.00:
        votes_0 += 1
    if features[4] <= 243.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] <= 55.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[4] <= 243.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] <= 55.50 and features[8] > 0.50:
        votes_1 += 1
    if features[4] <= 243.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] > 55.50 and features[9] <= 0.95:
        votes_0 += 1
    if features[4] <= 243.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] > 55.50 and features[9] > 0.95:
        votes_1 += 1
    if features[4] <= 243.50 and features[2] > 3.50 and features[7] <= 160.50 and features[1] <= 0.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[4] <= 243.50 and features[2] > 3.50 and features[7] <= 160.50 and features[1] <= 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[4] <= 243.50 and features[2] > 3.50 and features[7] <= 160.50 and features[1] > 0.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[4] <= 243.50 and features[2] > 3.50 and features[7] <= 160.50 and features[1] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[4] <= 243.50 and features[2] > 3.50 and features[7] > 160.50 and features[8] <= 0.50 and features[9] <= 0.85:
        votes_0 += 1
    if features[4] <= 243.50 and features[2] > 3.50 and features[7] > 160.50 and features[8] <= 0.50 and features[9] > 0.85:
        votes_1 += 1
    if features[4] <= 243.50 and features[2] > 3.50 and features[7] > 160.50 and features[8] > 0.50 and features[0] <= 56.50:
        votes_1 += 1
    if features[4] <= 243.50 and features[2] > 3.50 and features[7] > 160.50 and features[8] > 0.50 and features[0] > 56.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] <= 54.50 and features[6] <= 1.50 and features[4] <= 299.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[4] > 243.50 and features[0] <= 54.50 and features[6] <= 1.50 and features[4] <= 299.50 and features[2] > 3.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] <= 54.50 and features[6] <= 1.50 and features[4] > 299.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[4] > 243.50 and features[0] <= 54.50 and features[6] <= 1.50 and features[4] > 299.50 and features[1] > 0.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] <= 54.50 and features[6] > 1.50 and features[7] <= 161.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] <= 54.50 and features[6] > 1.50 and features[7] <= 161.50 and features[10] > 1.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] <= 54.50 and features[6] > 1.50 and features[7] > 161.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[4] > 243.50 and features[0] <= 54.50 and features[6] > 1.50 and features[7] > 161.50 and features[2] > 3.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] > 54.50 and features[10] <= 1.50 and features[7] <= 145.50 and features[4] <= 320.00:
        votes_1 += 1
    if features[4] > 243.50 and features[0] > 54.50 and features[10] <= 1.50 and features[7] <= 145.50 and features[4] > 320.00:
        votes_0 += 1
    if features[4] > 243.50 and features[0] > 54.50 and features[10] <= 1.50 and features[7] > 145.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[4] > 243.50 and features[0] > 54.50 and features[10] <= 1.50 and features[7] > 145.50 and features[2] > 3.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] > 54.50 and features[10] > 1.50 and features[8] <= 0.50 and features[7] <= 158.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] > 54.50 and features[10] > 1.50 and features[8] <= 0.50 and features[7] > 158.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] > 54.50 and features[10] > 1.50 and features[8] > 0.50 and features[0] <= 61.50:
        votes_1 += 1
    if features[4] > 243.50 and features[0] > 54.50 and features[10] > 1.50 and features[8] > 0.50 and features[0] > 61.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] <= 147.50 and features[1] <= 0.50 and features[6] <= 1.00 and features[9] <= 0.95:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] <= 147.50 and features[1] <= 0.50 and features[6] <= 1.00 and features[9] > 0.95:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] <= 147.50 and features[1] <= 0.50 and features[6] > 1.00 and features[9] <= 1.10:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] <= 147.50 and features[1] <= 0.50 and features[6] > 1.00 and features[9] > 1.10:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] <= 147.50 and features[1] > 0.50 and features[2] <= 3.50 and features[7] <= 129.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] <= 147.50 and features[1] > 0.50 and features[2] <= 3.50 and features[7] > 129.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] <= 147.50 and features[1] > 0.50 and features[2] > 3.50 and features[4] <= 327.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] <= 147.50 and features[1] > 0.50 and features[2] > 3.50 and features[4] > 327.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] > 147.50 and features[2] <= 3.50 and features[9] <= 1.95 and features[3] <= 196.00:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] > 147.50 and features[2] <= 3.50 and features[9] <= 1.95 and features[3] > 196.00:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] > 147.50 and features[2] <= 3.50 and features[9] > 1.95 and features[3] <= 132.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] > 147.50 and features[2] <= 3.50 and features[9] > 1.95 and features[3] > 132.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] > 147.50 and features[2] > 3.50 and features[8] <= 0.50 and features[9] <= 0.95:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] > 147.50 and features[2] > 3.50 and features[8] <= 0.50 and features[9] > 0.95:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] > 147.50 and features[2] > 3.50 and features[8] > 0.50 and features[7] <= 181.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] > 147.50 and features[2] > 3.50 and features[8] > 0.50 and features[7] > 181.50:
        votes_0 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[7] <= 146.50 and features[7] <= 137.00 and features[2] <= 2.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[7] <= 146.50 and features[7] <= 137.00 and features[2] > 2.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[7] <= 146.50 and features[7] > 137.00 and features[0] <= 52.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[7] <= 146.50 and features[7] > 137.00 and features[0] > 52.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[7] > 146.50 and features[8] <= 0.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[7] > 146.50 and features[8] <= 0.50 and features[1] > 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[7] > 146.50 and features[8] > 0.50 and features[2] <= 1.50:
        votes_0 += 1
    if features[10] > 1.50 and features[2] <= 3.50 and features[7] > 146.50 and features[8] > 0.50 and features[2] > 1.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[7] <= 161.50 and features[7] <= 146.50 and features[3] <= 179.00:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[7] <= 161.50 and features[7] <= 146.50 and features[3] > 179.00:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[7] <= 161.50 and features[7] > 146.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[7] <= 161.50 and features[7] > 146.50 and features[6] > 1.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[7] > 161.50 and features[1] <= 0.50 and features[11] <= 2.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[7] > 161.50 and features[1] <= 0.50 and features[11] > 2.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[7] > 161.50 and features[1] > 0.50 and features[0] <= 54.50:
        votes_1 += 1
    if features[10] > 1.50 and features[2] > 3.50 and features[7] > 161.50 and features[1] > 0.50 and features[0] > 54.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] <= 146.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[4] <= 252.00:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] <= 146.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[4] > 252.00:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] <= 146.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] <= 54.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] <= 146.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] > 54.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] <= 146.50 and features[2] > 3.50 and features[8] <= 0.50 and features[7] <= 125.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] <= 146.50 and features[2] > 3.50 and features[8] <= 0.50 and features[7] > 125.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] <= 146.50 and features[2] > 3.50 and features[8] > 0.50 and features[4] <= 171.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] <= 146.50 and features[2] > 3.50 and features[8] > 0.50 and features[4] > 171.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] > 146.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[11] <= 2.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] > 146.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[11] > 2.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] > 146.50 and features[2] <= 3.50 and features[1] > 0.50 and features[9] <= 1.95:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] > 146.50 and features[2] <= 3.50 and features[1] > 0.50 and features[9] > 1.95:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] > 146.50 and features[2] > 3.50 and features[1] <= 0.50 and features[11] <= 2.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] > 146.50 and features[2] > 3.50 and features[1] <= 0.50 and features[11] > 2.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[7] > 146.50 and features[2] > 3.50 and features[1] > 0.50 and features[4] <= 266.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[7] > 146.50 and features[2] > 3.50 and features[1] > 0.50 and features[4] > 266.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[5] <= 0.50 and features[10] <= 2.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[5] <= 0.50 and features[10] <= 2.50 and features[2] > 3.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[5] <= 0.50 and features[10] > 2.50 and features[7] <= 161.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[5] <= 0.50 and features[10] > 2.50 and features[7] > 161.50:
        votes_0 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[5] > 0.50 and features[2] <= 3.50 and features[4] <= 239.50:
        votes_0 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[5] > 0.50 and features[2] <= 3.50 and features[4] > 239.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[5] > 0.50 and features[2] > 3.50 and features[7] <= 158.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] <= 0.50 and features[5] > 0.50 and features[2] > 3.50 and features[7] > 158.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[7] <= 179.50 and features[5] <= 0.50 and features[10] <= 2.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[7] <= 179.50 and features[5] <= 0.50 and features[10] > 2.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[7] <= 179.50 and features[5] > 0.50 and features[2] <= 1.50:
        votes_0 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[7] <= 179.50 and features[5] > 0.50 and features[2] > 1.50:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[7] > 179.50 and features[3] <= 119.00:
        votes_1 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[7] > 179.50 and features[3] > 119.00 and features[3] <= 145.00:
        votes_0 += 1
    if features[10] > 1.50 and features[8] > 0.50 and features[7] > 179.50 and features[3] > 119.00 and features[3] > 145.00:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 55.50 and features[9] <= 0.95 and features[0] <= 43.50 and features[7] <= 135.00:
        votes_1 += 1
    if features[10] <= 1.50 and features[0] <= 55.50 and features[9] <= 0.95 and features[0] <= 43.50 and features[7] > 135.00:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 55.50 and features[9] <= 0.95 and features[0] > 43.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 55.50 and features[9] <= 0.95 and features[0] > 43.50 and features[1] > 0.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 55.50 and features[9] > 0.95 and features[8] <= 0.50 and features[7] <= 139.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[0] <= 55.50 and features[9] > 0.95 and features[8] <= 0.50 and features[7] > 139.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] <= 55.50 and features[9] > 0.95 and features[8] > 0.50 and features[7] <= 172.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[0] <= 55.50 and features[9] > 0.95 and features[8] > 0.50 and features[7] > 172.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 55.50 and features[7] <= 147.50 and features[8] <= 0.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 55.50 and features[7] <= 147.50 and features[8] <= 0.50 and features[2] > 3.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[0] > 55.50 and features[7] <= 147.50 and features[8] > 0.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[0] > 55.50 and features[7] <= 147.50 and features[8] > 0.50 and features[1] > 0.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[0] > 55.50 and features[7] > 147.50 and features[2] <= 3.50 and features[4] <= 234.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 55.50 and features[7] > 147.50 and features[2] <= 3.50 and features[4] > 234.50:
        votes_0 += 1
    if features[10] <= 1.50 and features[0] > 55.50 and features[7] > 147.50 and features[2] > 3.50 and features[6] <= 0.50:
        votes_1 += 1
    if features[10] <= 1.50 and features[0] > 55.50 and features[7] > 147.50 and features[2] > 3.50 and features[6] > 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] <= 161.50 and features[2] <= 3.50 and features[7] <= 140.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] <= 161.50 and features[2] <= 3.50 and features[7] <= 140.50 and features[1] > 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] <= 161.50 and features[2] <= 3.50 and features[7] > 140.50 and features[6] <= 1.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] <= 161.50 and features[2] <= 3.50 and features[7] > 140.50 and features[6] > 1.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] <= 161.50 and features[2] > 3.50 and features[8] <= 0.50 and features[7] <= 150.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] <= 161.50 and features[2] > 3.50 and features[8] <= 0.50 and features[7] > 150.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] <= 161.50 and features[2] > 3.50 and features[8] > 0.50 and features[3] <= 135.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] <= 161.50 and features[2] > 3.50 and features[8] > 0.50 and features[3] > 135.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] > 161.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[7] > 161.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[1] > 0.50:
        votes_0 += 1
    if features[10] > 1.50 and features[7] > 161.50 and features[2] <= 3.50 and features[8] > 0.50 and features[4] <= 257.00:
        votes_1 += 1
    if features[10] > 1.50 and features[7] > 161.50 and features[2] <= 3.50 and features[8] > 0.50 and features[4] > 257.00:
        votes_1 += 1
    if features[10] > 1.50 and features[7] > 161.50 and features[2] > 3.50 and features[7] <= 179.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] > 161.50 and features[2] > 3.50 and features[7] <= 179.50 and features[8] > 0.50:
        votes_1 += 1
    if features[10] > 1.50 and features[7] > 161.50 and features[2] > 3.50 and features[7] > 179.50 and features[4] <= 275.50:
        votes_0 += 1
    if features[10] > 1.50 and features[7] > 161.50 and features[2] > 3.50 and features[7] > 179.50 and features[4] > 275.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[0] <= 55.50 and features[4] <= 241.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[0] <= 55.50 and features[4] > 241.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[0] > 55.50 and features[3] <= 131.00:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[0] > 55.50 and features[3] > 131.00:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[8] > 0.50 and features[7] <= 145.50 and features[0] <= 54.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[8] > 0.50 and features[7] <= 145.50 and features[0] > 54.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[8] > 0.50 and features[7] > 145.50 and features[4] <= 208.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] <= 3.50 and features[8] > 0.50 and features[7] > 145.50 and features[4] > 208.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[9] <= 0.85 and features[0] <= 52.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[9] <= 0.85 and features[0] <= 52.50 and features[8] > 0.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[9] <= 0.85 and features[0] > 52.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[9] <= 0.85 and features[0] > 52.50 and features[10] > 1.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[9] > 0.85 and features[8] <= 0.50 and features[0] <= 47.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[9] > 0.85 and features[8] <= 0.50 and features[0] > 47.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[9] > 0.85 and features[8] > 0.50 and features[7] <= 162.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[2] > 3.50 and features[9] > 0.85 and features[8] > 0.50 and features[7] > 162.50:
        votes_1 += 1
    if features[1] > 0.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[8] <= 0.50 and features[6] <= 1.00:
        votes_1 += 1
    if features[1] > 0.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[8] <= 0.50 and features[6] > 1.00:
        votes_1 += 1
    if features[1] > 0.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[8] > 0.50 and features[7] <= 146.50:
        votes_1 += 1
    if features[1] > 0.50 and features[7] <= 160.50 and features[9] <= 0.95 and features[8] > 0.50 and features[7] > 146.50:
        votes_1 += 1
    if features[1] > 0.50 and features[7] <= 160.50 and features[9] > 0.95 and features[0] <= 52.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[1] > 0.50 and features[7] <= 160.50 and features[9] > 0.95 and features[0] <= 52.50 and features[10] > 1.50:
        votes_1 += 1
    if features[1] > 0.50 and features[7] <= 160.50 and features[9] > 0.95 and features[0] > 52.50 and features[7] <= 139.50:
        votes_1 += 1
    if features[1] > 0.50 and features[7] <= 160.50 and features[9] > 0.95 and features[0] > 52.50 and features[7] > 139.50:
        votes_1 += 1
    if features[1] > 0.50 and features[7] > 160.50 and features[9] <= 0.85 and features[7] <= 179.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[1] > 0.50 and features[7] > 160.50 and features[9] <= 0.85 and features[7] <= 179.50 and features[2] > 3.50:
        votes_1 += 1
    if features[1] > 0.50 and features[7] > 160.50 and features[9] <= 0.85 and features[7] > 179.50 and features[0] <= 58.50:
        votes_0 += 1
    if features[1] > 0.50 and features[7] > 160.50 and features[9] <= 0.85 and features[7] > 179.50 and features[0] > 58.50:
        votes_0 += 1
    if features[1] > 0.50 and features[7] > 160.50 and features[9] > 0.85 and features[7] <= 179.50 and features[9] <= 2.55:
        votes_1 += 1
    if features[1] > 0.50 and features[7] > 160.50 and features[9] > 0.85 and features[7] <= 179.50 and features[9] > 2.55:
        votes_1 += 1
    if features[1] > 0.50 and features[7] > 160.50 and features[9] > 0.85 and features[7] > 179.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[1] > 0.50 and features[7] > 160.50 and features[9] > 0.85 and features[7] > 179.50 and features[2] > 3.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 54.50 and features[9] <= 0.85 and features[7] <= 160.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 54.50 and features[9] <= 0.85 and features[7] <= 160.50 and features[8] > 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 54.50 and features[9] <= 0.85 and features[7] > 160.50 and features[4] <= 273.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 54.50 and features[9] <= 0.85 and features[7] > 160.50 and features[4] > 273.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 54.50 and features[9] > 0.85 and features[9] <= 1.95 and features[4] <= 235.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 54.50 and features[9] > 0.85 and features[9] <= 1.95 and features[4] > 235.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] <= 54.50 and features[9] > 0.85 and features[9] > 1.95 and features[7] <= 159.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 54.50 and features[9] > 0.85 and features[9] > 1.95 and features[7] > 159.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] > 54.50 and features[1] <= 0.50 and features[6] <= 0.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] > 54.50 and features[1] <= 0.50 and features[6] <= 0.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 54.50 and features[1] <= 0.50 and features[6] > 0.50 and features[0] <= 57.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] > 54.50 and features[1] <= 0.50 and features[6] > 0.50 and features[0] > 57.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] > 54.50 and features[1] > 0.50 and features[9] <= 0.95 and features[7] <= 160.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 54.50 and features[1] > 0.50 and features[9] <= 0.95 and features[7] > 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[0] > 54.50 and features[1] > 0.50 and features[9] > 0.95 and features[9] <= 2.55:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 54.50 and features[1] > 0.50 and features[9] > 0.95 and features[9] > 2.55:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] <= 160.50 and features[10] <= 1.50 and features[0] <= 51.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] <= 160.50 and features[10] <= 1.50 and features[0] > 51.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] <= 160.50 and features[10] > 1.50 and features[0] <= 42.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] <= 160.50 and features[10] > 1.50 and features[0] > 42.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] > 160.50 and features[8] <= 0.50 and features[0] <= 57.50:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] > 160.50 and features[8] <= 0.50 and features[0] > 57.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] > 160.50 and features[8] > 0.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] > 160.50 and features[8] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[4] <= 243.50 and features[7] <= 161.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[4] <= 243.50 and features[7] <= 161.50 and features[10] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[4] <= 243.50 and features[7] > 161.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[4] <= 243.50 and features[7] > 161.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[4] > 243.50 and features[10] <= 1.50 and features[6] <= 1.00:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[4] > 243.50 and features[10] <= 1.50 and features[6] > 1.00:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[4] > 243.50 and features[10] > 1.50 and features[3] <= 124.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[4] > 243.50 and features[10] > 1.50 and features[3] > 124.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[4] <= 267.50 and features[7] <= 147.50 and features[4] <= 220.50 and features[9] <= 0.70:
        votes_0 += 1
    if features[1] <= 0.50 and features[4] <= 267.50 and features[7] <= 147.50 and features[4] <= 220.50 and features[9] > 0.70:
        votes_1 += 1
    if features[1] <= 0.50 and features[4] <= 267.50 and features[7] <= 147.50 and features[4] > 220.50 and features[10] <= 1.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[4] <= 267.50 and features[7] <= 147.50 and features[4] > 220.50 and features[10] > 1.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[4] <= 267.50 and features[7] > 147.50 and features[9] <= 1.15 and features[6] <= 1.00:
        votes_0 += 1
    if features[1] <= 0.50 and features[4] <= 267.50 and features[7] > 147.50 and features[9] <= 1.15 and features[6] > 1.00:
        votes_0 += 1
    if features[1] <= 0.50 and features[4] <= 267.50 and features[7] > 147.50 and features[9] > 1.15 and features[2] <= 3.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[4] <= 267.50 and features[7] > 147.50 and features[9] > 1.15 and features[2] > 3.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[4] > 267.50 and features[2] <= 3.50 and features[11] <= 2.50 and features[9] <= 1.10:
        votes_0 += 1
    if features[1] <= 0.50 and features[4] > 267.50 and features[2] <= 3.50 and features[11] <= 2.50 and features[9] > 1.10:
        votes_1 += 1
    if features[1] <= 0.50 and features[4] > 267.50 and features[2] <= 3.50 and features[11] > 2.50 and features[0] <= 64.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[4] > 267.50 and features[2] <= 3.50 and features[11] > 2.50 and features[0] > 64.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[4] > 267.50 and features[2] > 3.50 and features[9] <= 0.55 and features[7] <= 143.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[4] > 267.50 and features[2] > 3.50 and features[9] <= 0.55 and features[7] > 143.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[4] > 267.50 and features[2] > 3.50 and features[9] > 0.55 and features[10] <= 1.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[4] > 267.50 and features[2] > 3.50 and features[9] > 0.55 and features[10] > 1.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] <= 0.95 and features[7] <= 147.50 and features[7] <= 125.50 and features[7] <= 110.00:
        votes_1 += 1
    if features[1] > 0.50 and features[9] <= 0.95 and features[7] <= 147.50 and features[7] <= 125.50 and features[7] > 110.00:
        votes_1 += 1
    if features[1] > 0.50 and features[9] <= 0.95 and features[7] <= 147.50 and features[7] > 125.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] <= 0.95 and features[7] <= 147.50 and features[7] > 125.50 and features[8] > 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] <= 0.95 and features[7] > 147.50 and features[3] <= 141.00 and features[2] <= 3.50:
        votes_0 += 1
    if features[1] > 0.50 and features[9] <= 0.95 and features[7] > 147.50 and features[3] <= 141.00 and features[2] > 3.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] <= 0.95 and features[7] > 147.50 and features[3] > 141.00 and features[2] <= 3.50:
        votes_0 += 1
    if features[1] > 0.50 and features[9] <= 0.95 and features[7] > 147.50 and features[3] > 141.00 and features[2] > 3.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] > 0.95 and features[4] <= 203.50 and features[0] <= 55.50 and features[2] <= 3.50:
        votes_0 += 1
    if features[1] > 0.50 and features[9] > 0.95 and features[4] <= 203.50 and features[0] <= 55.50 and features[2] > 3.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] > 0.95 and features[4] <= 203.50 and features[0] > 55.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] > 0.95 and features[4] <= 203.50 and features[0] > 55.50 and features[8] > 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] > 0.95 and features[4] > 203.50 and features[0] <= 54.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] > 0.95 and features[4] > 203.50 and features[0] <= 54.50 and features[8] > 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] > 0.95 and features[4] > 203.50 and features[0] > 54.50 and features[4] <= 245.50:
        votes_1 += 1
    if features[1] > 0.50 and features[9] > 0.95 and features[4] > 203.50 and features[0] > 54.50 and features[4] > 245.50:
        votes_1 += 1
    total = votes_0 + votes_1
    if total == 0:
        return 0.7020
    return votes_1 / total


def predict_zone_3(features):
    """Predict for zone 3. 316 rules, majority vote."""
    votes_0, votes_1 = 0, 0
    if features[1] <= 0.50 and features[7] <= 161.50 and features[10] <= 1.50 and features[4] <= 229.50 and features[7] <= 140.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] <= 161.50 and features[10] <= 1.50 and features[4] <= 229.50 and features[7] > 140.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] <= 161.50 and features[10] <= 1.50 and features[4] > 229.50 and features[0] <= 55.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] <= 161.50 and features[10] <= 1.50 and features[4] > 229.50 and features[0] > 55.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] <= 161.50 and features[10] > 1.50 and features[2] <= 3.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] <= 161.50 and features[10] > 1.50 and features[2] <= 3.50 and features[8] > 0.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] <= 161.50 and features[10] > 1.50 and features[2] > 3.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] <= 161.50 and features[10] > 1.50 and features[2] > 3.50 and features[8] > 0.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] > 161.50 and features[9] <= 0.95 and features[2] <= 3.50 and features[2] <= 1.50:
        votes_0 += 1
    if features[1] <= 0.50 and features[7] > 161.50 and features[9] <= 0.95 and features[2] <= 3.50 and features[2] > 1.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] > 161.50 and features[9] <= 0.95 and features[2] > 3.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] > 161.50 and features[9] <= 0.95 and features[2] > 3.50 and features[0] > 53.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] > 161.50 and features[9] > 0.95 and features[7] <= 183.00 and features[10] <= 1.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] > 161.50 and features[9] > 0.95 and features[7] <= 183.00 and features[10] > 1.50:
        votes_1 += 1
    if features[1] <= 0.50 and features[7] > 161.50 and features[9] > 0.95 and features[7] > 183.00:
        votes_0 += 1
    if features[1] > 0.50 and features[0] <= 53.50 and features[2] <= 3.50 and features[9] <= 0.85 and features[12] <= 6.50:
        votes_0 += 1
    if features[1] > 0.50 and features[0] <= 53.50 and features[2] <= 3.50 and features[9] <= 0.85 and features[12] > 6.50:
        votes_1 += 1
    if features[1] > 0.50 and features[0] <= 53.50 and features[2] <= 3.50 and features[9] > 0.85 and features[9] <= 1.85:
        votes_1 += 1
    if features[1] > 0.50 and features[0] <= 53.50 and features[2] <= 3.50 and features[9] > 0.85 and features[9] > 1.85:
        votes_1 += 1
    if features[1] > 0.50 and features[0] <= 53.50 and features[2] > 3.50 and features[6] <= 0.50 and features[9] <= 0.95:
        votes_1 += 1
    if features[1] > 0.50 and features[0] <= 53.50 and features[2] > 3.50 and features[6] <= 0.50 and features[9] > 0.95:
        votes_1 += 1
    if features[1] > 0.50 and features[0] <= 53.50 and features[2] > 3.50 and features[6] > 0.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[1] > 0.50 and features[0] <= 53.50 and features[2] > 3.50 and features[6] > 0.50 and features[10] > 1.50:
        votes_1 += 1
    if features[1] > 0.50 and features[0] > 53.50 and features[2] <= 3.50 and features[5] <= 0.50 and features[9] <= 0.85:
        votes_1 += 1
    if features[1] > 0.50 and features[0] > 53.50 and features[2] <= 3.50 and features[5] <= 0.50 and features[9] > 0.85:
        votes_1 += 1
    if features[1] > 0.50 and features[0] > 53.50 and features[2] <= 3.50 and features[5] > 0.50 and features[7] <= 158.50:
        votes_1 += 1
    if features[1] > 0.50 and features[0] > 53.50 and features[2] <= 3.50 and features[5] > 0.50 and features[7] > 158.50:
        votes_1 += 1
    if features[1] > 0.50 and features[0] > 53.50 and features[2] > 3.50 and features[11] <= 2.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[0] > 53.50 and features[2] > 3.50 and features[11] <= 2.50 and features[8] > 0.50:
        votes_1 += 1
    if features[1] > 0.50 and features[0] > 53.50 and features[2] > 3.50 and features[11] > 2.50 and features[0] <= 61.50:
        votes_1 += 1
    if features[1] > 0.50 and features[0] > 53.50 and features[2] > 3.50 and features[11] > 2.50 and features[0] > 61.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] <= 203.50 and features[9] <= 0.70 and features[2] <= 3.50 and features[7] <= 141.00:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] <= 203.50 and features[9] <= 0.70 and features[2] <= 3.50 and features[7] > 141.00:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] <= 203.50 and features[9] <= 0.70 and features[2] > 3.50 and features[7] <= 148.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] <= 203.50 and features[9] <= 0.70 and features[2] > 3.50 and features[7] > 148.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] <= 203.50 and features[9] > 0.70 and features[9] <= 2.05 and features[7] <= 130.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] <= 203.50 and features[9] > 0.70 and features[9] <= 2.05 and features[7] > 130.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] <= 203.50 and features[9] > 0.70 and features[9] > 2.05 and features[7] <= 157.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] <= 203.50 and features[9] > 0.70 and features[9] > 2.05 and features[7] > 157.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] > 203.50 and features[2] <= 3.50 and features[2] <= 2.50 and features[7] <= 146.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] > 203.50 and features[2] <= 3.50 and features[2] <= 2.50 and features[7] > 146.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] > 203.50 and features[2] <= 3.50 and features[2] > 2.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] > 203.50 and features[2] <= 3.50 and features[2] > 2.50 and features[0] > 53.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] > 203.50 and features[2] > 3.50 and features[9] <= 0.85 and features[3] <= 139.00:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] > 203.50 and features[2] > 3.50 and features[9] <= 0.85 and features[3] > 139.00:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] > 203.50 and features[2] > 3.50 and features[9] > 0.85 and features[7] <= 132.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[4] > 203.50 and features[2] > 3.50 and features[9] > 0.85 and features[7] > 132.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] <= 57.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[6] <= 1.00:
        votes_0 += 1
    if features[7] > 160.50 and features[0] <= 57.50 and features[2] <= 3.50 and features[1] <= 0.50 and features[6] > 1.00:
        votes_1 += 1
    if features[7] > 160.50 and features[0] <= 57.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] <= 36.00:
        votes_1 += 1
    if features[7] > 160.50 and features[0] <= 57.50 and features[2] <= 3.50 and features[1] > 0.50 and features[0] > 36.00:
        votes_1 += 1
    if features[7] > 160.50 and features[0] <= 57.50 and features[2] > 3.50 and features[1] <= 0.50 and features[0] <= 39.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] <= 57.50 and features[2] > 3.50 and features[1] <= 0.50 and features[0] > 39.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] <= 57.50 and features[2] > 3.50 and features[1] > 0.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] <= 57.50 and features[2] > 3.50 and features[1] > 0.50 and features[0] > 53.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] > 57.50 and features[2] <= 3.50 and features[9] <= 0.75 and features[7] <= 168.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] > 57.50 and features[2] <= 3.50 and features[9] <= 0.75 and features[7] > 168.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] > 57.50 and features[2] <= 3.50 and features[9] > 0.75 and features[10] <= 1.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] > 57.50 and features[2] <= 3.50 and features[9] > 0.75 and features[10] > 1.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] > 57.50 and features[2] > 3.50 and features[9] <= 1.05 and features[1] <= 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] > 57.50 and features[2] > 3.50 and features[9] <= 1.05 and features[1] > 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] > 57.50 and features[2] > 3.50 and features[9] > 1.05 and features[5] <= 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[0] > 57.50 and features[2] > 3.50 and features[9] > 1.05 and features[5] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 52.50 and features[6] <= 0.50 and features[9] <= 0.95 and features[9] <= 0.70:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 52.50 and features[6] <= 0.50 and features[9] <= 0.95 and features[9] > 0.70:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 52.50 and features[6] <= 0.50 and features[9] > 0.95 and features[8] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 52.50 and features[6] <= 0.50 and features[9] > 0.95 and features[8] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 52.50 and features[6] > 0.50 and features[1] <= 0.50 and features[9] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 52.50 and features[6] > 0.50 and features[1] <= 0.50 and features[9] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 52.50 and features[6] > 0.50 and features[1] > 0.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] <= 52.50 and features[6] > 0.50 and features[1] > 0.50 and features[7] > 160.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 52.50 and features[9] <= 0.70 and features[6] <= 1.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 52.50 and features[9] <= 0.70 and features[6] <= 1.50 and features[12] > 6.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 52.50 and features[9] <= 0.70 and features[6] > 1.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 52.50 and features[9] <= 0.70 and features[6] > 1.50 and features[10] > 1.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 52.50 and features[9] > 0.70 and features[7] <= 160.50 and features[4] <= 233.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 52.50 and features[9] > 0.70 and features[7] <= 160.50 and features[4] > 233.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 52.50 and features[9] > 0.70 and features[7] > 160.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[0] > 52.50 and features[9] > 0.70 and features[7] > 160.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] <= 165.50 and features[7] <= 150.50 and features[6] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] <= 165.50 and features[7] <= 150.50 and features[6] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] <= 165.50 and features[7] > 150.50 and features[6] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] <= 165.50 and features[7] > 150.50 and features[6] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] > 165.50 and features[8] <= 0.50 and features[7] <= 167.00:
        votes_0 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] > 165.50 and features[8] <= 0.50 and features[7] > 167.00:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] > 165.50 and features[8] > 0.50 and features[0] <= 70.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[7] > 165.50 and features[8] > 0.50 and features[0] > 70.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[7] <= 161.50 and features[3] <= 141.00 and features[3] <= 107.00:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[7] <= 161.50 and features[3] <= 141.00 and features[3] > 107.00:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[7] <= 161.50 and features[3] > 141.00 and features[7] <= 149.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[7] <= 161.50 and features[3] > 141.00 and features[7] > 149.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[7] > 161.50 and features[4] <= 230.50 and features[5] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[7] > 161.50 and features[4] <= 230.50 and features[5] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[7] > 161.50 and features[4] > 230.50 and features[7] <= 185.00:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[7] > 161.50 and features[4] > 230.50 and features[7] > 185.00:
        votes_0 += 1
    if features[7] <= 160.50 and features[8] <= 0.50 and features[10] <= 1.50 and features[7] <= 146.50 and features[9] <= 1.05:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] <= 0.50 and features[10] <= 1.50 and features[7] <= 146.50 and features[9] > 1.05:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] <= 0.50 and features[10] <= 1.50 and features[7] > 146.50 and features[4] <= 228.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] <= 0.50 and features[10] <= 1.50 and features[7] > 146.50 and features[4] > 228.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] <= 0.50 and features[10] > 1.50 and features[2] <= 3.50 and features[7] <= 150.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] <= 0.50 and features[10] > 1.50 and features[2] <= 3.50 and features[7] > 150.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] <= 0.50 and features[10] > 1.50 and features[2] > 3.50 and features[7] <= 140.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] <= 0.50 and features[10] > 1.50 and features[2] > 3.50 and features[7] > 140.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] > 0.50 and features[1] <= 0.50 and features[0] <= 44.50 and features[6] <= 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] > 0.50 and features[1] <= 0.50 and features[0] <= 44.50 and features[6] > 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] > 0.50 and features[1] <= 0.50 and features[0] > 44.50 and features[6] <= 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] > 0.50 and features[1] <= 0.50 and features[0] > 44.50 and features[6] > 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] <= 203.50 and features[2] <= 1.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] <= 203.50 and features[2] > 1.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] > 203.50 and features[0] <= 45.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[8] > 0.50 and features[1] > 0.50 and features[4] > 203.50 and features[0] > 45.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[7] <= 179.50 and features[9] <= 0.75 and features[7] <= 162.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[7] <= 179.50 and features[9] <= 0.75 and features[7] > 162.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[7] <= 179.50 and features[9] > 0.75 and features[1] <= 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[7] <= 179.50 and features[9] > 0.75 and features[1] > 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[7] > 179.50 and features[8] <= 0.50 and features[4] <= 282.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[7] > 179.50 and features[8] <= 0.50 and features[4] > 282.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[7] > 179.50 and features[8] > 0.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[7] > 179.50 and features[8] > 0.50 and features[1] > 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[9] <= 0.85 and features[1] <= 0.50 and features[12] <= 6.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[9] <= 0.85 and features[1] <= 0.50 and features[12] > 6.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[9] <= 0.85 and features[1] > 0.50 and features[5] <= 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[9] <= 0.85 and features[1] > 0.50 and features[5] > 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[9] > 0.85 and features[7] <= 183.00 and features[7] <= 179.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[9] > 0.85 and features[7] <= 183.00 and features[7] > 179.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[9] > 0.85 and features[7] > 183.00 and features[6] <= 1.00:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[9] > 0.85 and features[7] > 183.00 and features[6] > 1.00:
        votes_0 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[9] <= 0.70 and features[10] <= 1.50 and features[0] <= 43.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[9] <= 0.70 and features[10] <= 1.50 and features[0] > 43.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[9] <= 0.70 and features[10] > 1.50 and features[4] <= 306.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[9] <= 0.70 and features[10] > 1.50 and features[4] > 306.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[9] > 0.70 and features[9] <= 1.85 and features[10] <= 1.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[9] > 0.70 and features[9] <= 1.85 and features[10] > 1.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[9] > 0.70 and features[9] > 1.85 and features[1] <= 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[9] > 0.70 and features[9] > 1.85 and features[1] > 0.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[0] <= 51.50 and features[6] <= 0.50 and features[9] <= 0.95:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[0] <= 51.50 and features[6] <= 0.50 and features[9] > 0.95:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[0] <= 51.50 and features[6] > 0.50 and features[4] <= 181.00:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[0] <= 51.50 and features[6] > 0.50 and features[4] > 181.00:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[0] > 51.50 and features[10] <= 1.50 and features[7] <= 151.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[0] > 51.50 and features[10] <= 1.50 and features[7] > 151.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[0] > 51.50 and features[10] > 1.50 and features[9] <= 0.45:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[0] > 51.50 and features[10] > 1.50 and features[9] > 0.45:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[9] <= 0.75 and features[0] <= 52.50 and features[8] <= 0.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[9] <= 0.75 and features[0] <= 52.50 and features[8] > 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[9] <= 0.75 and features[0] > 52.50 and features[0] <= 57.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[9] <= 0.75 and features[0] > 52.50 and features[0] > 57.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[9] > 0.75 and features[7] <= 179.50 and features[7] <= 161.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[9] > 0.75 and features[7] <= 179.50 and features[7] > 161.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[9] > 0.75 and features[7] > 179.50 and features[3] <= 131.00:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[9] > 0.75 and features[7] > 179.50 and features[3] > 131.00:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[4] <= 220.00 and features[0] <= 53.50 and features[3] <= 143.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[4] <= 220.00 and features[0] <= 53.50 and features[3] > 143.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[4] <= 220.00 and features[0] > 53.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[4] <= 220.00 and features[0] > 53.50 and features[12] > 6.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[4] > 220.00 and features[9] <= 0.85 and features[6] <= 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[4] > 220.00 and features[9] <= 0.85 and features[6] > 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[4] > 220.00 and features[9] > 0.85 and features[4] <= 287.00:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[4] > 220.00 and features[9] > 0.85 and features[4] > 287.00:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[0] <= 52.50 and features[12] <= 6.50 and features[11] <= 2.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[0] <= 52.50 and features[12] <= 6.50 and features[11] > 2.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[0] <= 52.50 and features[12] > 6.50 and features[4] <= 212.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[0] <= 52.50 and features[12] > 6.50 and features[4] > 212.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[0] > 52.50 and features[10] <= 1.50 and features[0] <= 57.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[0] > 52.50 and features[10] <= 1.50 and features[0] > 57.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[0] > 52.50 and features[10] > 1.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] <= 0.50 and features[0] > 52.50 and features[10] > 1.50 and features[1] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[2] <= 1.50 and features[7] <= 156.50 and features[7] <= 140.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[2] <= 1.50 and features[7] <= 156.50 and features[7] > 140.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[2] <= 1.50 and features[7] > 156.50 and features[9] <= 1.30:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[2] <= 1.50 and features[7] > 156.50 and features[9] > 1.30:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[2] > 1.50 and features[9] <= 0.85 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[2] > 1.50 and features[9] <= 0.85 and features[1] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[2] > 1.50 and features[9] > 0.85 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[8] > 0.50 and features[2] > 1.50 and features[9] > 0.85 and features[1] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[0] <= 53.50 and features[8] <= 0.50 and features[7] <= 169.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[0] <= 53.50 and features[8] <= 0.50 and features[7] > 169.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[0] <= 53.50 and features[8] > 0.50 and features[5] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[0] <= 53.50 and features[8] > 0.50 and features[5] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[0] > 53.50 and features[10] <= 1.50 and features[7] <= 153.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[0] > 53.50 and features[10] <= 1.50 and features[7] > 153.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[0] > 53.50 and features[10] > 1.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] <= 0.85 and features[0] > 53.50 and features[10] > 1.50 and features[1] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[1] <= 0.50 and features[12] <= 6.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[1] <= 0.50 and features[12] <= 6.50 and features[10] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[1] <= 0.50 and features[12] > 6.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[1] <= 0.50 and features[12] > 6.50 and features[8] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[1] > 0.50 and features[0] <= 52.50 and features[9] <= 1.95:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[1] > 0.50 and features[0] <= 52.50 and features[9] > 1.95:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[1] > 0.50 and features[0] > 52.50 and features[7] <= 189.00:
        votes_1 += 1
    if features[2] > 3.50 and features[9] > 0.85 and features[1] > 0.50 and features[0] > 52.50 and features[7] > 189.00:
        votes_0 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[6] <= 0.50 and features[0] <= 52.50 and features[4] <= 211.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[6] <= 0.50 and features[0] <= 52.50 and features[4] > 211.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[6] <= 0.50 and features[0] > 52.50 and features[4] <= 369.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[6] <= 0.50 and features[0] > 52.50 and features[4] > 369.50:
        votes_0 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[6] > 0.50 and features[8] <= 0.50 and features[3] <= 186.00:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[6] > 0.50 and features[8] <= 0.50 and features[3] > 186.00:
        votes_0 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[6] > 0.50 and features[8] > 0.50 and features[4] <= 204.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] <= 3.50 and features[6] > 0.50 and features[8] > 0.50 and features[4] > 204.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[1] <= 0.50 and features[0] <= 56.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[1] <= 0.50 and features[0] <= 56.50 and features[12] > 6.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[1] <= 0.50 and features[0] > 56.50 and features[7] <= 153.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[1] <= 0.50 and features[0] > 56.50 and features[7] > 153.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[1] > 0.50 and features[9] <= 0.45 and features[0] <= 42.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[1] > 0.50 and features[9] <= 0.45 and features[0] > 42.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[1] > 0.50 and features[9] > 0.45 and features[0] <= 52.50:
        votes_1 += 1
    if features[7] <= 160.50 and features[2] > 3.50 and features[1] > 0.50 and features[9] > 0.45 and features[0] > 52.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[10] <= 1.50 and features[0] <= 57.50:
        votes_0 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[10] <= 1.50 and features[0] > 57.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[10] > 1.50 and features[10] <= 2.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] <= 0.50 and features[10] > 1.50 and features[10] > 2.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[2] <= 2.50 and features[9] <= 0.45:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[2] <= 2.50 and features[9] > 0.45:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[2] > 2.50 and features[7] <= 184.00:
        votes_1 += 1
    if features[7] > 160.50 and features[2] <= 3.50 and features[8] > 0.50 and features[2] > 2.50 and features[7] > 184.00:
        votes_0 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[0] <= 49.50 and features[4] <= 202.00 and features[7] <= 169.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[0] <= 49.50 and features[4] <= 202.00 and features[7] > 169.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[0] <= 49.50 and features[4] > 202.00 and features[10] <= 1.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[0] <= 49.50 and features[4] > 202.00 and features[10] > 1.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[0] > 49.50 and features[0] <= 58.50 and features[9] <= 0.85:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[0] > 49.50 and features[0] <= 58.50 and features[9] > 0.85:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[0] > 49.50 and features[0] > 58.50 and features[6] <= 0.50:
        votes_1 += 1
    if features[7] > 160.50 and features[2] > 3.50 and features[0] > 49.50 and features[0] > 58.50 and features[6] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] <= 0.75 and features[10] <= 1.50 and features[8] <= 0.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] <= 0.75 and features[10] <= 1.50 and features[8] <= 0.50 and features[7] > 160.50:
        votes_0 += 1
    if features[2] <= 3.50 and features[9] <= 0.75 and features[10] <= 1.50 and features[8] > 0.50 and features[7] <= 162.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] <= 0.75 and features[10] <= 1.50 and features[8] > 0.50 and features[7] > 162.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] <= 0.75 and features[10] > 1.50 and features[8] <= 0.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] <= 0.75 and features[10] > 1.50 and features[8] <= 0.50 and features[12] > 6.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] <= 0.75 and features[10] > 1.50 and features[8] > 0.50 and features[4] <= 233.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] <= 0.75 and features[10] > 1.50 and features[8] > 0.50 and features[4] > 233.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] > 0.75 and features[9] <= 1.95 and features[8] <= 0.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] > 0.75 and features[9] <= 1.95 and features[8] <= 0.50 and features[1] > 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] > 0.75 and features[9] <= 1.95 and features[8] > 0.50 and features[7] <= 161.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] > 0.75 and features[9] <= 1.95 and features[8] > 0.50 and features[7] > 161.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] > 0.75 and features[9] > 1.95 and features[7] <= 160.50 and features[7] <= 150.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] > 0.75 and features[9] > 1.95 and features[7] <= 160.50 and features[7] > 150.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] > 0.75 and features[9] > 1.95 and features[7] > 160.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] <= 3.50 and features[9] > 0.75 and features[9] > 1.95 and features[7] > 160.50 and features[1] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[7] <= 148.50 and features[5] <= 0.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[7] <= 148.50 and features[5] <= 0.50 and features[1] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[7] <= 148.50 and features[5] > 0.50 and features[0] <= 34.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[7] <= 148.50 and features[5] > 0.50 and features[0] > 34.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[7] > 148.50 and features[8] <= 0.50 and features[9] <= 0.85:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[7] > 148.50 and features[8] <= 0.50 and features[9] > 0.85:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[7] > 148.50 and features[8] > 0.50 and features[0] <= 46.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] <= 160.50 and features[7] > 148.50 and features[8] > 0.50 and features[0] > 46.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[9] <= 0.85 and features[0] <= 53.50 and features[10] <= 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[9] <= 0.85 and features[0] <= 53.50 and features[10] > 1.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[9] <= 0.85 and features[0] > 53.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[9] <= 0.85 and features[0] > 53.50 and features[1] > 0.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[9] > 0.85 and features[7] <= 185.00 and features[4] <= 203.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[9] > 0.85 and features[7] <= 185.00 and features[4] > 203.50:
        votes_1 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[9] > 0.85 and features[7] > 185.00 and features[9] <= 1.10:
        votes_0 += 1
    if features[2] > 3.50 and features[7] > 160.50 and features[9] > 0.85 and features[7] > 185.00 and features[9] > 1.10:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] <= 1.50 and features[1] <= 0.50 and features[0] <= 59.50 and features[9] <= 1.85:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] <= 1.50 and features[1] <= 0.50 and features[0] <= 59.50 and features[9] > 1.85:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] <= 1.50 and features[1] <= 0.50 and features[0] > 59.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] <= 1.50 and features[1] <= 0.50 and features[0] > 59.50 and features[12] > 6.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] <= 1.50 and features[1] > 0.50 and features[5] <= 0.50 and features[3] <= 103.00:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] <= 1.50 and features[1] > 0.50 and features[5] <= 0.50 and features[3] > 103.00:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] <= 1.50 and features[1] > 0.50 and features[5] > 0.50 and features[3] <= 141.00:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] <= 1.50 and features[1] > 0.50 and features[5] > 0.50 and features[3] > 141.00:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] > 1.50 and features[6] <= 0.50 and features[2] <= 3.50 and features[5] <= 0.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] > 1.50 and features[6] <= 0.50 and features[2] <= 3.50 and features[5] > 0.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] > 1.50 and features[6] <= 0.50 and features[2] > 3.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] > 1.50 and features[6] <= 0.50 and features[2] > 3.50 and features[12] > 6.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] > 1.50 and features[6] > 0.50 and features[2] <= 3.50 and features[11] <= 2.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] > 1.50 and features[6] > 0.50 and features[2] <= 3.50 and features[11] > 2.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] > 1.50 and features[6] > 0.50 and features[2] > 3.50 and features[0] <= 34.50:
        votes_1 += 1
    if features[8] <= 0.50 and features[10] > 1.50 and features[6] > 0.50 and features[2] > 3.50 and features[0] > 34.50:
        votes_1 += 1
    if features[8] > 0.50 and features[6] <= 0.50 and features[7] <= 187.00 and features[10] <= 1.50 and features[9] <= 0.55:
        votes_1 += 1
    if features[8] > 0.50 and features[6] <= 0.50 and features[7] <= 187.00 and features[10] <= 1.50 and features[9] > 0.55:
        votes_1 += 1
    if features[8] > 0.50 and features[6] <= 0.50 and features[7] <= 187.00 and features[10] > 1.50 and features[7] <= 160.50:
        votes_1 += 1
    if features[8] > 0.50 and features[6] <= 0.50 and features[7] <= 187.00 and features[10] > 1.50 and features[7] > 160.50:
        votes_1 += 1
    if features[8] > 0.50 and features[6] <= 0.50 and features[7] > 187.00:
        votes_0 += 1
    if features[8] > 0.50 and features[6] > 0.50 and features[7] <= 180.00 and features[0] <= 54.50 and features[1] <= 0.50:
        votes_1 += 1
    if features[8] > 0.50 and features[6] > 0.50 and features[7] <= 180.00 and features[0] <= 54.50 and features[1] > 0.50:
        votes_1 += 1
    if features[8] > 0.50 and features[6] > 0.50 and features[7] <= 180.00 and features[0] > 54.50 and features[3] <= 179.00:
        votes_1 += 1
    if features[8] > 0.50 and features[6] > 0.50 and features[7] <= 180.00 and features[0] > 54.50 and features[3] > 179.00:
        votes_1 += 1
    if features[8] > 0.50 and features[6] > 0.50 and features[7] > 180.00 and features[2] <= 3.50 and features[4] <= 281.00:
        votes_0 += 1
    if features[8] > 0.50 and features[6] > 0.50 and features[7] > 180.00 and features[2] <= 3.50 and features[4] > 281.00:
        votes_0 += 1
    if features[8] > 0.50 and features[6] > 0.50 and features[7] > 180.00 and features[2] > 3.50 and features[0] <= 53.00:
        votes_0 += 1
    if features[8] > 0.50 and features[6] > 0.50 and features[7] > 180.00 and features[2] > 3.50 and features[0] > 53.00:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] <= 3.50 and features[7] <= 155.50 and features[10] <= 1.50 and features[4] <= 196.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] <= 3.50 and features[7] <= 155.50 and features[10] <= 1.50 and features[4] > 196.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] <= 3.50 and features[7] <= 155.50 and features[10] > 1.50 and features[2] <= 1.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] <= 3.50 and features[7] <= 155.50 and features[10] > 1.50 and features[2] > 1.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] <= 3.50 and features[7] > 155.50 and features[10] <= 1.50 and features[1] <= 0.50:
        votes_0 += 1
    if features[9] <= 0.75 and features[2] <= 3.50 and features[7] > 155.50 and features[10] <= 1.50 and features[1] > 0.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] <= 3.50 and features[7] > 155.50 and features[10] > 1.50 and features[0] <= 52.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] <= 3.50 and features[7] > 155.50 and features[10] > 1.50 and features[0] > 52.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] > 3.50 and features[6] <= 0.50 and features[0] <= 43.50 and features[12] <= 6.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] > 3.50 and features[6] <= 0.50 and features[0] <= 43.50 and features[12] > 6.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] > 3.50 and features[6] <= 0.50 and features[0] > 43.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] > 3.50 and features[6] <= 0.50 and features[0] > 43.50 and features[8] > 0.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] > 3.50 and features[6] > 0.50 and features[1] <= 0.50 and features[0] <= 58.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] > 3.50 and features[6] > 0.50 and features[1] <= 0.50 and features[0] > 58.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] > 3.50 and features[6] > 0.50 and features[1] > 0.50 and features[0] <= 53.50:
        votes_1 += 1
    if features[9] <= 0.75 and features[2] > 3.50 and features[6] > 0.50 and features[1] > 0.50 and features[0] > 53.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] <= 3.50 and features[7] <= 160.50 and features[10] <= 1.50 and features[0] <= 54.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] <= 3.50 and features[7] <= 160.50 and features[10] <= 1.50 and features[0] > 54.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] <= 3.50 and features[7] <= 160.50 and features[10] > 1.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] <= 3.50 and features[7] <= 160.50 and features[10] > 1.50 and features[8] > 0.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] <= 3.50 and features[7] > 160.50 and features[10] <= 1.50 and features[11] <= 2.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] <= 3.50 and features[7] > 160.50 and features[10] <= 1.50 and features[11] > 2.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] <= 3.50 and features[7] > 160.50 and features[10] > 1.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] <= 3.50 and features[7] > 160.50 and features[10] > 1.50 and features[8] > 0.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] > 3.50 and features[10] <= 1.50 and features[7] <= 160.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] > 3.50 and features[10] <= 1.50 and features[7] <= 160.50 and features[8] > 0.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] > 3.50 and features[10] <= 1.50 and features[7] > 160.50 and features[3] <= 127.00:
        votes_1 += 1
    if features[9] > 0.75 and features[2] > 3.50 and features[10] <= 1.50 and features[7] > 160.50 and features[3] > 127.00:
        votes_1 += 1
    if features[9] > 0.75 and features[2] > 3.50 and features[10] > 1.50 and features[7] <= 160.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] > 3.50 and features[10] > 1.50 and features[7] <= 160.50 and features[8] > 0.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] > 3.50 and features[10] > 1.50 and features[7] > 160.50 and features[8] <= 0.50:
        votes_1 += 1
    if features[9] > 0.75 and features[2] > 3.50 and features[10] > 1.50 and features[7] > 160.50 and features[8] > 0.50:
        votes_1 += 1
    total = votes_0 + votes_1
    if total == 0:
        return 0.9651
    return votes_1 / total


def predict(features):
    """Predict heart disease probability for a patient."""
    zone = assign_zone(features)
    zone_fn = {0: predict_zone_0, 1: predict_zone_1, 2: predict_zone_2, 3: predict_zone_3}
    return zone_fn.get(zone, lambda f: 0.5)(features)
