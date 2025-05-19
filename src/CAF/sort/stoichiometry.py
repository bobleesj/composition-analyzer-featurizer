from bobleesj.utils.parsers.formula import Formula
from bobleesj.utils.sources.oliynyk import Oliynyk, Property


def sort(
    formula: str,
    oliynyk: Oliynyk,
    ascending=True,
    normalize=False,
) -> str:
    """Sort the elements in the chemical formula based on their composition.

    When there are more than one element with the same compsition, the
    Mendeleev number is used to break the tie. During the tie, the Mendeleev
    number is always sorted in ascending order.

    Parameters
    ----------
    formula : str
        The chemical formula to be sorted.
    oliynyk : Oliynyk
        The Oliynyk dataset object.
    ascending : bool, optional
        Whether to sort in ascending order. Defaults to True.
    normalize : bool, optional
        Whether to normalize the formula before sorting. Defaults to False.

    Returns
    -------
    str
        The formula string with elements sorted according to the specified
        property.

    Examples
    --------
    >>> sort("LiNa2B", db)
    "LiBNa2"
    """
    formula_obj = Formula(formula)
    formula_parsed = (
        formula_obj.get_normalized_parsed_formula()
        if normalize
        else formula_obj.parsed_formula
    )
    mend_numbers = oliynyk.get_property_data_for_formula(
        formula, Property.MEND_NUM
    )
    reverse = not ascending
    formula_sorted = sorted(
        formula_parsed,
        key=lambda x: (
            # 1st sort, reverse sort if descending (reversed)
            -x[1] if reverse else x[1],
            # 2nd sort for the same compoposition. Always ascending sort.
            mend_numbers[x[0]],
        ),
    )
    return Formula.build_formula_from_parsed(formula_sorted)
