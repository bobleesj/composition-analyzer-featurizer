import pandas as pd


def get_element_label_lists(num_elements):
    # Define the appropriate lists of elements based on the structure type
    if num_elements == 2:
        df = pd.read_excel(
            "data/label.xlsx", sheet_name="Binary", engine="openpyxl"
        )

        # Assuming the first column is 'Element_A' and the second is 'Element_B'
        A_list = df["Element_A"].dropna().tolist()
        B_list = df["Element_B"].dropna().tolist()

        return A_list, B_list

    if num_elements == 3:
        df = pd.read_excel(
            "data/label.xlsx", sheet_name="Ternary", engine="openpyxl"
        )

        R_list = df["Element_R"].dropna().tolist()
        M_list = df["Element_M"].dropna().tolist()
        X_list = df["Element_X"].dropna().tolist()

        return R_list, M_list, X_list


def get_mendeleev_numbers(data):
    data = "data/element_Mendeleev_numbers.xlsx"
    df = pd.read_excel(data, header=None)
    elements = df.iloc[:, 0]  # Assuming elements are in the first column
    mendeleev_numbers = df.iloc[
        :, 1
    ]  # Assuming Mendeleev numbers are in the 6th column
    return dict(zip(elements, mendeleev_numbers))


def get_element_property_values(data, element_col_num):
    data = "data/element_properties_for_ML.xlsx"
    df = pd.read_excel(data, header=None, engine="openpyxl")
    elements = df.iloc[:, 0]  # Assuming elements are in the first column
    property_values = df.iloc[
        :, element_col_num
    ]  # Choose the property (by default Mendeleev number)
    return dict(zip(elements, property_values))
