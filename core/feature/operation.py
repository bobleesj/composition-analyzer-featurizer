import numpy as np

from core.feature import operation
from core.util import parser


def apply_operation(value, property_name, precision):
    # Define a dictionary with all required transformations
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

    # Apply each transformation to the input value
    results = {}
    for transform_name, transform_func in transformations.items():
        try:
            transformed_value = transform_func(value)
            results[f"{property_name}_{transform_name}"] = round(
                transformed_value, precision
            )
        except Exception as e:
            # Handle any mathematical errors like overflows or domain errors
            results[f"{property_name}_{transform_name}"] = None
            print(f"Error applying {transform_name} on {value}: {e}")

    return results


def get_feature_entry_values(formula, property_data, property_name, function):
    normalized_formula = parser.get_normalized_formula(formula)
    parsed_formula = parser.get_parsed_formula(formula)
    parsed_normalized_formula = parser.get_parsed_formula(normalized_formula)
    element_list = [x[0] for x in parsed_normalized_formula]

    # Get index
    index_list = [float(x[1]) if x[1] != "" else 1.0 for x in parsed_formula]
    normalized_index_list = [float(x[1]) for x in parsed_normalized_formula]
    precision = 3

    value_list = np.array(
        [
            property_data[element][property_name]
            for element in element_list
            if element in property_data
        ]
    )

    stats = function.calculate_stats(value_list, index_list, normalized_index_list)

    value_dict = {}

    # Apply transforamtion
    for stat_name, stat_value in stats.items():
        value_dict[f"{property_name}_{stat_name}"] = round(stat_value, precision)
        value_dict.update(
            operation.apply_operation(
                stat_value, f"{property_name}_{stat_name}", precision
            )
        )

    return value_dict
