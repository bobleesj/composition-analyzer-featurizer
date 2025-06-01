from bobleesj.utils.parsers.formula import Formula
from bobleesj.utils.sources.oliynyk import Oliynyk, Property


def sort(
    formula: str,
    property: Property,
    oliynyk: Oliynyk,
    ascending=True,
    normalize=False,
) -> str:
    """Sort the elements in a chemical formula based on a specified CAF
    property.

    Parameters
    ----------
    formula : str
        The chemical formula to be sorted.
    property : Property
        The CAF property name to sort by (e.g., atomic radius).
    oliynyk : Oliynyk
        The CAF oliynyk dataset.
    ascending : bool=True
        Whether to sort in ascending order. Defaults to True.
    normalize : bool=False
        Whether to normalize the formula before sorting.

    Returns
    -------
    str
        The formula string with elements sorted according to the
        specified property.

    Examples
    --------
    >>> sort("Cu2Al", Property.ATOMIC_NUMBER, db)
    "AlCu2"
    """
    formula_obj = Formula(formula)
    formula_parsed = (
        formula_obj.get_normalized_parsed_formula()
        if normalize
        else formula_obj.parsed_formula
    )
    property_data = oliynyk.get_property_data_for_formula(formula, property)
    formula_sorted = sorted(
        formula_parsed,
        key=lambda x: property_data.get(x[0], 0),
        reverse=not ascending,
    )
    return Formula.build_formula_from_parsed(formula_sorted)
