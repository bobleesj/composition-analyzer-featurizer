from bobleesj.utils.parsers.formula import Formula


def prepare_binary_formula(formula: str):
    formula_obj = Formula(formula)
    parsed_formula = formula_obj.parsed_formula
    normalized_parsed_formula = formula_obj.get_normalized_parsed_formula()
    A = parsed_formula[0][0]
    B = parsed_formula[1][0]
    index_A = parsed_formula[0][1]
    index_B = parsed_formula[1][1]
    index_A_norm = normalized_parsed_formula[0][1]
    index_B_norm = normalized_parsed_formula[1][1]
    return A, B, index_A, index_B, index_A_norm, index_B_norm


def A_plus_B(A, B, property_name, db):
    return db[A][property_name] + db[B][property_name]


def A_plus_B_weighted(formula, property_name, db):
    A, B, index_A, index_B, _, _ = prepare_binary_formula(formula)
    return (db[A][property_name] * index_A) + (db[B][property_name] * index_B)


def A_plus_B_weighted_norm(formula, prop_name, db):
    A, B, _, _, index_A_norm, index_B_norm = prepare_binary_formula(formula)
    return (db[A][prop_name] * index_A_norm) + (
        db[B][prop_name] * index_B_norm
    )


def A_minus_B(A, B, property_name, db):
    return db[A][property_name] - db[B][property_name]


def A_by_B(A, B, property_name, db):
    return db[A][property_name] / db[B][property_name]


def max_value(A, B, property_name, db):
    return max(db[A][property_name], db[B][property_name])


def min_value(A, B, property_name, db):
    return min(db[A][property_name], db[B][property_name])


def avg_value(A, B, property_name, db):
    return (db[A][property_name] + db[B][property_name]) / 2
