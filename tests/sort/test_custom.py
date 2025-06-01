import pytest

from CAF.sort.custom import (
    _convert_custom_labels_to_order_map,
    get_custom_labels_from_excel,
    sort,
)


def test_get_custom_labels_from_excel(custom_label_excel_path):
    actual_custom_label = get_custom_labels_from_excel(custom_label_excel_path)
    assert actual_custom_label == {
        2: {"A": ["Fe", "Co", "Ni"], "B": ["Si", "Ga", "Ge"]},
        3: {
            "R": ["Sc", "Y", "La"],
            "M": ["Fe", "Co", "Ni"],
            "X": ["Si", "Ga", "Ge"],
        },
        4: {
            "A": ["Sc", "Y", "La"],
            "B": ["Fe", "Co", "Ni"],
            "C": ["Si", "Ga", "Ge"],
            "D": ["Gd", "Tb", "Dy"],
        },
    }


def test_convert_custom_labels_to_order_map(custom_labels_from_excel):
    actual_order_map = _convert_custom_labels_to_order_map(
        custom_labels_from_excel
    )
    expected_order_map = {
        2: {"Fe": 0, "Co": 0, "Ni": 0, "Si": 1, "Ga": 1, "Ge": 1},
        3: {
            "Sc": 0,
            "Y": 0,
            "La": 0,
            "Fe": 1,
            "Co": 1,
            "Ni": 1,
            "Si": 2,
            "Ga": 2,
            "Ge": 2,
        },
        4: {
            "Sc": 0,
            "Y": 0,
            "La": 0,
            "Fe": 1,
            "Co": 1,
            "Ni": 1,
            "Si": 2,
            "Ga": 2,
            "Ge": 2,
            "Gd": 3,
            "Tb": 3,
            "Dy": 3,
        },
    }
    assert actual_order_map == expected_order_map


@pytest.mark.parametrize(
    "formula,expected_sorted_formula",
    [
        # Binary
        ("FeSi", "FeSi"),
        ("SiFe", "FeSi"),
        # Ternary
        ("ScFeSi", "ScFeSi"),
        ("FeScSi", "ScFeSi"),
        ("SiFeSc", "ScFeSi"),
        # Quaternary
        ("ScFeSiGd", "ScFeSiGd"),
        ("FeScSiGd", "ScFeSiGd"),
        ("SiFeScGd", "ScFeSiGd"),
        ("GdFeScSi", "ScFeSiGd"),
        ("GdSiFeSc", "ScFeSiGd"),
    ],
)
def test_sort_with_custom_order(
    formula, expected_sorted_formula, custom_labels_from_excel
):
    actual_sorted_formula = sort(formula, custom_labels_from_excel)
    assert actual_sorted_formula == expected_sorted_formula
