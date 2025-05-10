import numpy as np
import pandas as pd

from core.feature import feature_util
from core.util import parser


def generate_univeral_features(df):
    property_excel_path = "data/element_properties_for_ML.xlsx"

    # Read property Excel file
    property_df = pd.read_excel(property_excel_path)
    property_data = property_df.set_index("symbol").to_dict(orient="index")

    # Drop the first column of "Symbol"
    property_df.drop(property_df.columns[0], axis=1, inplace=True)

    # Drop the last five columns for uni features
    property_df = property_df.iloc[:, :-5]

    # Generate universal features
    (
        universal_sorted_df,
        universal_unsorted_df,
    ) = get_universal_featurized_df(property_df, df["Formula"], property_data)
    return universal_sorted_df, universal_unsorted_df


def get_universal_feature_entry_values(
    parsed_normalized_formula, property_data, property
):
    precision = 3
    element_list = [x[0] for x in parsed_normalized_formula]
    normalized_index_list = [float(x[1]) for x in parsed_normalized_formula]
    value_list = np.array(
        [
            property_data[element][property]
            for element in element_list
            if element in property_data
        ]
    )

    # Combine normalized index
    avg_weighted_norm = np.average(value_list, weights=normalized_index_list)
    avg = value_list.mean()
    max = value_list.max()
    min = value_list.min()
    max_by_min = max / min
    first_element_value = value_list[0]
    last_element_value = value_list[-1]

    value_dict = {
        f"{property}_avg_weighted_norm": round(avg_weighted_norm, precision),
        f"{property}_avg": round(avg, precision),
        f"{property}_max": round(max, precision),
        f"{property}_min": round(min, precision),
        f"{property}_max_by_min": round(max_by_min, precision),
        f"{property}_first_element_value": round(first_element_value, precision),
        f"{property}_last_element_value": round(last_element_value, precision),
    }
    return value_dict


def get_universal_featurized_df(property_df, formulas, property_data):
    data = []
    # Loop through each formula and calculate features
    for formula in formulas:
        normalized_formula = parser.get_normalized_formula(formula)
        parsed_normalized_formula = parser.get_parsed_formula(normalized_formula)
        normalized_index_list = np.array(
            [float(x[1]) for x in parsed_normalized_formula]
        )
        feature_dict = {formula: {}}

        for column_name in property_df.columns:
            value_dict = get_universal_feature_entry_values(
                parsed_normalized_formula, property_data, column_name
            )
            feature_dict[formula][column_name] = value_dict

        # Flatten the dictionary
        for formula, properties in feature_dict.items():
            row = {"Formula": formula}

            row.update(
                {
                    "first_element_normalized_index": normalized_index_list[0],
                    "last_element_normalized_index": normalized_index_list[-1],
                    "max_normalized_index": normalized_index_list.max(),
                    "min_normalized_index": normalized_index_list.min(),
                    "num_element": parser.get_num_element(formula),
                }
            )
            for _, metrics in properties.items():
                row.update(metrics)
            data.append(row)

    # Create DataFrame outside the loop
    sorted_df = pd.DataFrame(data)
    unsorted_df = feature_util.get_unsorted_df(sorted_df)

    return sorted_df, unsorted_df
