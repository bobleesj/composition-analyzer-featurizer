import pytest
from bobleesj.utils.parsers.formula import Formula

from CAF.sort.custom import (
    convert_custom_labels_to_order_map,
    get_custom_labels_from_excel,
    sort,
)


def test_convert_custom_labels_to_order_map(
    custom_sort_labels, custom_sort_element_order_map
):
    actual_output = convert_custom_labels_to_order_map(custom_sort_labels)
    assert actual_output == custom_sort_element_order_map


@pytest.mark.parametrize(
    "formula,expected_sorted_formula",
    [
        ("BLi", "LiB"),
        ("InEr", "ErIn"),
        ("CoErIn", "ErCoIn"),
        ("UInErCo", "ErCoInU"),
    ],
)
def test_sort_with_custom_order(
    formula, expected_sorted_formula, custom_sort_element_order_map
):
    element_count = Formula(formula).element_count
    element_order = custom_sort_element_order_map[element_count]
    actual_sorted_formula = sort(formula, element_order)
    assert actual_sorted_formula == expected_sorted_formula


def test_get_custom_labels_from_excel():
    # Assuming the Excel file is structured correctly and the path is valid
    excel_path = "tests/data/sort/test-custom-labels.xlsx"
    custom_labels = get_custom_labels_from_excel(excel_path)

    expected_labels = {
        2: {
            "A": ["Fe", "Co", "Ni", "Ru", "Rh", "Pd", "Os", "Ir", "Pt"],
            "B": ["Si", "Ga", "Ge", "In", "Sn", "Sb"],
        },
        3: {
            "R": [
                "Sc",
                "Y",
                "La",
                "Ce",
                "Py",
                "Nd",
                "Pm",
                "Sm",
                "Eu",
                "Gd",
                "Tb",
                "Dy",
                "Ho",
                "Er",
                "Tm",
                "Yb",
                "Lu",
                "Th",
                "U",
            ],
            "M": ["Fe", "Co", "Ni", "Ru", "Rh", "Pd", "Os", "Ir", "Pt"],
            "X": ["Si", "Ga", "Ge", "In", "Sn", "Sb"],
        },
        4: {
            "A": ["Sc", "Y", "La", "Ce", "Py", "Pm", "Sm", "Eu"],
            "B": ["Fe", "Co", "Ni", "Ru", "Rh", "Pd", "Os", "Ir", "Pt", "Nd"],
            "C": ["Si", "Ga", "Ge", "In", "Sn", "Sb"],
            "D": ["Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Th", "U"],
        },
    }

    assert custom_labels == expected_labels
