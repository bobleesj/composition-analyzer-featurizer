import numpy as np


def apply_transformations_to_features(features):
    """Apply various mathematical transformations to each feature value."""
    transformed_data = {}
    for feature_name, value in features.items():
        transformed_features = _transform_value(feature_name, value)
        transformed_data.update(transformed_features)
    return transformed_data


def _transform_value(feature_name, value):
    """Prepare a dictionary of functions for transforming the value."""
    transformations = {
        "exp": np.exp,
        "exp_neg": lambda x: np.exp(-x),
        "inverse": lambda x: 1 / x if x != 0 else float("inf"),
        "square": np.square,
        "cube": lambda x: x**3,
        "sqrt": np.sqrt,
        "cbrt": np.cbrt,
        "log": lambda x: np.log(x) if x > 0 else float("-inf"),
        "abs": np.abs,
        "sixth_power": lambda x: x**6,
        "sin": np.sin,
        "cos": np.cos,
    }

    data = {}
    for transform_name, transform_func in transformations.items():
        try:
            transformed_value = transform_func(value)
            data[f"{feature_name}_{transform_name}"] = transformed_value
        except Exception:
            data[f"{feature_name}_{transform_name}"] = None
    return data
