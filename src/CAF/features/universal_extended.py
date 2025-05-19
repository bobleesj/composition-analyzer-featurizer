from bobleesj.utils import numbers
from bobleesj.utils.parsers.formula import Formula
from bobleesj.utils.sources.oliynyk import Property as P
from numpy import average

from CAF.features import transform


def generate_features(formula, db):
    data = {}
    data["formula"] = formula
    formula_obj = Formula(formula)
    elements = formula_obj.elements
    indices = formula_obj.indices
    # Generate a set of features for each property
    for prop in P:
        prop = prop.value
        prop_values = [db[element][prop] for element in elements]
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
    # Get normalized indices for universal features only.
    normalized_indices = [index / sum(indices) for index in indices]
    stats = numbers.calculate_basic_stats(prop_values)
    max_value = stats["max"]
    min_value = stats["min"]
    avg_value = stats["avg"]
    features = {
        f"{prop}_avg": avg_value,
        f"{prop}_avg_weighted_norm": float(
            average(prop_values, weights=normalized_indices)
        ),
        f"{prop}_max": max_value,
        f"{prop}_max_by_min": max_value / min_value,
        f"{prop}_min": min_value,
        f"{prop}_std_dev": stats["std"],
        f"{prop}_variance": stats["var"],
    }
    return features
