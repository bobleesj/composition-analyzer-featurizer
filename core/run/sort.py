import os

import pandas as pd

from core.sort import sort_df_handler
from core.util import data, folder, prompt


def run_sort_option(script_dir_path):
    prompt.print_sort_option()
    sort_method = prompt.choose_sort_method()
    sorted_formulas_df = None
    is_ascending_order = None
    suffix = None
    formula_excel_path = None
    is_formula_parsed_columns_added = True

    if sort_method in [1, 2, 3, 4]:
        formula_excel_path = folder.list_xlsx_files_with_formula(script_dir_path)
        if formula_excel_path:
            print(f"Selected Excel file: {formula_excel_path}")

    # list Excel files containing excel files and starts with "formula"
    directory, base_name = os.path.split(formula_excel_path)
    base_name_no_ext = os.path.splitext(base_name)[0]
    df = pd.read_excel(formula_excel_path)

    if "Formula" not in df.columns:
        raise ValueError("The Excel file does not contain a 'Formula' column.")
    # Drop all except "Formual" column
    df = df[["Formula"]]

    # Sort by label
    if sort_method == 1:
        is_formula_parsed_columns_added = prompt.get_is_formula_parsed_columns_added()
        sorted_formulas_df = sort_df_handler.get_sorted_formula_df_by_label(df)
        suffix = "by_label"
        A_list, B_list = data.get_element_label_lists(2)
        R_list, M_list, X_list = data.get_element_label_lists(3)

        A_list, B_list = data.get_element_label_lists(2)
        print("Binary formulas are sorted into A-B based on:")
        print("  - A:", ", ".join(A_list))
        print("  - B:", ", ".join(B_list))

        R_list, M_list, X_list = data.get_element_label_lists(3)
        print("\nTernary formulas are sorted into R-M-X based on:")
        print("  - R:", ", ".join(R_list))
        print("  - M:", ", ".join(M_list))
        print("  - X:", ", ".join(X_list))

        print(
            "\nNote: you may modify the columns in data/label.xlsx"
            " to add or remove pre-defined elements.\n"
        )

    # Sort by index
    if sort_method == 2:
        # Ask whether to sort by ascending order
        is_ascending_order = prompt.get_is_ascending_order()

        # Ask whether to convert indices into fractions
        is_indices_as_fractions = prompt.get_is_indices_as_fractions()

        # Ask whether to include parsed columns
        is_formula_parsed_columns_added = prompt.get_is_formula_parsed_columns_added()
        # Sort
        sorted_formulas_df = sort_df_handler.get_sorted_formula_df_by_index(
            df, is_ascending_order, is_indices_as_fractions
        )

        suffix = "by_index"
        print("Elements with the same index are sorted by Mendeleev number.")

    # Sort by property
    if sort_method == 3:
        element_col_num = prompt.get_element_col_num_after_printing()
        is_ascending_order = prompt.get_is_ascending_order()
        is_formula_parsed_columns_added = prompt.get_is_formula_parsed_columns_added()
        sorted_formulas_df = sort_df_handler.get_sorted_formula_df_by_property(
            df, is_ascending_order, element_col_num
        )
        suffix = "by_property"

    # Parse the elements without sorting
    if sort_method == 4:
        suffix = "parsed"
        is_parse_option = True
        sorted_formulas_df = sort_df_handler.get_parsed_formula_df(df, is_parse_option)

    # Save the sorted DataFrame to a new Excel file
    sorted_output_path = os.path.join(directory, f"{base_name_no_ext}_{suffix}.xlsx")

    # If Option 4 (parse), save and exit early
    if sort_method == 4:
        sorted_formulas_df.index = sorted_formulas_df.index + 1
        print(sorted_formulas_df.head(20))
        sorted_formulas_df.to_excel(sorted_output_path, index=False)
        print(f"Finished. Data saved to {sorted_output_path}")
        return

    # If Option 1-3 and the user wants simple output with "Formula"
    if not is_formula_parsed_columns_added:
        sorted_formulas_df = sorted_formulas_df[["Formula"]]
        sorted_formulas_df.index = sorted_formulas_df.index + 1
        print(sorted_formulas_df.head(20))
        sorted_formulas_df.to_excel(sorted_output_path, index=False)

    # If Option 1-3 and the user wants verbose output
    else:
        sorted_formulas_df_with_parsed_formula = sort_df_handler.get_parsed_formula_df(
            sorted_formulas_df
        )
        sorted_formulas_df_with_parsed_formula.to_excel(sorted_output_path, index=False)
        sorted_formulas_df_with_parsed_formula.index = (
            sorted_formulas_df_with_parsed_formula.index + 1
        )
        print(sorted_formulas_df_with_parsed_formula.head(20))

    print(f"Finished. Data saved to {sorted_output_path}")
