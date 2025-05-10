import pandas as pd

from core.sort import index, label, property
from core.util import parser


def get_sorted_formula_df_by_label(df):
    sorted_formulas = []
    for formula in df["Formula"]:
        sorted_formula = label.sort_formula_by_label(formula)
        num_elements = parser.get_num_element(sorted_formula)
        sorted_formulas.append(
            {
                "Formula": sorted_formula,
                "Old formula": formula,
                "Number of elements": num_elements,
            }
        )
    return pd.DataFrame(sorted_formulas)


def get_sorted_formula_df_by_index(
    formulas_df, is_ascending_order, is_indices_as_fractions
):
    # Demical places for the fractions
    demical_places = 2
    sorted_formulas = []

    # Normalize each index by the total index sum
    if is_indices_as_fractions:
        for formula in formulas_df["Formula"]:
            index_sum = 0
            normalized_formula_parts = []
            parsed_formula_set = parser.get_parsed_formula(formula)

            # Calculate the sum of all indices
            for element, element_index in parsed_formula_set:
                if element_index == "":
                    index_sum += 1  # Treat missing indices as 1
                else:
                    index_sum += float(element_index)

            for element, element_index in parsed_formula_set:
                if element_index == "":
                    normalized_index = 1 / index_sum
                else:
                    normalized_index = float(element_index) / index_sum

                normalized_formula_parts.append(
                    f"{element}{normalized_index:.{demical_places}f}"
                )

            # Join all parts into one string for the normalized formula
            normalized_formula_str = "".join(normalized_formula_parts)
            sorted_formula = index.sort_formula_by_index(
                normalized_formula_str, is_ascending_order
            )
            num_elements = parser.get_num_element(sorted_formula)
            sorted_formulas.append(
                {
                    "Formula": sorted_formula,
                    "Old formula": formula,
                    "Number of elements": num_elements,
                }
            )
    if not is_indices_as_fractions:
        for formula in formulas_df["Formula"]:
            num_elements = parser.get_num_element(formula)
            sorted_formula = index.sort_formula_by_index(formula, is_ascending_order)
            sorted_formulas.append(
                {
                    "Formula": sorted_formula,
                    "Old formula": formula,
                    "Number of elements": num_elements,
                }
            )

    # Create and return a DataFrame with a single "Formula" column
    return pd.DataFrame(sorted_formulas)


def get_sorted_formula_df_by_property(formulas_df, is_ascending_order, element_col_num):
    sorted_formulas = []
    for formula in formulas_df["Formula"]:
        num_elements = parser.get_num_element(formula)
        sorted_formula = property.sort_formula_by_selected_property(
            formula,
            num_elements,
            is_ascending_order,
            element_col_num,
        )

        sorted_formulas.append(
            {
                "Formula": sorted_formula,
                "Old formula": formula,
                "Number of elements": num_elements,
            }
        )
    sorted_formulas_df = pd.DataFrame(sorted_formulas)
    return sorted_formulas_df


def get_parsed_formula_df(df, is_parse_option=False):
    max_elements = 0
    parsed_formulas = []

    # Parse each formula and find the maximum number of elements in any formula
    for formula in df["Formula"]:
        parsed_formula = parser.get_parsed_formula(formula)
        max_elements = max(max_elements, len(parsed_formula))
        parsed_formulas.append(parsed_formula)

    # Define new columns for the DataFrame based on the maximum elements found

    if not is_parse_option:
        column_names = [
            "Formula",
            "Old formula",
            "Number of elements",
        ]  # Keep the original columns
        for i in range(1, max_elements + 1):
            column_names.extend([f"Element {i}", f"Index {i}"])

        # Create a new DataFrame to store all the data
        new_data = []
        for (formula, old_formula, num_elements), parsed in zip(
            df[["Formula", "Old formula", "Number of elements"]].values,
            parsed_formulas,
        ):
            row = [
                formula,
                old_formula,
                num_elements,
            ]  # Start with existing data
            for element, idx in parsed:
                # If index is empty, assume it is 1
                idx = idx if idx else "1"
                row.extend([element, float(idx)])
            # Fill remaining cells if this row has fewer elements than max_elements
            row.extend([None] * (2 * max_elements - len(row) + 3))
            new_data.append(row)

        parsed_df = pd.DataFrame(new_data, columns=column_names)
        return parsed_df

    if is_parse_option:
        max_elements = 0
        parsed_formulas = []

        # Parse formulas and find the maximum number of elements
        for formula in df["Formula"]:
            parsed_formula = parser.get_parsed_formula(formula)
            num_elements = parser.get_num_element(formula)
            max_elements = max(max_elements, num_elements)
            parsed_formulas.append((parsed_formula, num_elements))

        # Initialize column names with 'Formula' and 'Number of elements'
        column_names = ["Formula", "Number of elements"]
        # Add columns dynamically based on the maximum number of elements found
        for i in range(1, max_elements + 1):
            column_names.extend([f"Element {i}", f"Index {i}"])

        # Create a new DataFrame to store all the data
        new_data = []
        for formula, (parsed, num_elements) in zip(df["Formula"], parsed_formulas):
            # Start with the formula data and the number of elements
            row = [
                formula,
                num_elements,
            ]  # Include the number of elements in each formula
            for element, idx in parsed:
                idx = idx if idx else "1"  # If index is empty, assume it is 1
                row.extend([element, float(index)])
            # Fill remaining cells if this row has fewer elements than max_elements
            row.extend([None] * (2 * (max_elements - num_elements)))
            new_data.append(row)

        parsed_df = pd.DataFrame(new_data, columns=column_names)
        return parsed_df
