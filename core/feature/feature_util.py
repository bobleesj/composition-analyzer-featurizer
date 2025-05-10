import os

import pandas as pd

from core.util import parser


def get_property_df_data():
    property_excel_path = "data/element_properties_for_ML.xlsx"
    property_df = pd.read_excel(property_excel_path)
    property_data = property_df.set_index("symbol").to_dict(orient="index")
    # Drop the first column of "symbol"
    property_df.drop(property_df.columns[0], axis=1, inplace=True)

    # Drop the last five columns for features
    property_df = property_df.iloc[:, :-5]
    return property_df, property_data


def get_unsorted_df(sorted_df):
    columns_to_drop = [
        col for col in sorted_df.columns if col.endswith("element_value")
    ]
    unsorted_df = sorted_df.drop(columns=columns_to_drop)
    return unsorted_df


def merge_df_with_same_columns(binary_df, ternary_df):
    # Ensure both dataframes have the same columns
    if set(binary_df.columns) == set(ternary_df.columns):
        # Concatenate dataframes
        merged_df = pd.concat([binary_df, ternary_df], ignore_index=True)
        return merged_df
    else:
        raise ValueError("DataFrames do not have the same columns")


def get_binary_ternary_formulas(formulas):
    binary_formulas = []
    ternary_formulas = []

    for formula in formulas:
        num_elements = parser.get_num_element(formula)
        if num_elements == 2:
            binary_formulas.append(formula)
        elif num_elements == 3:
            ternary_formulas.append(formula)
    return binary_formulas, ternary_formulas


def get_output_paths(directory, base_name_no_ext, file_format):
    binary_output_path = os.path.join(
        directory, f"{base_name_no_ext}_features_binary.{file_format}"
    )
    ternary_output_path = os.path.join(
        directory, f"{base_name_no_ext}_features_ternary.{file_format}"
    )

    univeral_sorted_output_path = os.path.join(
        directory,
        f"{base_name_no_ext}_features_universal_sorted.{file_format}",
    )

    univeral_unsorted_output_path = os.path.join(
        directory,
        f"{base_name_no_ext}_features_universal_unsorted.{file_format}",
    )

    return (
        binary_output_path,
        ternary_output_path,
        univeral_sorted_output_path,
        univeral_unsorted_output_path,
    )


def round_dataframes(dfs):
    precision = 3
    return [df.round(precision) for df in dfs]
