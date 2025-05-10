import numpy as np
import pandas as pd

from core.feature import property_data
from core.util import parser


def add_weighted_A_plus_B(df, property, temp_df):
    df[f"{property}_weighted_A+B"] = temp_df[f"{property}_A"] * temp_df["Index_A"]
    +temp_df[f"{property}_B"] * temp_df["Index_B"]
    return df


def add_weighted_norm_A_plus_B(df, property, temp_df):
    df[f"{property}_weighted_norm_A+B"] = (
        temp_df[f"{property}_A"] * temp_df["Normalized_Index_A"]
    )
    +temp_df[f"{property}_B"] * temp_df["Normalized_Index_B"]
    return df


def add_A_by_B(df, property, temp_df):
    df[f"{property}_A/B"] = temp_df[f"{property}_A"] / temp_df[f"{property}_B"]
    return df


def add_A_minus_B(df, property, temp_df):
    df[f"{property}_A-B"] = temp_df[f"{property}_A"] - temp_df[f"{property}_B"]
    return df


def add_A_plus_B(df, property, temp_df):
    df[f"{property}_A+B"] = temp_df[f"{property}_A"] + temp_df[f"{property}_B"]
    return df


def add_max_and_min(df, property, temp_df):
    df[f"{property}_max"] = temp_df[[f"{property}_A", f"{property}_B"]].max(axis=1)
    df[f"{property}_min"] = temp_df[[f"{property}_A", f"{property}_B"]].min(axis=1)
    return df


def add_avg(df, property, temp_df):
    df[f"{property}_avg"] = temp_df[[f"{property}_A", f"{property}_B"]].mean(axis=1)
    return df


def add_A_and_B(df, property, temp_df):
    df[f"{property}_A"] = temp_df[f"{property}_A"]
    df[f"{property}_B"] = temp_df[f"{property}_B"]
    return df


def add_A_exp_and_B_exp(df, property, temp_df):
    df[f"{property}_A_exp"] = temp_df[f"{property}_A"].apply(np.exp)
    df[f"{property}_B_exp"] = temp_df[f"{property}_B"].apply(np.exp)
    return df


def add_A_exp_neg_and_B_exp_neg(df, property, temp_df):
    df[f"{property}_A_exp_neg"] = temp_df[f"{property}_A"].apply(lambda x: np.exp(-x))
    df[f"{property}_B_exp_neg"] = temp_df[f"{property}_B"].apply(lambda x: np.exp(-x))
    return df


def add_A_inverse_and_B_inverse(df, property, temp_df):
    df[f"{property}_A_inverse"] = temp_df[f"{property}_A"].apply(lambda x: 1 / x)
    df[f"{property}_B_inverse"] = temp_df[f"{property}_B"].apply(lambda x: 1 / x)
    return df


def add_A_square_and_B_square(df, property, temp_df):
    df[f"{property}_A_square"] = temp_df[f"{property}_A"].apply(np.square)
    df[f"{property}_B_square"] = temp_df[f"{property}_B"].apply(np.square)
    return df


def add_A_cube_and_B_cube(df, property, temp_df):
    df[f"{property}_A_cube"] = temp_df[f"{property}_A"].apply(lambda x: x**3)
    df[f"{property}_B_cube"] = temp_df[f"{property}_B"].apply(lambda x: x**3)
    return df


def add_A_sqrt_and_B_sqrt(df, property, temp_df):
    df[f"{property}_A_sqrt"] = temp_df[f"{property}_A"].apply(np.sqrt)
    df[f"{property}_B_sqrt"] = temp_df[f"{property}_B"].apply(np.sqrt)
    return df


def add_A_cbrt_and_B_cbrt(df, property, temp_df):
    df[f"{property}_A_cbrt"] = temp_df[f"{property}_A"].apply(np.cbrt)
    df[f"{property}_B_cbrt"] = temp_df[f"{property}_B"].apply(np.cbrt)
    return df


def add_A_log_and_B_log(df, property, temp_df):
    df[f"{property}_A_log"] = temp_df[f"{property}_A"].apply(np.log)
    df[f"{property}_B_log"] = temp_df[f"{property}_B"].apply(np.log)
    return df


def add_A_abs_and_B_abs(df, property, temp_df):
    df[f"{property}_A_abs"] = temp_df[f"{property}_A"].apply(np.abs)
    df[f"{property}_B_abs"] = temp_df[f"{property}_B"].apply(np.abs)
    return df


def add_A_sixth_and_B_sixth(df, property, temp_df):
    df[f"{property}_A_sixth"] = temp_df[f"{property}_A"].apply(lambda x: x**6)
    df[f"{property}_B_sixth"] = temp_df[f"{property}_B"].apply(lambda x: x**6)
    return df


