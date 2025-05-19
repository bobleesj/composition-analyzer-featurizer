from bobleesj.utils.parsers.formula import Formula
from bobleesj.utils.sources.oliynyk import Property as P

from CAF.features.binary_helper import (
    A_by_B,
    A_minus_B,
    A_plus_B,
    A_plus_B_weighted,
    A_plus_B_weighted_norm,
    avg_value,
    max_value,
    min_value,
    prepare_binary_formula,
)


def generate_features(formula: str, db: dict) -> dict:
    """Generate features for a binary formula."""
    A, B, index_A, index_B, index_A_norm, index_B_norm = (
        prepare_binary_formula(formula)
    )
    index_max, index_min, index_avg = Formula(formula).max_min_avg_index

    features = {
        # index - 7 features
        "formula": formula,
        "index_A": index_A,
        "index_B": index_B,
        "index_A_norm": index_A_norm,
        "index_B_norm": index_B_norm,
        "index_max": index_max,
        "index_min": index_min,
        "index_avg": index_avg,
        # atomic_weight - 3 features
        "atomic_weight_A+B_weighted": A_plus_B_weighted(formula, P.AW, db),
        "atomic_weight_A/B": A_by_B(A, B, P.AW, db),
        "atomic_weight_A-B": A_minus_B(A, B, P.AW, db),
        # period - 2 features
        "period_A": db[A][P.PERIOD],
        "period_B": db[B][P.PERIOD],
        # group - 3 features
        "group_A": db[A][P.GROUP],
        "group_B": db[B][P.GROUP],
        "group_A-B": A_minus_B(A, B, P.GROUP, db),
        # Mendeleev number - 3 features
        "Mendeleev_number_A": db[A][P.MEND_NUM],
        "Mendeleev_number_B": db[B][P.MEND_NUM],
        "Mendeleev_number_A-B": A_minus_B(A, B, P.MEND_NUM, db),
        # valence total - 6 features
        "valencee_total_A": db[A][P.VAL_TOTAL],
        "valencee_total_B": db[B][P.VAL_TOTAL],
        "valencee_total_A-B": A_minus_B(A, B, P.VAL_TOTAL, db),
        "valencee_total_A+B": A_plus_B(A, B, P.VAL_TOTAL, db),
        "valencee_total_A+B_weighted": A_plus_B_weighted(
            formula, P.VAL_TOTAL, db
        ),
        "valencee_total_A+B_weighted_norm": A_plus_B_weighted_norm(
            formula, P.VAL_TOTAL, db
        ),
        # unpaired_electrons - 6 features
        "unpaired_electrons_A": db[A][P.UNPARIED_E],
        "unpaired_electrons_B": db[B][P.UNPARIED_E],
        "unpaired_electrons_A-B": A_minus_B(A, B, P.UNPARIED_E, db),
        "unpaired_electrons_A+B": A_plus_B(A, B, P.UNPARIED_E, db),
        "unpaired_electrons_A+B_weighted": A_plus_B_weighted(
            formula, P.UNPARIED_E, db
        ),
        "unpaired_electrons_A+B_weighted_norm": A_plus_B_weighted_norm(
            formula, P.UNPARIED_E, db
        ),
        # Gilman - 6 features
        "Gilman_A": db[A][P.GILMAN],
        "Gilman_B": db[B][P.GILMAN],
        "Gilman_A-B": A_minus_B(A, B, P.GILMAN, db),
        "Gilman_A+B": A_plus_B(A, B, P.GILMAN, db),
        "Gilman_A+B_weighted": A_plus_B_weighted(formula, P.GILMAN, db),
        "Gilman_A+B_weighted_norm": A_plus_B_weighted_norm(
            formula, P.GILMAN, db
        ),
        # Z_eff - 8 features
        "Z_eff_A": db[A][P.Z_EFF],
        "Z_eff_B": db[B][P.Z_EFF],
        "Z_eff_A-B": A_minus_B(A, B, P.Z_EFF, db),
        "Z_eff_A/B": A_by_B(A, B, P.Z_EFF, db),
        "Z_eff_max": max_value(A, B, P.Z_EFF, db),
        "Z_eff_min": min_value(A, B, P.Z_EFF, db),
        "Z_eff_avg": avg_value(A, B, P.Z_EFF, db),
        "Z_eff_A+B_weighted_norm": A_plus_B_weighted_norm(
            formula, P.Z_EFF, db
        ),
        # ionization_energy - 8 features
        "ionization_energy_A": db[A][P.ION_ENERGY],
        "ionization_energy_B": db[B][P.ION_ENERGY],
        "ionization_energy_A-B": A_minus_B(A, B, P.ION_ENERGY, db),
        "ionization_energy_A/B": A_by_B(A, B, P.ION_ENERGY, db),
        "ionization_energy_max": max_value(A, B, P.ION_ENERGY, db),
        "ionization_energy_min": min_value(A, B, P.ION_ENERGY, db),
        "ionization_energy_avg": avg_value(A, B, P.ION_ENERGY, db),
        "ionization_energy_A+B_weighted_norm": A_plus_B_weighted_norm(
            formula, P.ION_ENERGY, db
        ),
        # coordination_number - 3 features
        "coordination_number_A": db[A][P.COORD_NUM],
        "coordination_number_B": db[B][P.COORD_NUM],
        "coordination_number_A-B": A_minus_B(A, B, P.COORD_NUM, db),
        # ratio_closest - 5 features
        "ratio_closest_A": db[A][P.RATIO_CLOSEST],
        "ratio_closest_B": db[B][P.RATIO_CLOSEST],
        "ratio_closest_max": max_value(A, B, P.RATIO_CLOSEST, db),
        "ratio_closest_min": min_value(A, B, P.RATIO_CLOSEST, db),
        "ratio_closest_avg": avg_value(A, B, P.RATIO_CLOSEST, db),
        # polyhedron_distortion - 5 features
        "polyhedron_distortion_A": db[A][P.POLYHEDRON_DISTORT],
        "polyhedron_distortion_B": db[B][P.POLYHEDRON_DISTORT],
        "polyhedron_distortion_max": max_value(A, B, P.POLYHEDRON_DISTORT, db),
        "polyhedron_distortion_min": min_value(A, B, P.POLYHEDRON_DISTORT, db),
        "polyhedron_distortion_avg": avg_value(A, B, P.POLYHEDRON_DISTORT, db),
        # CIF_radius - 6 features
        "CIF_radius_A": db[A][P.CIF_RADIUS],
        "CIF_radius_B": db[B][P.CIF_RADIUS],
        "CIF_radius_A-B": A_minus_B(A, B, P.CIF_RADIUS, db),
        "CIF_radius_A/B": A_by_B(A, B, P.CIF_RADIUS, db),
        "CIF_radius_avg": avg_value(A, B, P.CIF_RADIUS, db),
        "CIF_radius_A+B_weighted_norm": A_plus_B_weighted_norm(
            formula, P.CIF_RADIUS, db
        ),
        # Pauling_radius_CN12 - 6 features
        "Pauling_radius_CN12_A": db[A][P.PAULING_RADIUS_CN12],
        "Pauling_radius_CN12_B": db[B][P.PAULING_RADIUS_CN12],
        "Pauling_radius_CN12_A-B": A_minus_B(A, B, P.PAULING_RADIUS_CN12, db),
        "Pauling_radius_CN12_A/B": A_by_B(A, B, P.PAULING_RADIUS_CN12, db),
        "Pauling_radius_CN12_avg": avg_value(A, B, P.PAULING_RADIUS_CN12, db),
        "Pauling_radius_CN12_A+B_weighted_norm": A_plus_B_weighted_norm(
            formula, P.CIF_RADIUS, db
        ),
    }
    # Rest of properties with exact 8 features
    rest_properties = [
        P.PAULING_EN,
        P.MARTYNOV_BATSANOV_EN,
        P.MELTING_POINT_K,
        P.DENSITY,
        P.SPECIFIC_HEAT,
        P.COHESIVE_ENERGY,
        P.BULK_MODULUS,
    ]

    for prop in rest_properties:
        prop = prop.value
        features.update(
            {
                f"{prop}_A": db[A][prop],
                f"{prop}_B": db[B][prop],
                f"{prop}_A-B": A_minus_B(A, B, prop, db),
                f"{prop}_A/B": A_by_B(A, B, prop, db),
                f"{prop}_max": max_value(A, B, prop, db),
                f"{prop}_min": min_value(A, B, prop, db),
                f"{prop}_avg": avg_value(A, B, prop, db),
                f"{prop}_A+B_weighted_norm": A_plus_B_weighted_norm(
                    formula, prop, db
                ),
            }
        )
    return features
