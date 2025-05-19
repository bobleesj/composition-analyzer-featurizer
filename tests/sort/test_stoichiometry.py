import pytest

from CAF.sort.stoichiometry import sort


@pytest.mark.parametrize(
    # Li Mendeleev number = 1
    # Na Mendeleev number = 11
    # B Mendeleev number = 72
    "formula, expected_output",
    [
        # Test sorting by composiiton, ascending
        # C1. Test binary
        ("LiB", "LiB"),
        ("Li1B1", "LiB"),
        ("LiB1", "LiB"),
        ("BLi", "LiB"),
        ("B1Li1", "LiB"),
        ("BLi1", "LiB"),
        # C2 Test ternary
        # 1. All 3 element same comp, expect LiNaB
        ("LiNaB", "LiNaB"),
        ("Li1Na1B1", "LiNaB"),
        ("LiNaB1", "LiNaB"),
        ("BLiNa", "LiNaB"),
        ("BLi1Na1", "LiNaB"),
        ("BLiNa1", "LiNaB"),
        # 2. Two elements same comp, expect one element last
        ("LiNa2B", "LiBNa2"),  # Na2 should be last
        ("LiNaB2", "LiNaB2"),  # B2 should be last
        ("Li2NaB", "NaBLi2"),  # Li2 should be last
    ],
)
def test_sort_by_composition_ascending(formula, oliynyk_obj, expected_output):
    result = sort(formula, oliynyk_obj)
    assert result == expected_output


@pytest.mark.parametrize(
    "formula, expected_output",
    [
        # Test sorting by composition, descending
        # C1. Test binary
        ("LiB", "LiB"),
        ("Li1B1", "LiB"),
        ("LiB1", "LiB"),
        ("BLi", "LiB"),
        ("B1Li1", "LiB"),
        ("BLi1", "LiB"),
        # C2 Test ternary
        # 1. Two elements same comp, expect one element last
        ("LiNa2B", "Na2LiB"),  # Li should be last
        ("LiNaB2", "B2LiNa"),  # Na should be last
        # ("Li2NaB", "BNaLi2"), # Na should be last
    ],
)
def test_sort_by_composition_descending(formula, expected_output, oliynyk_obj):
    result = sort(formula, oliynyk_obj, ascending=False)
    assert result == expected_output
