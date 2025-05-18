from bobleesj.utils.parsers.formula import Formula
from CAF.sort.custom import sort, convert_custom_labels_to_order_map
import pytest


def test_convert_custom_labels_to_order_map(custom_sort_labels, custom_sort_element_order_map):
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
def test_sort_with_custom_order(formula, expected_sorted_formula, custom_sort_element_order_map):
    element_count = Formula(formula).element_count
    element_order = custom_sort_element_order_map[element_count]
    actual_sorted_formula = sort(formula, element_order)
    assert actual_sorted_formula == expected_sorted_formula
