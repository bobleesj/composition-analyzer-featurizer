import pytest
from bobleesj.utils.sources.oliynyk import Property

from CAF.sort.property import sort


@pytest.mark.parametrize(
    "formula, ascending, normalize, expected_output",
    [
        # C1. Ascending (Al = 13, Cu = 29) → Al before Cu
        ("AlCu2", True, False, "AlCu2"),
        ("Cu2Al", True, False, "AlCu2"),
        # # C2. Ascending, normalized
        ("AlCu2", True, True, "Al0.333333Cu0.666667"),
        ("Cu2Al", True, True, "Al0.333333Cu0.666667"),
        # C3. Descending
        ("AlCu2", False, False, "Cu2Al"),
        ("Cu2Al1", False, False, "Cu2Al"),
        # C4. Descending, normalized
        ("AlCu2", False, True, "Cu0.666667Al0.333333"),
        ("Cu2Al", False, True, "Cu0.666667Al0.333333"),
    ],
)
def test_sort_by_CAF_property(
    formula, ascending, normalize, expected_output, oliynyk_obj
):

    property = Property.ATOMIC_NUMBER
    result = sort(formula, property, oliynyk_obj, ascending, normalize)
    assert result == expected_output