def add_A_sin_and_B_sin(df, property, temp_df):
    df[f"{property}_A_sin"] = temp_df[f"{property}_A"].apply(np.sin)
    df[f"{property}_B_sin"] = temp_df[f"{property}_B"].apply(np.sin)
    return df


def add_A_cos_and_B_cos(df, property, temp_df):
    df[f"{property}_A_cos"] = temp_df[f"{property}_A"].apply(np.cos)
    df[f"{property}_B_cos"] = temp_df[f"{property}_B"].apply(np.cos)
    return df


def generate_binary_features(formulas):
    # Set display option to show all columns
    pd.set_option("display.max_columns", None)
    temp_df = parser.get_parsed_binary_formula_df(formulas)
    # Additional feature calculations

    oliynyk_df = property_data.get_processed_oliynyk_df()

    # Drop the first column
    oliynyk_df.drop(oliynyk_df.columns[0], axis=1, inplace=True)

    # Drop the last 5 columns from oliynyk_df
    oliynyk_df = oliynyk_df.iloc[:, :-5]

    # Set index to 'symbol' for easier mapping
    oliynyk_indexed = oliynyk_df.set_index("symbol")

    # Loop through each column in oliynyk_indexed and map it
    for column in oliynyk_indexed.columns:
        temp_df[f"{column}_A"] = (
            temp_df["Element A"].map(oliynyk_indexed[column]).astype(float)
        )
        temp_df[f"{column}_B"] = (
            temp_df["Element B"].map(oliynyk_indexed[column]).astype(float)
        )

    # String
    atomic_weight_string = "atomic_weight"
    group_string = "group"
    period_string = "period"
    Mendeleev_number_string = "Mendeleev_number"
    valencee_total_string = "valencee_total"
    unpaired_electrons_string = "unpaired_electrons"
    Gilman_string = "Gilman"
    Z_eff_string = "Z_eff"
    ionization_energy_string = "ionization_energy"
    coordination_number_string = "coordination_number"
    ratio_closest_string = "ratio_closest"
    polyhedron_distortion_string = "polyhedron_distortion"
    CIF_radius_string = "CIF_radius"
    Pauling_radius_CN12_string = "Pauling_radius_CN12"
    Pauling_EN_string = "Pauling_EN"
    Martynov_Batsanov_EN_string = "Martynov_Batsanov_EN"
    melting_point_K_string = "melting_point_K"
    density_string = "density"
    specific_heat_string = "specific_heat"
    cohesive_energy_string = "cohesive_energy"
    bulk_modulus_string = "bulk_modulus"

    df = pd.DataFrame()
    df["Formula"] = temp_df["Formula"]
    df["index_A"] = temp_df["Index_A"]
    df["index_B"] = temp_df["Index_B"]
    df["normalized_index_A"] = temp_df["Normalized_Index_A"]
    df["normalized_index_B"] = temp_df["Normalized_Index_B"]
    df["largest_index"] = temp_df[["Index_A", "Index_B"]].max(axis=1)
    df["smallest_index"] = temp_df[["Index_A", "Index_B"]].min(axis=1)
    df["avg_index"] = (temp_df["Index_A"] + temp_df["Index_B"]) / 2

    # atomic_weight
    df = add_weighted_A_plus_B(df, atomic_weight_string, temp_df)
    df = add_A_by_B(df, atomic_weight_string, temp_df)
    df = add_A_minus_B(df, atomic_weight_string, temp_df)

    # period
    df = add_A_and_B(df, period_string, temp_df)

    # group
    df = add_A_and_B(df, group_string, temp_df)
    df = add_A_minus_B(df, group_string, temp_df)

    # # Mendeleev_number
    df = add_A_and_B(df, Mendeleev_number_string, temp_df)
    df = add_A_minus_B(df, Mendeleev_number_string, temp_df)

    # valencee_total
    df = add_A_and_B(df, valencee_total_string, temp_df)
    df = add_A_minus_B(df, valencee_total_string, temp_df)
    df = add_A_plus_B(df, valencee_total_string, temp_df)
    df = add_weighted_A_plus_B(df, valencee_total_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, valencee_total_string, temp_df)

    # unpaired_electrons
    df = add_A_and_B(df, unpaired_electrons_string, temp_df)
    df = add_A_minus_B(df, unpaired_electrons_string, temp_df)
    df = add_A_plus_B(df, unpaired_electrons_string, temp_df)
    df = add_weighted_A_plus_B(df, unpaired_electrons_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, unpaired_electrons_string, temp_df)

    # # Gilman
    df = add_A_and_B(df, Gilman_string, temp_df)
    df = add_A_minus_B(df, Gilman_string, temp_df)
    df = add_A_plus_B(df, Gilman_string, temp_df)
    df = add_weighted_A_plus_B(df, Gilman_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, Gilman_string, temp_df)

    # # Z_eff
    df = add_A_and_B(df, Z_eff_string, temp_df)
    df = add_A_minus_B(df, Z_eff_string, temp_df)
    df = add_A_by_B(df, Z_eff_string, temp_df)
    df = add_max_and_min(df, Z_eff_string, temp_df)
    df = add_avg(df, Z_eff_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, Z_eff_string, temp_df)

    # ionization_energy
    df = add_A_and_B(df, ionization_energy_string, temp_df)
    df = add_A_minus_B(df, ionization_energy_string, temp_df)
    df = add_A_by_B(df, ionization_energy_string, temp_df)
    df = add_max_and_min(df, ionization_energy_string, temp_df)
    df = add_avg(df, ionization_energy_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, ionization_energy_string, temp_df)

    # coordination_number
    df = add_A_and_B(df, coordination_number_string, temp_df)
    df = add_A_minus_B(df, coordination_number_string, temp_df)

    # ratio_closest
    df = add_A_and_B(df, ratio_closest_string, temp_df)
    df = add_max_and_min(df, ratio_closest_string, temp_df)
    df = add_avg(df, ratio_closest_string, temp_df)

    # polyhedron_distortion
    df = add_A_and_B(df, polyhedron_distortion_string, temp_df)
    df = add_max_and_min(df, polyhedron_distortion_string, temp_df)
    df = add_avg(df, polyhedron_distortion_string, temp_df)

    # CIF_radius
    df = add_A_and_B(df, CIF_radius_string, temp_df)
    df = add_A_by_B(df, CIF_radius_string, temp_df)
    df = add_A_minus_B(df, CIF_radius_string, temp_df)
    df = add_avg(df, CIF_radius_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, CIF_radius_string, temp_df)

    # Pauling_radius_CN12
    df = add_A_and_B(df, Pauling_radius_CN12_string, temp_df)
    df = add_A_by_B(df, Pauling_radius_CN12_string, temp_df)
    df = add_A_minus_B(df, Pauling_radius_CN12_string, temp_df)
    df = add_avg(df, Pauling_radius_CN12_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, Pauling_radius_CN12_string, temp_df)

    # Pauling_EN
    df = add_A_and_B(df, Pauling_EN_string, temp_df)
    df = add_A_minus_B(df, Pauling_EN_string, temp_df)
    df = add_A_by_B(df, Pauling_EN_string, temp_df)
    df = add_max_and_min(df, Pauling_EN_string, temp_df)
    df = add_avg(df, Pauling_EN_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, Pauling_EN_string, temp_df)

    # Martynov_Batsanov_EN
    df = add_A_and_B(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_A_minus_B(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_A_by_B(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_max_and_min(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_avg(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, Martynov_Batsanov_EN_string, temp_df)

    # melting_point_K
    df = add_A_and_B(df, melting_point_K_string, temp_df)
    df = add_A_minus_B(df, melting_point_K_string, temp_df)
    df = add_A_by_B(df, melting_point_K_string, temp_df)
    df = add_max_and_min(df, melting_point_K_string, temp_df)
    df = add_avg(df, melting_point_K_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, melting_point_K_string, temp_df)

    # density
    df = add_A_and_B(df, density_string, temp_df)
    df = add_A_minus_B(df, density_string, temp_df)
    df = add_A_by_B(df, density_string, temp_df)
    df = add_max_and_min(df, density_string, temp_df)
    df = add_avg(df, density_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, density_string, temp_df)

    # specific_heat
    df = add_A_and_B(df, specific_heat_string, temp_df)
    df = add_A_minus_B(df, specific_heat_string, temp_df)
    df = add_A_by_B(df, specific_heat_string, temp_df)
    df = add_max_and_min(df, specific_heat_string, temp_df)
    df = add_avg(df, specific_heat_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, specific_heat_string, temp_df)

    # cohesive_energy
    df = add_A_and_B(df, cohesive_energy_string, temp_df)
    df = add_A_minus_B(df, cohesive_energy_string, temp_df)
    df = add_A_by_B(df, cohesive_energy_string, temp_df)
    df = add_max_and_min(df, cohesive_energy_string, temp_df)
    df = add_avg(df, cohesive_energy_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, cohesive_energy_string, temp_df)

    # bulk_modulus
    df = add_A_and_B(df, bulk_modulus_string, temp_df)
    df = add_A_minus_B(df, bulk_modulus_string, temp_df)
    df = add_A_by_B(df, bulk_modulus_string, temp_df)
    df = add_max_and_min(df, bulk_modulus_string, temp_df)
    df = add_avg(df, bulk_modulus_string, temp_df)
    df = add_weighted_norm_A_plus_B(df, bulk_modulus_string, temp_df)
    # prompt.print_column_names_from_df(df)

    return df
