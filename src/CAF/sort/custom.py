from bobleesj.utils.parsers.formula import Formula


def sort(
    formula: str,
    element_order: dict,
    normalize: bool = False,
) -> str:
    """Sort elements in a chemical formula using a precomputed element order
    map.

    Parameters
    ----------
    formula : str
        The chemical formula to be sorted.
    element_order : dict
        The mapping from element symbols to their desired sort index.
    normalize : bool, optional
        Whether to normalize the parsed formula, by default False.

    Returns
    -------
    str
        The sorted formula string.
    """
    formula_obj = Formula(formula)
    formula_parsed = formula_obj.get_normalized_parsed_formula() if normalize else formula_obj.parsed_formula
    formula_sorted = sorted(formula_parsed, key=lambda x: element_order.get(x[0], float("inf")))
    return Formula.build_formula_from_parsed(formula_sorted)


def convert_custom_labels_to_order_map(custom_labels: dict) -> dict:
    """Convert a nested custom_labels dictionary into an element order mapping.

    Parameters
    ----------
    custom_labels : dict
        The dictionary mapping element counts to label mappings. Each label mapping
        is a dictionary where keys are label names and values are lists of element symbols
        or comma-separated strings of element symbols.

    Returns
    -------
    dict
        The dictionary mapping element counts to dictionaries of element symbol to order index.

    Examples
    --------
    >>> custom_labels = {
    ...     2: {
    ...         "A": ["Li", "Er"],
    ...         "B": ["B", "In"],
    ...     },
    ...     3: {
    ...         "R": ["Er"],
    ...         "M": ["Co"],
    ...         "X": ["In"],
    ...     },
    ...     4: {
    ...         "A": ["Er"],
    ...         "B": ["Co"],
    ...         "C": ["In"],
    ...         "D": ["U"],
    ...     },
    ... }
    >>> convert_custom_labels_to_order_map(custom_labels)
    {
        2: {'Li': 0, 'Er': 0, 'B': 1, 'In': 1},
        3: {'Er': 0, 'Co': 1, 'In': 2},
        4: {'Er': 0, 'Co': 1, 'In': 2, 'U': 3}
    }
    """
    element_order = {}
    for element_count, label_mapping in custom_labels.items():
        order_map = {}
        for idx, elements in enumerate(label_mapping.values()):
            for element in elements:
                order_map[element] = idx
        element_order[element_count] = order_map
    return element_order
