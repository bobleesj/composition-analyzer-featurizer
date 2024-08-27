import os
import warnings

import click
import pandas as pd

from core.feature import (
    binary,
    binary_long,
    encoding,
    feature_handler,
    feature_util,
    ternary,
    ternary_long,
    universal,
    universal_long,
)
from core.util import folder

"""
Ignore warnings for Pandas
"""
warnings.simplefilter("ignore")


def run_feature_option(script_dir_path):
    # User select the Excel file
    formula_excel_path = folder.list_xlsx_files_with_formula(script_dir_path)
    if formula_excel_path:
        print(f"Selected Excel file: {formula_excel_path}")

    # list Excel files containing excel files and starts with "formula"
    directory, base_name = os.path.split(formula_excel_path)
    base_name_no_ext = os.path.splitext(base_name)[0]
    df = pd.read_excel(formula_excel_path)
    formulas = df["Formula"]

    # User select whether to add normalized compositional one-hot encoding
    is_encoding_added = click.confirm(
        "\nDo you want to include normalized composition vector? (Default is N)",
        default=False,
    )

    if is_encoding_added:
        is_all_element_displayed = click.confirm(
            "\nDo you want to include all elements in the composition vector or"
            " only the ones present in the dataset? (Default is Y)",
            default=True,
        )

    is_long_features_saved = click.confirm(
        "\nDo you want to save additional files containing features with"
        "\nmathematical operations? Ex) +, -, *, /, exp, square, cube, etc."
        "\n(Default is N)",
        default=False,
    )

    is_csv_saved = click.confirm(
        "\nDo you want to save the outputs as .csv files? If not, .xlsx is used. (Default is Y)",
        default=True,
    )

    # Parse binary and ternary formulas
    (
        binary_formulas,
        ternary_formulas,
    ) = feature_util.get_binary_ternary_formulas(formulas)

    # Save long features
    if is_long_features_saved and binary_formulas:
        feature_handler.save_long_features(
            binary_formulas,
            binary_long,
            f"{base_name_no_ext}_long_features_binary",
        )
    if is_long_features_saved and ternary_formulas:
        feature_handler.save_long_features(
            ternary_formulas,
            ternary_long,
            f"{base_name_no_ext}_long_features_ternary",
        )
    if is_long_features_saved:
        feature_handler.save_long_features(
            formulas,
            universal_long,
            f"{base_name_no_ext}_long_features_universal",
        )

    # Split formulas into binary and ternary
    binary_df = binary.generate_binary_features(binary_formulas)
    ternary_df = ternary.generate_ternary_features(ternary_formulas)
    (
        universal_sorted_df,
        universal_unsorted_df,
    ) = universal.generate_univeral_features(df)

    # Add encoding
    if is_encoding_added:
        binary_df = encoding.add_encoding_to_df(
            binary_df, binary_formulas, is_all_element_displayed
        )
        ternary_df = encoding.add_encoding_to_df(
            ternary_df, ternary_formulas, is_all_element_displayed
        )
        universal_sorted_df = encoding.add_encoding_to_df(
            universal_sorted_df,
            formulas,
            is_all_element_displayed,
        )
        universal_unsorted_df = encoding.add_encoding_to_df(
            universal_unsorted_df,
            formulas,
            is_all_element_displayed,
        )

    # Round df
    dfs = [
        binary_df,
        ternary_df,
        universal_sorted_df,
        universal_unsorted_df,
    ]
    (
        binary_df,
        ternary_df,
        universal_sorted_df,
        universal_unsorted_df,
    ) = feature_util.round_dataframes(dfs)

    if is_csv_saved:
        file_format = "csv"
    else:
        file_format = "xlsx"

    # Save Excel files
    feature_handler.save_dataframes(
        binary_df,
        ternary_df,
        universal_sorted_df,
        universal_unsorted_df,
        directory,
        base_name_no_ext,
        file_format,
    )
