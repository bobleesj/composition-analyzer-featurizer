import re

import pandas as pd

from core.util import data, parser


def sort_formula_by_index(formula, is_smallest_to_largest):
    # Check whether to sort by index or Mendeeleve
    is_sorted_by_index = decide_sorting_method(formula)
    sorted_formula = None

    if is_sorted_by_index:
        if is_smallest_to_largest:
            sorted_formula = sort_by_index(
                formula,
                is_smallest_to_largest=True,
            )
        else:
            sorted_formula = sort_by_index(
                formula,
                is_smallest_to_largest=False,
            )

    mendeleev_file = "data/element_Mendeleev_numbers.xlsx"
    mendeleev_numbers = load_mendeleev_numbers(mendeleev_file)
    # Use Mendeeleeve to sort
    if not is_sorted_by_index:
        sorted_formula = sort_by_mendeleev(formula, mendeleev_numbers)

    return sorted_formula


def load_mendeleev_numbers(filepath):
    df = pd.read_excel(
        filepath,
        header=None,
        names=["Element", "MendeleevNumber"],
    )
    return dict(zip(df["Element"], df["MendeleevNumber"]))


def get_parsed_formula(formula):
    pattern = r"([A-Z][a-z]*)(\d*\.?\d*)"
    matches = re.findall(pattern, formula)
    parsed_formula = []
    for element, index in matches:
        if index == "":
            index = 1
        else:
            index = float(index) if "." in index else int(index)
        parsed_formula.append((element, index))
    return parsed_formula


def sort_by_index(formula, is_smallest_to_largest):
    # Parse the formula
    parsed_formula = get_parsed_formula(formula)

    # Sort by index values smallest to largest
    sorted_smallest_to_largest = sorted(parsed_formula, key=lambda x: x[1])
    # Sort by index values largest to smallest
    sorted_largest_to_smallest = sorted(
        parsed_formula,
        key=lambda x: x[1],
        reverse=True,
    )

    # Convert tuples back to formula string, omitting '1' for indices
    smallest_to_largest = "".join(
        [
            f"{elem}{'' if idx == 1 else int(idx) if isinstance(idx, int) else idx}"
            for elem, idx in sorted_smallest_to_largest
        ]
    )
    largest_to_smallest = "".join(
        [
            f"{elem}{'' if idx == 1 else int(idx) if isinstance(idx, int) else idx}"
            for elem, idx in sorted_largest_to_smallest
        ]
    )

    if is_smallest_to_largest:
        return smallest_to_largest
    else:
        return largest_to_smallest


def sort_by_mendeleev(formula, mendeleev_numbers):
    mendeleev_numbers = data.get_mendeleev_numbers(
        "data/element_Mendeleev_numbers.xlsx"
    )
    parsed_formulas_set = [list(item) for item in parser.get_parsed_formula(formula)]

    sorted_formulas_set = sorted(
        parsed_formulas_set,
        key=lambda x: (mendeleev_numbers.get(x[0], float("inf")),),
    )
    sorted_formula_string = "".join(
        [
            f"{element[0]}{'' if element[1] == 1 else element[1]}"
            for element in sorted_formulas_set
        ]
    )
    return sorted_formula_string


def decide_sorting_method(formula):
    parsed_formula = get_parsed_formula(formula)
    indices = [idx for _, idx in parsed_formula]
    is_sorted_by_index = len(set(indices)) == len(indices)
    return is_sorted_by_index
