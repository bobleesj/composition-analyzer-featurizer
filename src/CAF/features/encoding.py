from bobleesj.utils.parsers.formula import Formula


def generate_features(formula, elements: list[str]) -> dict[str, float]:
    """Adds normalized compositional one-hot encoding."""
    formula_parsed_normalized = Formula(
        formula
    ).get_normalized_parsed_formula()
    encoding = {element: 0 for element in elements}
    for element, index_norm in formula_parsed_normalized:
        if element in encoding:
            encoding[element] = float(index_norm)
    return encoding
