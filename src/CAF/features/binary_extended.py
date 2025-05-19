from bobleesj.utils import numbers
from bobleesj.utils.sources.oliynyk import Property as P

from CAF.features import binary_helper as bi_helper
from CAF.features import transform


def generate_features(formula, db):
    data = {}
    data["formula"] = formula
    A, B, index_A, index_B, _, _ = bi_helper.prepare_binary_formula(formula)
    indices = (index_A, index_B)
    for prop in P:
        prop = prop.value
        # Generate features for each property, like A+B, A-B, A*B, etc.
        prop_values = (db[A][prop], db[B][prop])
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
    # Handling binary values specifically
    A_prop_value, B_prop_value = prop_values
    A_index, B_index = indices
    stats = numbers.calculate_basic_stats(prop_values)
    A_weighted = A_prop_value * A_index
    B_weighted = B_prop_value * B_index
    features = {
        f"{prop}_A": A_prop_value,
        f"{prop}_B": B_prop_value,
        f"{prop}_A+B": A_prop_value + B_prop_value,
        f"{prop}_A+B_weighted": A_weighted + B_weighted,
        f"{prop}_A-B": A_prop_value - B_prop_value,
        f"{prop}_A-B_weighted": A_weighted - B_weighted,
        f"{prop}_A*B": A_prop_value * B_prop_value,
        f"{prop}_A*B_weighted": A_weighted * B_weighted,
        f"{prop}_A/B": (
            A_prop_value / B_prop_value if B_prop_value != 0 else float("inf")
        ),
        f"{prop}_A/B_weighted": (
            A_weighted / B_weighted if B_weighted != 0 else float("inf")
        ),
        f"{prop}_avg": stats["avg"],
        f"{prop}_max": stats["max"],
        f"{prop}_min": stats["min"],
        f"{prop}_std_dev": stats["std"],
        f"{prop}_variance": stats["var"],
    }
    return features
