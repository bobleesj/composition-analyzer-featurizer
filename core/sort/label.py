from core.util import data, parser


def sort_formula_by_label(formula):
    num_elements = parser.get_num_element(formula)
    element_label_lists = data.get_element_label_lists(num_elements)
    sorted_formula = None

    if num_elements == 2:
        sorted_formula = sort_binary_formula_by_label(
            formula,
            element_label_lists,
            num_elements,
        )
    elif num_elements == 3:
        sorted_formula = sort_ternary_formula_by_label(
            formula,
            element_label_lists,
            num_elements,
        )

    return sorted_formula


def sort_binary_formula_by_label(formula, element_label_lists, num_elements):
    parsed_formulas_set = [list(item) for item in parser.get_parsed_formula(formula)]
    A_list, B_list = element_label_lists
    sorted_formulas = ""

    # Append the element label to the parsed formula
    for formula in parsed_formulas_set:
        parsed_element = formula[0]
        if parsed_element in A_list:
            formula.append("A")
        elif parsed_element in B_list:
            formula.append("B")
        else:
            formula.append("None")  # To handle elements not in A_list or B_list

    # Get "None" count
    none_element_label_count = parser.get_none_element_label_count(parsed_formulas_set)

    # Check whether they are the same
    is_same_element_label = parser.get_is_same_element_label(
        parsed_formulas_set, num_elements
    )

    # Handle when A-B, B-A
    if none_element_label_count == 0 and not is_same_element_label:
        sorted_formulas = sorted(
            parsed_formulas_set,
            key=lambda x: x[-1],
        )
        sorted_formula_string = "".join(
            [f"{formula[0]}{formula[1]}" for formula in sorted_formulas]
        )
        return sorted_formula_string

    # Handle when A-?, ?-B, ?-A, B-? (Containing 1 "None")
    if none_element_label_count == 1 and not is_same_element_label:
        first_formula = parsed_formulas_set[0]
        first_formula_label = first_formula[-1]

        second_formula = parsed_formulas_set[1]
        second_formula_label = second_formula[-1]

        first_formula_index_string = first_formula[0] + first_formula[1]
        second_formula_index_string = second_formula[0] + second_formula[1]

        # Binary case 3. A-? -> A-?
        if first_formula_label == "A" and second_formula_label == "None":
            return first_formula_index_string + second_formula_index_string

        # Binary case 4. B-? -> ?-B"
        if first_formula_label == "B" and second_formula_label == "None":
            return second_formula_index_string + first_formula_index_string

        # Binary case 5. ?-A -> A-?
        if first_formula_label == "None" and second_formula_label == "A":
            return second_formula_index_string + first_formula_index_string

        # "Binary case 6. ?-B -> ?-B
        if first_formula_label == "None" and second_formula_label == "B":
            return first_formula_index_string + second_formula_index_string

        # Binary case 7. A-A, B-B, ?-? (Containing 2 "None") using Mendeleev numbers
    if none_element_label_count == 2 or is_same_element_label:
        mendeleev_numbers = data.get_mendeleev_numbers(
            "data/element_Mendeleev_numbers.xlsx"
        )
        sorted_formulas = sorted(
            parsed_formulas_set,
            key=lambda x: mendeleev_numbers.get(x[0], float("inf")),
        )
        sorted_formula_string = "".join(
            [f"{formula[0]}{formula[1]}" for formula in sorted_formulas]
        )
        return sorted_formula_string

    sorted_formulas = sorted(parsed_formulas_set, key=lambda x: x[-1])

    return sorted_formula_string


# TERNARY STRUCTURE


def sort_ternary_formula_by_label(
    formula_tuple,
    element_label_lists,
    num_elements,
):
    # Assume 'parser.get_parsed_formula' is a method that extracts the formula correctly; simulating this:
    parsed_formulas_set = [
        list(item) for item in parser.get_parsed_formula(formula_tuple)
    ]
    R_list, M_list, X_list = element_label_lists

    # Append the correct label to each element, note correction in your condition checks
    for formula in parsed_formulas_set:
        parsed_element = formula[0]
        if parsed_element in R_list:
            formula.append("R")
        elif parsed_element in M_list:
            formula.append("M")
        elif parsed_element in X_list:
            formula.append("X")
        else:
            formula.append("None")  # Handle elements not in any specified list
    # Sort the list by the appended labels using a defined order map
    none_element_label_count = parser.get_none_element_label_count(parsed_formulas_set)

    order_map = {
        "R": 0,
        "M": 1,
        "X": 2,
        "None": 3,
    }
    sorted_formula_string = ""
    is_element_same = parser.get_is_same_element_label(
        parsed_formulas_set, num_elements
    )

    # Handle all R, M, X found
    # also handle when one of element label is not found
    if (
        none_element_label_count == 0 and not is_element_same
    ) or none_element_label_count == 1:
        sorted_formulas_set = sorted(
            parsed_formulas_set,
            key=lambda x: order_map[x[2]],
        )
        sorted_formula_string = "".join(
            [f"{element[0]}{element[1]}" for element in sorted_formulas_set]
        )
        return sorted_formula_string

    # Case 1: R(M,X)-?-? -> R(M,X)-?-?
    if none_element_label_count == 2 or is_element_same:
        mendeleev_numbers = data.get_mendeleev_numbers(
            "data/element_Mendeleev_numbers.xlsx"
        )
        sorted_formulas_set = sorted(
            parsed_formulas_set,
            key=lambda x: (
                order_map.get(x[2], float("inf")),
                mendeleev_numbers.get(x[0], float("inf")),
            ),
        )
        sorted_formula_string = "".join(
            [f"{element[0]}{element[1]}" for element in sorted_formulas_set]
        )

        return sorted_formula_string

    # Case 2: 2 elements from the same list (R-R-X, R-M-M, etc.)
    if num_elements == 3 and is_element_same:
        sorted_formulas_set = sorted(
            parsed_formulas_set,
            key=lambda x: (
                order_map[x[2]],
                mendeleev_numbers.get(x[0], float("inf")),
            ),
        )
        sorted_formula_string = "".join(
            [f"{element[0]}{element[1]}" for element in sorted_formulas_set]
        )

        return sorted_formula_string

    # Case 3: 3 elements from the same list (R-R-R, M-M-M, X-X-X)
    if num_elements == 3 and is_element_same:
        sorted_formulas_set = sorted(
            parsed_formulas_set,
            key=lambda x: (
                mendeleev_numbers.get(x[0], float("inf")),
                order_map[x[2]],
            ),
        )
        sorted_formula_string = "".join(
            [f"{element[0]}{element[1]}" for element in sorted_formulas_set]
        )

        return sorted_formula_string

    # Case 4: 3 missing elements (?-?-?)
    if none_element_label_count == 3:
        sorted_formulas_set = sorted(
            parsed_formulas_set,
            key=lambda x: mendeleev_numbers.get(x[0], float("inf")),
        )
        sorted_formula_string = "".join(
            [f"{element[0]}{element[1]}" for element in sorted_formulas_set]
        )

        return sorted_formula_string


def sort_formula(formula):
    num_elements = parser.get_num_element(formula)
    element_label_lists = data.get_element_label_lists(num_elements)
    sorted_formula = None

    if num_elements == 2:
        sorted_formula = sort_binary_formula_by_label(
            formula,
            element_label_lists,
            num_elements,
        )

    if num_elements == 3:
        sorted_formula = sort_ternary_formula_by_label(
            formula,
            element_label_lists,
            num_elements,
        )

    # print(formula, "->", sorted_formula)
    return sorted_formula
