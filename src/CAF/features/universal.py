from bobleesj.utils.parsers.formula import Formula
from bobleesj.utils.sources.oliynyk import Property as P

from CAF.features.universal_helper import (
    avg_value,
    avg_weighted_norm,
    first_element_value,
    last_element_value,
    max_by_min_value,
    max_value,
    min_value,
)


def generate_features(formula: str, db: dict) -> dict:
    # Get the formula and index
    formula_obj = Formula(formula)
    norm_parsed_formula = formula_obj.get_normalized_parsed_formula()
    num_elements = formula_obj.element_count
    features = {
        "formula": formula,
        "index_norm_first_element": norm_parsed_formula[0][1],
        "index_norm_last_element": norm_parsed_formula[-1][1],
        "index_norm_max": max([i[1] for i in norm_parsed_formula]),
        "index_norm_min": min([i[1] for i in norm_parsed_formula]),
        "num_element": num_elements,
    }

    remaining_properties = [
        P.AW,
        P.ATOMIC_NUMBER,
        P.PERIOD,
        P.GROUP,
        P.MEND_NUM,
        P.VAL_TOTAL,
        P.UNPARIED_E,
        P.GILMAN,
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
    for prop in remaining_properties:
        prop = prop.value
        features.update(
            {
                f"{prop}_avg_weighted_norm": avg_weighted_norm(
                    norm_parsed_formula, prop, db
                ),
                f"{prop}_avg": avg_value(norm_parsed_formula, prop, db),
                f"{prop}_max": max_value(norm_parsed_formula, prop, db),
                f"{prop}_min": min_value(norm_parsed_formula, prop, db),
                f"{prop}_max_by_min": max_by_min_value(
                    norm_parsed_formula, prop, db
                ),
                f"{prop}_first_element": first_element_value(
                    norm_parsed_formula, prop, db
                ),
                f"{prop}_last_element": last_element_value(
                    norm_parsed_formula, prop, db
                ),
            }
        )
    return features
