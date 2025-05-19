import pandas as pd
from bobleesj.utils.parsers.formula import Formula


def sort(
    formula: str,
    custom_labels: dict,
    normalize: bool = False,
) -> str:
    """Sort elements in a chemical formula using a precomputed element order
    map.

    Parameters
    ----------
    formula : str
        The chemical formula to be sorted.
    element_order : dict[int, dict[str, int]]
        The mapping from element symbols to their desired sort index.
    normalize : bool, optional
        Whether to normalize the parsed formula, by default False.

    Returns
    -------
    str
        The sorted formula string.
    Examples
    --------
    >>> formula = "BLi"
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
    >>> sorted_formula = sort(formula, custom_labels)
    >>> print(sorted_formula)
    LiB
    """
    formula_obj = Formula(formula)
    formula_parsed = (
        formula_obj.get_normalized_parsed_formula()
        if normalize
        else formula_obj.parsed_formula
    )
    num_elements = formula_obj.element_count
    label_order_map = _convert_custom_labels_to_order_map(custom_labels)
    element_order = label_order_map.get(num_elements, {})
    formula_sorted = sorted(
        formula_parsed, key=lambda x: element_order.get(x[0], float("inf"))
    )
    return Formula.build_formula_from_parsed(formula_sorted)


def _convert_custom_labels_to_order_map(custom_labels: dict) -> dict:
    """Convert a nested custom_labels dictionary into an element order mapping.

    This function is used for the sorting of elements in the sort formula as
    a part of the sorted function above.

    Parameters
    ----------
    custom_labels : dict
        The dictionary mapping element counts to label mappings. Each label
        mapping is a dictionary where keys are label names and values are
        lists of element symbols or comma-separated strings of element symbols.

    Returns
    -------
    label_order_map : dict[int, dict[str, int]]
        The dictionary mapping element counts to dictionaries of element
        symbol to order index.

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
    label_order_map = {}
    for element_count, label_mapping in custom_labels.items():
        order_map = {}
        for idx, elements in enumerate(label_mapping.values()):
            for element in elements:
                order_map[element] = idx
        label_order_map[element_count] = order_map
    return label_order_map


def get_custom_labels_from_excel(excel_path: str) -> dict:
    """Read custom labels from an Excel file and return a dictionary
    mapping."""

    sheet_map = {
        2: ("Binary", ["Element_A", "Element_B"]),
        3: ("Ternary", ["Element_R", "Element_M", "Element_X"]),
        4: (
            "Quaternary",
            ["Element_A", "Element_B", "Element_C", "Element_D"],
        ),
    }

    label_keys_map = {
        2: ["A", "B"],
        3: ["R", "M", "X"],
        4: ["A", "B", "C", "D"],
    }

    custom_labels = {}
    for num_elements, (sheet, columns) in sheet_map.items():
        df = pd.read_excel(excel_path, sheet_name=sheet, engine="openpyxl")
        element_lists = [df[col].dropna().tolist() for col in columns]
        label_keys = label_keys_map[num_elements]
        custom_labels[num_elements] = {
            label: elements
            for label, elements in zip(label_keys, element_lists)
        }
    return custom_labels
