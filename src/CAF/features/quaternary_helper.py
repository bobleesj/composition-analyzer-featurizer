from bobleesj.utils.parsers.formula import Formula


def prepare_quaternary_formula(formula: str):
    formula_obj = Formula(formula)
    parsed_formula = formula_obj.parsed_formula
    normalized_parsed_formula = formula_obj.get_normalized_parsed_formula()
    A = parsed_formula[0][0]
    B = parsed_formula[1][0]
    C = parsed_formula[2][0]
    D = parsed_formula[3][0]
    index_A = parsed_formula[0][1]
    index_B = parsed_formula[1][1]
    index_C = parsed_formula[2][1]
    index_D = parsed_formula[3][1]
    index_A_norm = normalized_parsed_formula[0][1]
    index_B_norm = normalized_parsed_formula[1][1]
    index_C_norm = normalized_parsed_formula[2][1]
    index_D_norm = normalized_parsed_formula[3][1]
    return (
        (A, B, C, D),
        (index_A, index_B, index_C, index_D),
        (
            index_A_norm,
            index_B_norm,
            index_C_norm,
            index_D_norm,
        ),
    )


# Sum
def ABCD_sum(ABCD, prop_name, db):
    A, B, C, D = ABCD
    return (
        db[A][prop_name]
        + db[B][prop_name]
        + db[C][prop_name]
        + db[D][prop_name]
    )


def ABCD_sum_weighted(ABCD, indices, prop_name, db):
    A, B, C, D = ABCD
    index_A, index_B, index_C, index_D = indices
    return (
        (db[A][prop_name] * index_A)
        + (db[B][prop_name] * index_B)
        + (db[C][prop_name] * index_C)
        + (db[D][prop_name] * index_D)
    )


def ABCD_sum_weighted_norm(ABCD, indices_norm, prop_name, db):
    A, B, C, D = ABCD
    index_A_norm, index_B_norm, index_C_norm, index_D_norm = indices_norm
    return (
        (db[A][prop_name] * index_A_norm)
        + (db[B][prop_name] * index_B_norm)
        + (db[C][prop_name] * index_C_norm)
        + (db[D][prop_name] * index_D_norm)
    )


def AB_sum_weighted_norm(A, B, index_A_norm, index_B_norm, prop_name, db):
    return (
        (db[A][prop_name] * index_A_norm) + (db[B][prop_name] * index_B_norm)
    ) / (index_A_norm + index_B_norm)


def AC_sum_weighted_norm(A, C, index_A_norm, index_C_norm, prop_name, db):
    return (
        (db[A][prop_name] * index_A_norm) + (db[C][prop_name] * index_C_norm)
    ) / (index_A_norm + index_C_norm)


def AD_sum_weighted_norm(A, D, index_A_norm, index_D_norm, prop_name, db):
    return (
        (db[A][prop_name] * index_A_norm) + (db[D][prop_name] * index_D_norm)
    ) / (index_A_norm + index_D_norm)


def BC_sum_weighted_norm(B, C, index_B_norm, index_C_norm, prop_name, db):
    return (
        (db[B][prop_name] * index_B_norm) + (db[C][prop_name] * index_C_norm)
    ) / (index_B_norm + index_C_norm)


def BD_sum_weighted_norm(B, D, index_B_norm, index_D_norm, prop_name, db):
    return (
        (db[B][prop_name] * index_B_norm) + (db[D][prop_name] * index_D_norm)
    ) / (index_B_norm + index_D_norm)


def CD_sum_weighted_norm(C, D, index_C_norm, index_D_norm, prop_name, db):
    return (
        (db[C][prop_name] * index_C_norm) + (db[D][prop_name] * index_D_norm)
    ) / (index_C_norm + index_D_norm)


# Min and max


def ABCD_max(ABCD, property_name, db):
    A, B, C, D = ABCD
    return max(
        db[A][property_name],
        db[B][property_name],
        db[C][property_name],
        db[D][property_name],
    )


def ABCD_min(ABCD, property_name, db):
    A, B, C, D = ABCD
    return min(
        db[A][property_name],
        db[B][property_name],
        db[C][property_name],
        db[D][property_name],
    )


# Average
def ABCD_avg(ABCD, prop_name, db):
    A, B, C, D = ABCD
    return (
        db[A][prop_name]
        + db[B][prop_name]
        + db[C][prop_name]
        + db[D][prop_name]
    ) / 4


def ABCD_avg_weighted(ABCD, indices, prop_name, db):
    A, B, C, D = ABCD
    index_A, index_B, index_C, index_D = indices
    return (
        (db[A][prop_name] * index_A)
        + (db[B][prop_name] * index_B)
        + (db[C][prop_name] * index_C)
        + (db[D][prop_name] * index_D)
    ) / (index_A + index_B + index_C + index_D)


def ABCD_avg_weighted_norm(ABCD, indices_norm, prop_name, db):
    A, B, C, D = ABCD
    index_A_norm, index_B_norm, index_C_norm, index_D_norm = indices_norm
    return (
        (db[A][prop_name] * index_A_norm)
        + (db[B][prop_name] * index_B_norm)
        + (db[C][prop_name] * index_C_norm)
        + (db[D][prop_name] * index_D_norm)
    ) / (index_A_norm + index_B_norm + index_C_norm + index_D_norm)


def AB_avg(A, B, prop_name, db):
    return (db[A][prop_name] + db[B][prop_name]) / 2


def AC_avg(A, C, prop_name, db):
    return (db[A][prop_name] + db[C][prop_name]) / 2


def AD_avg(A, D, prop_name, db):
    return (db[A][prop_name] + db[D][prop_name]) / 2


def BC_avg(B, C, prop_name, db):
    return (db[B][prop_name] + db[C][prop_name]) / 2


def BD_avg(B, D, prop_name, db):
    return (db[B][prop_name] + db[D][prop_name]) / 2


def CD_avg(C, D, prop_name, db):
    return (db[C][prop_name] + db[D][prop_name]) / 2


# Subtraction
def A_minus_B(A, B, prop_name, db):
    return db[A][prop_name] - db[B][prop_name]


def A_minus_C(A, C, prop_name, db):
    return db[A][prop_name] - db[C][prop_name]


def A_minus_D(A, D, prop_name, db):
    return db[A][prop_name] - db[D][prop_name]


def B_minus_C(B, C, prop_name, db):
    return db[B][prop_name] - db[C][prop_name]


def B_minus_D(B, D, prop_name, db):
    return db[B][prop_name] - db[D][prop_name]


def C_minus_D(C, D, prop_name, db):
    return db[C][prop_name] - db[D][prop_name]


# Division
def A_by_B(A, B, prop_name, db):
    return db[A][prop_name] / db[B][prop_name]


def A_by_C(A, C, prop_name, db):
    return db[A][prop_name] / db[C][prop_name]


def A_by_D(A, D, prop_name, db):
    return db[A][prop_name] / db[D][prop_name]


def B_by_C(B, C, prop_name, db):
    return db[B][prop_name] / db[C][prop_name]


def B_by_D(B, D, prop_name, db):
    return db[B][prop_name] / db[D][prop_name]


def C_by_D(C, D, prop_name, db):
    return db[C][prop_name] / db[D][prop_name]


# Min, max, avg
# Max and min
