import os
import warnings
import click
import pandas as pd
from core.util import folder
from CAF.features import generator

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

    add_extended_features = click.confirm(
        "\nDo you want to save additional files containing features with"
        "\nmathematical operations? Ex) +, -, *, /, exp, square, cube, etc."
        "\n(Default is N)",
        default=False,
    )
    
    generator.get_composition_features(formulas, extended_features=add_extended_features, file_prefix=base_name_no_ext)
