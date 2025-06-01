from bobleesj.utils.parsers.formula import Formula
from bobleesj.utils.sources.oliynyk import Property as P

from CAF.features import quaternary_helper as helper


def generate_features(formula: str, db: dict) -> dict:
    ABCD, indices, indices_norm = helper.prepare_quaternary_formula(formula)
    A, B, C, D = ABCD
    index_A, index_B, index_C, index_D = indices
    index_A_norm, index_B_norm, index_C_norm, index_D_norm = indices_norm
    formula_obj = Formula(formula)
    index_max, index_min, index_avg = formula_obj.max_min_avg_index
    features = {
        "formula": formula,
        # index - 9 features
        "index_A": index_A,
        "index_B": index_B,
        "index_C": index_C,
        "index_D": index_D,
        "index_A_norm": index_A_norm,
        "index_B_norm": index_B_norm,
        "index_C_norm": index_C_norm,
        "index_D_norm": index_D_norm,
        "index_max": index_max,
        "index_min": index_min,
        "index_avg": index_avg,
        # atomic weight - 7
        "atomic_weight_ABCD_sum_weighted": helper.ABCD_sum_weighted(
            ABCD, indices, P.AW, db
        ),
        "atomic_weight_A/B": helper.A_by_B(A, B, P.AW, db),
        "atomic_weight_A/C": helper.A_by_C(A, C, P.AW, db),
        "atomic_weight_A/D": helper.A_by_D(A, D, P.AW, db),
        "atomic_weight_B/C": helper.B_by_C(B, C, P.AW, db),
        "atomic_weight_B/D": helper.B_by_D(B, D, P.AW, db),
        "atomic_weight_C/D": helper.C_by_D(C, D, P.AW, db),
        # atomic_number - 14
        "atomic_number_A-B": helper.A_minus_B(A, B, P.ATOMIC_NUMBER, db),
        "atomic_number_A-C": helper.A_minus_C(A, C, P.ATOMIC_NUMBER, db),
        "atomic_number_A-D": helper.A_minus_D(A, D, P.ATOMIC_NUMBER, db),
        "atomic_number_B-C": helper.B_minus_C(B, C, P.ATOMIC_NUMBER, db),
        "atomic_number_B-D": helper.B_minus_D(B, D, P.ATOMIC_NUMBER, db),
        "atomic_number_C-D": helper.C_minus_D(C, D, P.ATOMIC_NUMBER, db),
        "atomic_number_ABCD_avg": helper.ABCD_avg(ABCD, P.ATOMIC_NUMBER, db),
        "atomic_number_ABCD_avg_weighted": helper.ABCD_avg_weighted(
            ABCD, indices, P.ATOMIC_NUMBER, db
        ),
        "atomic_number_AB_avg": helper.AB_avg(A, B, P.ATOMIC_NUMBER, db),
        "atomic_number_AC_avg": helper.AC_avg(A, C, P.ATOMIC_NUMBER, db),
        "atomic_number_AD_avg": helper.AD_avg(A, D, P.ATOMIC_NUMBER, db),
        "atomic_number_BC_avg": helper.BC_avg(B, C, P.ATOMIC_NUMBER, db),
        "atomic_number_BD_avg": helper.BD_avg(B, D, P.ATOMIC_NUMBER, db),
        "atomic_number_CD_avg": helper.CD_avg(C, D, P.ATOMIC_NUMBER, db),
        # period - 11
        "period_A": db[A][P.PERIOD],
        "period_B": db[B][P.PERIOD],
        "period_C": db[C][P.PERIOD],
        "period_D": db[D][P.PERIOD],
        "period_ABCD_sum_weighted_norm": helper.ABCD_sum_weighted_norm(
            ABCD, indices_norm, P.PERIOD, db
        ),
        "period_AB_sum_weighted_norm": helper.AB_sum_weighted_norm(
            A, B, index_A_norm, index_B_norm, P.PERIOD, db
        ),
        "period_AC_sum_weighted_norm": helper.AC_sum_weighted_norm(
            A, C, index_A_norm, index_C_norm, P.PERIOD, db
        ),
        "period_AD_sum_weighted_norm": helper.AD_sum_weighted_norm(
            A, D, index_A_norm, index_D_norm, P.PERIOD, db
        ),
        "period_BC_sum_weighted_norm": helper.BC_sum_weighted_norm(
            B, C, index_B_norm, index_C_norm, P.PERIOD, db
        ),
        "period_BD_sum_weighted_norm": helper.BD_sum_weighted_norm(
            B, D, index_B_norm, index_D_norm, P.PERIOD, db
        ),
        "period_CD_sum_weighted_norm": helper.CD_sum_weighted_norm(
            C, D, index_C_norm, index_D_norm, P.PERIOD, db
        ),
        # group - 17
        "group_A": db[A][P.GROUP],
        "group_B": db[B][P.GROUP],
        "group_C": db[C][P.GROUP],
        "group_D": db[D][P.GROUP],
        "group_A-B": helper.A_minus_B(A, B, P.GROUP, db),
        "group_A-C": helper.A_minus_C(A, C, P.GROUP, db),
        "group_A-D": helper.A_minus_D(A, D, P.GROUP, db),
        "group_B-C": helper.B_minus_C(B, C, P.GROUP, db),
        "group_B-D": helper.B_minus_D(B, D, P.GROUP, db),
        "group_C-D": helper.C_minus_D(C, D, P.GROUP, db),
        "group_ABCD_sum_weighted_norm": helper.ABCD_sum_weighted_norm(
            ABCD, indices_norm, P.GROUP, db
        ),
        "group_AB_sum_weighted_norm": helper.AB_sum_weighted_norm(
            A, B, index_A_norm, index_B_norm, P.GROUP, db
        ),
        "group_AC_sum_weighted_norm": helper.AC_sum_weighted_norm(
            A, C, index_A_norm, index_C_norm, P.GROUP, db
        ),
        "group_AD_sum_weighted_norm": helper.AD_sum_weighted_norm(
            A, D, index_A_norm, index_D_norm, P.GROUP, db
        ),
        "group_BC_sum_weighted_norm": helper.BC_sum_weighted_norm(
            B, C, index_B_norm, index_C_norm, P.GROUP, db
        ),
        "group_BD_sum_weighted_norm": helper.BD_sum_weighted_norm(
            B, D, index_B_norm, index_D_norm, P.GROUP, db
        ),
        "group_CD_sum_weighted_norm": helper.CD_sum_weighted_norm(
            C, D, index_C_norm, index_D_norm, P.GROUP, db
        ),
        # Mendeleeve_number - 24
        "Mendeleev_number_A": db[A][P.MEND_NUM],
        "Mendeleev_number_B": db[B][P.MEND_NUM],
        "Mendeleev_number_C": db[C][P.MEND_NUM],
        "Mendeleev_number_D": db[D][P.MEND_NUM],
        "Mendeleev_number_A-B": helper.A_minus_B(A, B, P.MEND_NUM, db),
        "Mendeleev_number_A-C": helper.A_minus_C(A, C, P.MEND_NUM, db),
        "Mendeleev_number_A-D": helper.A_minus_D(A, D, P.MEND_NUM, db),
        "Mendeleev_number_B-C": helper.B_minus_C(B, C, P.MEND_NUM, db),
        "Mendeleev_number_B-D": helper.B_minus_D(B, D, P.MEND_NUM, db),
        "Mendeleev_number_C-D": helper.C_minus_D(C, D, P.MEND_NUM, db),
        "Mendeleev_number_ABCD_avg": helper.ABCD_avg(ABCD, P.MEND_NUM, db),
        "Mendeleev_number_ABCD_avg_weighted": helper.ABCD_avg_weighted(
            ABCD, indices, P.MEND_NUM, db
        ),
        "Mendeleev_number_AB_avg": helper.AB_avg(A, B, P.MEND_NUM, db),
        "Mendeleev_number_AC_avg": helper.AC_avg(A, C, P.MEND_NUM, db),
        "Mendeleev_number_AD_avg": helper.AD_avg(A, D, P.MEND_NUM, db),
        "Mendeleev_number_BC_avg": helper.BC_avg(B, C, P.MEND_NUM, db),
        "Mendeleev_number_BD_avg": helper.BD_avg(B, D, P.MEND_NUM, db),
        "Mendeleev_number_CD_avg": helper.CD_avg(C, D, P.MEND_NUM, db),
        "Mendeleev_number_AB_weighted_norm": helper.AB_sum_weighted_norm(
            A, B, index_A_norm, index_B_norm, P.MEND_NUM, db
        ),
        "Mendeleev_number_AC_weighted_norm": helper.AC_sum_weighted_norm(
            A, C, index_A_norm, index_C_norm, P.MEND_NUM, db
        ),
        "Mendeleev_number_AD_weighted_norm": helper.AD_sum_weighted_norm(
            A, D, index_A_norm, index_D_norm, P.MEND_NUM, db
        ),
        "Mendeleev_number_BC_weighted_norm": helper.BC_sum_weighted_norm(
            B, C, index_B_norm, index_C_norm, P.MEND_NUM, db
        ),
        "Mendeleev_number_BD_weighted_norm": helper.BD_sum_weighted_norm(
            B, D, index_B_norm, index_D_norm, P.MEND_NUM, db
        ),
        "Mendeleev_number_CD_weighted_norm": helper.CD_sum_weighted_norm(
            C, D, index_C_norm, index_D_norm, P.MEND_NUM, db
        ),
    }

    # 13 features
    rest_properties_one = [
        P.VAL_TOTAL,
        P.UNPARIED_E,
        P.GILMAN,
    ]

    for p in rest_properties_one:
        p = p.value
        features.update(
            {
                f"{p}_A": db[A][p],
                f"{p}_B": db[B][p],
                f"{p}_C": db[C][p],
                f"{p}_D": db[D][p],
                f"{p}_ABCD_sum": helper.ABCD_sum(ABCD, p, db),
                f"{p}_ABCD_sum_weighted": helper.ABCD_sum_weighted(
                    ABCD, indices, p, db
                ),
                f"{p}_ABCD_sum_weighted_norm": helper.ABCD_sum_weighted_norm(
                    ABCD, indices_norm, p, db
                ),
                f"{p}_AB_sum_weighted_norm": helper.AB_sum_weighted_norm(
                    A, B, index_A_norm, index_B_norm, p, db
                ),
                f"{p}_AC_sum_weighted_norm": helper.AC_sum_weighted_norm(
                    A, C, index_A_norm, index_C_norm, p, db
                ),
                f"{p}_AD_sum_weighted_norm": helper.AD_sum_weighted_norm(
                    A, D, index_A_norm, index_D_norm, p, db
                ),
                f"{p}_BC_sum_weighted_norm": helper.BC_sum_weighted_norm(
                    B, C, index_B_norm, index_C_norm, p, db
                ),
                f"{p}_BD_sum_weighted_norm": helper.BD_sum_weighted_norm(
                    B, D, index_B_norm, index_D_norm, p, db
                ),
                f"{p}_CD_sum_weighted_norm": helper.CD_sum_weighted_norm(
                    C, D, index_C_norm, index_D_norm, p, db
                ),
            }
        )
    # Other 13 features
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

    for p in rest_properties_two:
        p = p.value
        features.update(
            {
                f"{p}_A": db[A][p],
                f"{p}_B": db[B][p],
                f"{p}_C": db[C][p],
                f"{p}_D": db[D][p],
                f"{p}_A/B": helper.A_by_B(A, B, p, db),
                f"{p}_A/C": helper.A_by_C(A, C, p, db),
                f"{p}_A/D": helper.A_by_D(A, D, p, db),
                f"{p}_B/C": helper.B_by_C(B, C, p, db),
                f"{p}_B/D": helper.B_by_D(B, D, p, db),
                f"{p}_C/D": helper.C_by_D(C, D, p, db),
                f"{p}_ABCD_max": helper.ABCD_max(ABCD, p, db),
                f"{p}_ABCD_min": helper.ABCD_min(ABCD, p, db),
                f"{p}_ABCD_avg": helper.ABCD_avg(ABCD, p, db),
            }
        )
    return features
