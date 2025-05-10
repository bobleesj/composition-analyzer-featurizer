import pandas as pd

from core.util import parser


def get_element_list():
    elements_file_path = "data/element_Mendeleev_numbers.xlsx"
    elements_df = pd.read_excel(elements_file_path, header=None)
    element_list = elements_df[0].tolist()
    return element_list


def add_encoding_to_df(df, formulas, is_all_element_displayed):
    """
    Adds normalized compositional one-hot encoding to an existing df.
    Drops columns with all zeros if is_all_element_displayed is False.
    """
    # Initialize a temporary DataFrame to store the encoding vectors
    element_list = get_element_list()
    encoding_df = pd.DataFrame(columns=element_list)
    # Process each formula in the DataFrame
    for formula in formulas:
        normalized_formula = parser.get_normalized_formula(formula)
        normalized_parsed_formula = parser.get_parsed_formula(normalized_formula)

        # Create an encoding vector initialized with zeros
        encoding = {element: 0 for element in element_list}

        # Populate the vector with normalized values for elements
        for element, value in normalized_parsed_formula:
            if element in encoding:
                encoding[element] = float(
                    value
                )  # ensure the value is a float, if necessary

        # Create a DataFrame from the encoding dictionary
        new_row = pd.DataFrame([encoding])

        # Append the new row to the temporary encoding DataFrame
        encoding_df = pd.concat([encoding_df, new_row], ignore_index=True)

    # Concatenate the original DataFrame with the encoding DataFrame
    df_combined = pd.concat([df, encoding_df], axis=1)

    # Conditionally drop columns with all zeros if required
    if not is_all_element_displayed:
        df_combined = df_combined.loc[:, (df_combined != 0).any(axis=0)]

    return df_combined
