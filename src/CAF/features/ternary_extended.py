from bobleesj.utils import numbers
from bobleesj.utils.sources.oliynyk import Property as P
from numpy import mean

from CAF.features import ternary_helper as ter_helper
from CAF.features import transform


def generate_features(formula, db):
    data = {}
    data["formula"] = formula
    R, M, X, index_R, index_M, index_X, _, _, _ = (
        ter_helper.prepare_ternary_formula(formula)
    )
    indices = (index_R, index_M, index_X)
    for prop in P:
        prop = prop.value
        # Generate features for each property, like A+B, A-B, A*B, etc.
        prop_values = (db[R][prop], db[M][prop], db[X][prop])
        features = _transform_features_for_single_prop(
            prop, prop_values, indices
        )
        # For each feature, apply transformation
        transformed_features = transform.apply_transformations_to_features(
            features
        )
        data.update(transformed_features)
    return data


def _transform_features_for_single_prop(prop, prop_values, indices):
    R_prop_value, M_prop_value, X_prop_value = prop_values
    R_index, M_index, X_index = indices
    R_weighted = R_prop_value * R_index
    M_weighted = M_prop_value * M_index
    X_weighted = X_prop_value * X_index
    stats = numbers.calculate_basic_stats(prop_values)
    max_value = stats["max"]
    min_value = stats["min"]
    mid_value = stats["mid"]
    features = {
        f"{prop}_R": R_prop_value,
        f"{prop}_M": M_prop_value,
        f"{prop}_X": X_prop_value,
        f"{prop}_R+M": R_prop_value + M_prop_value,
        f"{prop}_M+X": M_prop_value + X_prop_value,
        f"{prop}_R+X": R_prop_value + X_prop_value,
        f"{prop}_R+M_weighted": R_weighted + M_weighted,
        f"{prop}_M+X_weighted": M_weighted + X_weighted,
        f"{prop}_R+X_weighted": R_weighted + X_weighted,
        f"{prop}_R-M": R_prop_value - M_prop_value,
        f"{prop}_M-X": M_prop_value - X_prop_value,
        f"{prop}_R-X": R_prop_value - X_prop_value,
        f"{prop}_R-M_weighted": R_weighted - M_weighted,
        f"{prop}_M-X_weighted": M_weighted - X_weighted,
        f"{prop}_R-X_weighted": R_weighted - X_weighted,
        f"{prop}_R/M": (
            R_prop_value / M_prop_value if M_prop_value != 0 else float("inf")
        ),
        f"{prop}_M/X": (
            M_prop_value / X_prop_value if X_prop_value != 0 else float("inf")
        ),
        f"{prop}_R/X": (
            R_prop_value / X_prop_value if X_prop_value != 0 else float("inf")
        ),
        f"{prop}_R/M_weighted": (
            R_weighted / M_weighted if M_weighted != 0 else float("inf")
        ),
        f"{prop}_M/X_weighted": (
            M_weighted / X_weighted if X_weighted != 0 else float("inf")
        ),
        f"{prop}_R/X_weighted": (
            R_weighted / X_weighted if X_weighted != 0 else float("inf")
        ),
        f"{prop}_RMX_avg": stats["avg"],
        f"{prop}_RM_avg": float(mean([R_prop_value, M_prop_value])),
        f"{prop}_MX_avg": float(mean([M_prop_value, X_prop_value])),
        f"{prop}_RX_avg": float(mean([R_prop_value, X_prop_value])),
        f"{prop}_max": max_value,
        f"{prop}_min": min_value,
        f"{prop}_max/min": max_value / min_value,
        f"{prop}_max-min": max_value - min_value,
        f"{prop}_max/mid": max_value / mid_value,
        f"{prop}_max-mid": max_value - mid_value,
        f"{prop}_mid/min": mid_value / min_value,
        f"{prop}_mid-min": mid_value - min_value,
        f"{prop}_std_dev": stats["std"],
        f"{prop}_variance": stats["var"],
    }
    return features
