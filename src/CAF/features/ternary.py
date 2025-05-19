from bobleesj.utils.parsers.formula import Formula
from bobleesj.utils.sources.oliynyk import Property as P

from CAF.features.ternary_helper import (
    M_by_X,
    M_minus_X,
    MX_avg,
    MX_sum_weighted_norm,
    R_by_M,
    R_by_X,
    R_minus_M,
    R_minus_X,
    RM_avg,
    RM_sum_weighted_norm,
    RMX_avg,
    RMX_sum,
    RMX_sum_weighted,
    RMX_sum_weighted_norm,
    RX_avg,
    RX_sum_weighted_norm,
    avg_value,
    avg_weighted_RMX,
    max_value,
    min_value,
    prepare_ternary_formula,
)


def generate_features(formula: str, db: dict) -> dict:
    (
        R,
        M,
        X,
        index_R,
        index_M,
        index_X,
        index_R_norm,
        index_M_norm,
        index_X_norm,
    ) = prepare_ternary_formula(formula)
    RMX = (R, M, X)
    indices = (index_R, index_M, index_X)
    indices_norm = (index_R_norm, index_M_norm, index_X_norm)
    index_max, index_min, index_avg = Formula(formula).max_min_avg_index

    features = {
        "formula": formula,
        # index - 9 features
        "index_R": index_R,
        "index_M": index_M,
        "index_X": index_X,
        "index_R_norm": index_R_norm,
        "index_M_norm": index_M_norm,
        "index_X_norm": index_X_norm,
        "index_max": index_max,
        "index_min": index_min,
        "index_avg": index_avg,
        # atomic_weight - 4 features
        "atomic_weight_RMX_sum_weighted": RMX_sum_weighted(
            RMX, indices, P.AW, db
        ),
        "atomic_weight_R/M": R_by_M(R, M, P.AW, db),
        "atomic_weight_M/X": M_by_X(M, X, P.AW, db),
        "atomic_weight_R/X": R_by_X(R, X, P.AW, db),
        # atomic number - 8 features
        "atomic_number_R-M": R_minus_M(R, M, P.ATOMIC_NUMBER, db),
        "atomic_number_M-X": M_minus_X(M, X, P.ATOMIC_NUMBER, db),
        "atomic_number_R-X": R_minus_X(R, X, P.ATOMIC_NUMBER, db),
        "atomic_number_RMX_avg": RMX_avg(RMX, P.ATOMIC_NUMBER, db),
        "atomic_number_RMX_avg_weighted": avg_weighted_RMX(
            RMX, indices, P.ATOMIC_NUMBER, db
        ),
        "atomic_number_RM_avg": RM_avg(R, M, P.ATOMIC_NUMBER, db),
        "atomic_number_MX_avg": MX_avg(M, X, P.ATOMIC_NUMBER, db),
        "atomic_number_RX_avg": RX_avg(R, X, P.ATOMIC_NUMBER, db),
        # period - 7 features
        "period_R": db[R][P.PERIOD],
        "period_M": db[M][P.PERIOD],
        "period_X": db[X][P.PERIOD],
        "period_RMX_sum_weighted_norm": RMX_sum_weighted_norm(
            RMX, indices_norm, P.PERIOD, db
        ),
        "period_RM_sum_weighted_norm": RM_sum_weighted_norm(
            R, M, indices_norm, P.PERIOD, db
        ),
        "period_MX_sum_weighted_norm": MX_sum_weighted_norm(
            M, X, indices_norm, P.PERIOD, db
        ),
        "period_RX_sum_weighted_norm": RX_sum_weighted_norm(
            R, X, indices_norm, P.PERIOD, db
        ),
        # group - 10 features
        "group_R": db[R][P.GROUP],
        "group_M": db[M][P.GROUP],
        "group_X": db[X][P.GROUP],
        "group_R-M": R_minus_M(R, M, P.GROUP, db),
        "group_M-X": M_minus_X(M, X, P.GROUP, db),
        "group_R-X": R_minus_X(R, X, P.GROUP, db),
        "group_RMX_sum_weighted_norm": RMX_sum_weighted_norm(
            RMX, indices_norm, P.GROUP, db
        ),
        "group_RM_sum_weighted_norm": RM_sum_weighted_norm(
            R, M, indices_norm, P.GROUP, db
        ),
        "group_MX_sum_weighted_norm": MX_sum_weighted_norm(
            M, X, indices_norm, P.GROUP, db
        ),
        "group_RX_sum_weighted_norm": RX_sum_weighted_norm(
            R, X, indices_norm, P.GROUP, db
        ),
        # Mendeleev number - 14 features
        "Mendeleev_number_R": db[R][P.MEND_NUM],
        "Mendeleev_number_M": db[M][P.MEND_NUM],
        "Mendeleev_number_X": db[X][P.MEND_NUM],
        "Mendeleev_number_R-M": R_minus_M(R, M, P.MEND_NUM, db),
        "Mendeleev_number_M-X": M_minus_X(M, X, P.MEND_NUM, db),
        "Mendeleev_number_R-X": R_minus_X(R, X, P.MEND_NUM, db),
        "Mendeleev_number_RMX_avg": RMX_avg(RMX, P.MEND_NUM, db),
        "Mendeleev_number_RMX_avg_weighted": avg_weighted_RMX(
            RMX, indices, P.MEND_NUM, db
        ),
        "Mendeleev_number_RM_avg": RM_avg(R, M, P.MEND_NUM, db),
        "Mendeleev_number_MX_avg": MX_avg(M, X, P.MEND_NUM, db),
        "Mendeleev_number_RX_avg": RX_avg(R, X, P.MEND_NUM, db),
        "Mendeleev_number_RM_sum_weighted_norm": RM_sum_weighted_norm(
            R, M, indices_norm, P.MEND_NUM, db
        ),
        "Mendeleev_number_MX_sum_weighted_norm": MX_sum_weighted_norm(
            M, X, indices_norm, P.MEND_NUM, db
        ),
        "Mendeleev_number_RX_sum_weighted_norm": RX_sum_weighted_norm(
            R, X, indices_norm, P.MEND_NUM, db
        ),
    }
    # Set 1 of properties with 9 identical features
    rest_properties_one = [
        P.VAL_TOTAL,
        P.UNPARIED_E,
        P.GILMAN,
    ]

    for prop in rest_properties_one:
        prop = prop.value
        features.update(
            {
                f"{prop}_R": db[R][prop],
                f"{prop}_M": db[M][prop],
                f"{prop}_X": db[X][prop],
                f"{prop}_RMX_sum": RMX_sum(RMX, prop, db),
                f"{prop}_RMX_sum_weighted": RMX_sum_weighted(
                    RMX, indices, prop, db
                ),
                f"{prop}_RMX_sum_weighted_norm": RMX_sum_weighted_norm(
                    RMX, indices_norm, prop, db
                ),
                f"{prop}_RM_sum_weighted_norm": RM_sum_weighted_norm(
                    R, M, indices_norm, prop, db
                ),
                f"{prop}_MX_sum_weighted_norm": MX_sum_weighted_norm(
                    M, X, indices_norm, prop, db
                ),
                f"{prop}_RX_sum_weighted_norm": RX_sum_weighted_norm(
                    R, X, indices_norm, prop, db
                ),
            }
        )

    # Set 2 of properties with identical 9 features
    rest_properties_two = [
        P.Z_EFF,
        P.ION_ENERGY,
        P.COORD_NUM,
        P.RATIO_CLOSEST,
        P.POLYHEDRON_DISTORT,
        P.CIF_RADIUS,
        P.PAULING_RADIUS_CN12,
        P.PAULING_EN,
        P.MARTYNOV_BATSANOV_EN,
        P.MELTING_POINT_K,
        P.DENSITY,
        P.SPECIFIC_HEAT,
        P.COHESIVE_ENERGY,
        P.BULK_MODULUS,
    ]

    for prop in rest_properties_two:
        prop = prop.value
        features.update(
            {
                f"{prop}_R": db[R][prop],
                f"{prop}_M": db[M][prop],
                f"{prop}_X": db[X][prop],
                f"{prop}_R/M": R_by_M(R, M, prop, db),
                f"{prop}_M/X": M_by_X(M, X, prop, db),
                f"{prop}_R/X": R_by_X(R, X, prop, db),
                f"{prop}_max": max_value(RMX, prop, db),
                f"{prop}_min": min_value(RMX, prop, db),
                f"{prop}_avg": avg_value(RMX, prop, db),
            }
        )

    return features
