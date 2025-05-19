import os

import pandas as pd

from app.util import folder, prompt
from CAF.sort import custom
from app.runners import sort_handler

def run_sort_option(script_dir_path):
    sort_method = prompt.choose_sort_method()
    if sort_method in [1, 2, 3, 4]:
        formula_excel_path = folder.list_xlsx_files_with_formula(script_dir_path)
        if formula_excel_path:
            print(f"You've selected: {formula_excel_path}")
    directory, base_name = os.path.split(formula_excel_path)
    base_name_no_ext = os.path.splitext(base_name)[0]
    df = pd.read_excel(formula_excel_path)

    # Sort by custom label
    if sort_method == 1:
        _prompt_custom_labels()
        
        
        
        
    # Sort by index
    # if sort_method == 2:
    #     # Ask whether to sort by ascending order

    #     is_ascending_order = prompt.ascend_order()
    #     is_normalized = prompt.normalize_formula()
    #     is_formula_parsed_columns_added = prompt.get_is_formula_parsed_columns_added()
    #     suffix = "by_index"
    #     print("Elements with the same index are sorted by Mendeleev number.")

    # # Sort by property
    # if sort_method == 3:
    #     element_col_num = prompt.get_element_col_num_after_printing()
    #     is_ascending_order = prompt.ascend_order()
        

    # A_list, B_list = data.get_element_label_lists(2)
    # print("Binary formulas are sorted into A-B based on:")
    # print("  - A:", ", ".join(A_list))
    # print("  - B:", ", ".join(B_list))

    # R_list, M_list, X_list = data.get_element_label_lists(3)
    # print("\nTernary formulas are sorted into R-M-X based on:")
    # print("  - R:", ", ".join(R_list))
    # print("  - M:", ", ".join(M_list))
    # print("  - X:", ", ".join(X_list))

    # A_list, B_list, C_list, D_list = data.get_element_label_lists(4)
    # print("\nQuaternary formulas are sorted into A-B-C-D based on:")
    # print("  - A:", ", ".join(A_list))
    # print("  - B:", ", ".join(B_list))
    # print("  - C:", ", ".join(C_list))
    # print("  - D:", ", ".join(D_list))
    
    # print(
    #     "\nNote: you may modify the custom labels in data/sort/custom-labels.xlsx"
    #     " to add or remove pre-defined elements.\n"
    # )
