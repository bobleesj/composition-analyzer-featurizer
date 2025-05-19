from bobleesj.utils.parsers.formula import Formula


def prepare_ternary_formula(formula: str):
    formula_obj = Formula(formula)
    parsed_formula = formula_obj.parsed_formula
    normalized_parsed_formula = formula_obj.get_normalized_parsed_formula()
    R = parsed_formula[0][0]
    M = parsed_formula[1][0]
    X = parsed_formula[2][0]
    index_R = parsed_formula[0][1]
    index_M = parsed_formula[1][1]
    index_X = parsed_formula[2][1]
    index_R_norm = normalized_parsed_formula[0][1]
    index_M_norm = normalized_parsed_formula[1][1]
    index_X_norm = normalized_parsed_formula[2][1]
    return (
        R,
        M,
        X,
        index_R,
        index_M,
        index_X,
        index_R_norm,
        index_M_norm,
        index_X_norm,
    )


# Sum
def RMX_sum(RMX, property_name, db):
    R, M, X = RMX
    return db[R][property_name] + db[M][property_name] + db[X][property_name]


def RMX_sum_weighted(RMX, indices, property_name, db):
    R, M, X = RMX
    index_R, index_M, index_X = indices
    return (
        (db[R][property_name] * index_R)
        + (db[M][property_name] * index_M)
        + (db[X][property_name] * index_X)
    )


def RMX_sum_weighted_norm(RMX, indices_norm, property_name, db):
    R, M, X = RMX
    index_R_norm, index_M_norm, index_X_norm = indices_norm
    return (
        (db[R][property_name] * index_R_norm)
        + (db[M][property_name] * index_M_norm)
        + (db[X][property_name] * index_X_norm)
    )


def RM_sum_weighted_norm(R, M, indices_norm, property_name, db):
    index_R_norm, index_M_norm, _ = indices_norm
    return (
        (db[R][property_name] * index_R_norm)
        + (db[M][property_name] * index_M_norm)
    ) / (index_R_norm + index_M_norm)


def MX_sum_weighted_norm(M, X, indices_norm, property_name, db):
    _, index_M_norm, index_X_norm = indices_norm
    return (
        (db[M][property_name] * index_M_norm)
        + (db[X][property_name] * index_X_norm)
    ) / (index_M_norm + index_X_norm)


def RX_sum_weighted_norm(R, X, indices_norm, property_name, db):
    index_R_norm, _, index_X_norm = indices_norm
    return (
        (db[R][property_name] * index_R_norm)
        + (db[X][property_name] * index_X_norm)
    ) / (index_R_norm + index_X_norm)


# Division
def R_by_M(R, M, property_name, db):
    return db[R][property_name] / db[M][property_name]


def M_by_X(M, X, property_name, db):
    return db[M][property_name] / db[X][property_name]


def R_by_X(R, X, property_name, db):
    return db[R][property_name] / db[X][property_name]


# Subtraction
def R_minus_M(R, M, property_name, db):
    return db[R][property_name] - db[M][property_name]


def M_minus_X(M, X, property_name, db):
    return db[M][property_name] - db[X][property_name]


def R_minus_X(R, X, property_name, db):
    return db[R][property_name] - db[X][property_name]


# Average
def RMX_avg(RMX, property_name, db):
    R, M, X = RMX
    return (
        db[R][property_name] + db[M][property_name] + db[X][property_name]
    ) / 3


def RM_avg(R, M, property_name, db):
    return (db[R][property_name] + db[M][property_name]) / 2


def MX_avg(M, X, property_name, db):
    return (db[M][property_name] + db[X][property_name]) / 2


def RX_avg(R, X, property_name, db):
    return (db[R][property_name] + db[X][property_name]) / 2


def avg_weighted_RMX(RMX, indices, property_name, db):
    R, M, X = RMX
    index_R, index_M, index_X = indices
    return (
        (db[R][property_name] * index_R)
        + (db[M][property_name] * index_M)
        + (db[X][property_name] * index_X)
    ) / (index_R + index_M + index_X)


def avg_weighted_norm_RMX(RMX, norm_indices, property_name, db):
    R, M, X = RMX
    index_R_norm, index_M_norm, index_X_norm = norm_indices
    return (
        (db[R][property_name] * index_R_norm)
        + (db[M][property_name] * index_M_norm)
        + (db[X][property_name] * index_X_norm)
    ) / (index_R_norm + index_M_norm + index_X_norm)


# Max and min
def max_value(RMX, property_name, db):
    R, M, X = RMX
    return max(
        db[R][property_name], db[M][property_name], db[X][property_name]
    )


def min_value(RMX, property_name, db):
    R, M, X = RMX
    return min(
        db[R][property_name], db[M][property_name], db[X][property_name]
    )


def avg_value(RMX, property_name, db):
    R, M, X = RMX
    return (
        db[R][property_name] + db[M][property_name] + db[X][property_name]
    ) / 3
