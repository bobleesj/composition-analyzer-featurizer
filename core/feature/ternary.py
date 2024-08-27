from warnings import simplefilter

import numpy as np
import pandas as pd

from core.feature import property_data
from core.util import parser, prompt

simplefilter(action="ignore", category=pd.errors.PerformanceWarning)


def add_R_M_X(df, property, temp_df):
    df[f"{property}_R"] = temp_df[f"{property}_R"]
    df[f"{property}_M"] = temp_df[f"{property}_M"]
    df[f"{property}_X"] = temp_df[f"{property}_X"]
    return df


def add_R_by_M(df, property, temp_df):
    df[f"{property}_R/M"] = temp_df[f"{property}_R"] / temp_df[f"{property}_M"]
    return df


def add_M_by_X(df, property, temp_df):
    df[f"{property}_M/X"] = temp_df[f"{property}_M"] / temp_df[f"{property}_X"]
    return df


def add_R_by_X(df, property, temp_df):
    df[f"{property}_R/X"] = temp_df[f"{property}_R"] / temp_df[f"{property}_X"]
    return df


def add_weighted_sum_RMX(df, property, temp_df):
    df[f"{property}_weighted_RMX"] = temp_df[f"{property}_R"] * temp_df["Index_M"]
    +temp_df[f"{property}_M"] * temp_df["Index_M"]
    +temp_df[f"{property}_X"] * temp_df["Index_X"]
    return df


def add_R_minus_M(df, property, temp_df):
    df[f"{property}_R-M"] = temp_df[f"{property}_R"] - temp_df[f"{property}_M"]
    return df


def add_M_minus_X(df, property, temp_df):
    df[f"{property}_M-X"] = temp_df[f"{property}_M"] - temp_df[f"{property}_X"]
    return df


def add_R_minus_X(df, property, temp_df):
    df[f"{property}_R-X"] = temp_df[f"{property}_R"] - temp_df[f"{property}_X"]
    return df


def add_avg_RMX(df, property, temp_df):
    df[f"{property}_avg_RMX"] = temp_df[
        [f"{property}_R", f"{property}_M", f"{property}_X"]
    ].mean(axis=1)
    return df


def add_avg_RM(df, property, temp_df):
    df[f"{property}_avg_RM"] = temp_df[[f"{property}_R", f"{property}_M"]].mean(axis=1)
    return df


def add_avg_MX(df, property, temp_df):
    df[f"{property}_avg_MX"] = temp_df[[f"{property}_M", f"{property}_X"]].mean(axis=1)
    return df


def add_avg_RX(df, property, temp_df):
    df[f"{property}_avg_RX"] = temp_df[[f"{property}_R", f"{property}_X"]].mean(axis=1)
    return df


def add_avg_weighted_RMX(df, property, temp_df):
    df[f"{property}_avg_weighted_RMX"] = (
        temp_df[f"{property}_R"] * temp_df["Index_R"]
        + temp_df[f"{property}_M"] * temp_df["Index_M"]
        + temp_df[f"{property}_X"] * temp_df["Index_X"]
    ) / (temp_df["Index_R"] + temp_df["Index_M"] + temp_df["Index_X"])
    return df


def add_weighted_norm_RMX(df, property, temp_df):
    # Calculate the weighted sum of R, M, and X
    weighted_sum = (
        temp_df[f"{property}_R"] * temp_df["Normalized_Index_R"]
        + temp_df[f"{property}_M"] * temp_df["Normalized_Index_M"]
        + temp_df[f"{property}_X"] * temp_df["Normalized_Index_X"]
    )

    normalized_weighted_sum = weighted_sum / (
        temp_df["Normalized_Index_R"]
        + temp_df["Normalized_Index_M"]
        + temp_df["Normalized_Index_X"]
    )

    # Assign the result to the DataFrame
    df[f"{property}_weighted_norm_RMX"] = normalized_weighted_sum

    return df


def add_weighted_norm_RM(df, property, temp_df):
    # Calculate the weighted sum of R and M
    weighted_sum = (
        temp_df[f"{property}_R"] * temp_df["Normalized_Index_R"]
        + temp_df[f"{property}_M"] * temp_df["Normalized_Index_M"]
    )

    # Normalize the weighted sum
    normalized_weighted_sum = weighted_sum / (
        temp_df["Normalized_Index_R"] + temp_df["Normalized_Index_M"]
    )

    # Assign the result to the DataFrame
    df[f"{property}_weighted_norm_RM"] = normalized_weighted_sum

    return df


def add_weighted_norm_MX(df, property, temp_df):
    # Calculate the weighted sum of M and X
    weighted_sum = (
        temp_df[f"{property}_M"] * temp_df["Normalized_Index_M"]
        + temp_df[f"{property}_X"] * temp_df["Normalized_Index_X"]
    )

    # Normalize the weighted sum
    normalized_weighted_sum = weighted_sum / (
        temp_df["Normalized_Index_M"] + temp_df["Normalized_Index_X"]
    )

    # Assign the result to the DataFrame
    df[f"{property}_weighted_norm_MX"] = normalized_weighted_sum

    return df


def add_weighted_norm_RX(df, property, temp_df):
    # Calculate the weighted sum of R and X
    weighted_sum = (
        temp_df[f"{property}_R"] * temp_df["Normalized_Index_R"]
        + temp_df[f"{property}_X"] * temp_df["Normalized_Index_X"]
    )

    # Normalize the weighted sum
    normalized_weighted_sum = weighted_sum / (
        temp_df["Normalized_Index_R"] + temp_df["Normalized_Index_X"]
    )

    # Assign the result to the DataFrame
    df[f"{property}_weighted_norm_RX"] = normalized_weighted_sum

    return df


def add_max_and_min(df, property, temp_df):
    df[f"{property}_max"] = temp_df[
        [f"{property}_R", f"{property}_M", f"{property}_X"]
    ].max(axis=1)
    df[f"{property}_min"] = temp_df[
        [f"{property}_R", f"{property}_M", f"{property}_X"]
    ].min(axis=1)
    return df


def add_sum_RMX(df, property, temp_df):
    df[f"{property}_sum"] = temp_df[
        [f"{property}_R", f"{property}_M", f"{property}_X"]
    ].sum(axis=1)
    return df


def add_R_and_M_and_X(df, property, temp_df):
    df[f"{property}_R"] = temp_df[f"{property}_R"]
    df[f"{property}_M"] = temp_df[f"{property}_M"]
    df[f"{property}_X"] = temp_df[f"{property}_X"]
    return df


def add_R_exp_and_M_exp_and_X_exp(df, property, temp_df):
    df[f"{property}_R_exp"] = temp_df[f"{property}_R"].apply(np.exp)
    df[f"{property}_M_exp"] = temp_df[f"{property}_M"].apply(np.exp)
    df[f"{property}_X_exp"] = temp_df[f"{property}_X"].apply(np.exp)
    return df


def add_R_exp_neg_and_M_exp_neg_and_X_exp_neg(df, property, temp_df):
    df[f"{property}_R_exp_neg"] = temp_df[f"{property}_R"].apply(lambda x: np.exp(-x))
    df[f"{property}_M_exp_neg"] = temp_df[f"{property}_M"].apply(lambda x: np.exp(-x))
    df[f"{property}_X_exp_neg"] = temp_df[f"{property}_X"].apply(lambda x: np.exp(-x))
    return df


def add_R_inverse_and_M_inverse_and_X_inverse(df, property, temp_df):
    df[f"{property}_R_inverse"] = temp_df[f"{property}_R"].apply(lambda x: 1 / x)
    df[f"{property}_M_inverse"] = temp_df[f"{property}_M"].apply(lambda x: 1 / x)
    df[f"{property}_X_inverse"] = temp_df[f"{property}_X"].apply(lambda x: 1 / x)
    return df


def add_R_square_and_M_square_and_X_square(df, property, temp_df):
    df[f"{property}_R_square"] = temp_df[f"{property}_R"].apply(np.square)
    df[f"{property}_M_square"] = temp_df[f"{property}_M"].apply(np.square)
    df[f"{property}_X_square"] = temp_df[f"{property}_X"].apply(np.square)
    return df


def add_R_cube_and_M_cube_and_X_cube(df, property, temp_df):
    df[f"{property}_R_cube"] = temp_df[f"{property}_R"].apply(lambda x: x**3)
    df[f"{property}_M_cube"] = temp_df[f"{property}_M"].apply(lambda x: x**3)
    df[f"{property}_X_cube"] = temp_df[f"{property}_X"].apply(lambda x: x**3)
    return df


def add_R_sqrt_and_M_sqrt_and_X_sqrt(df, property, temp_df):
    df[f"{property}_R_sqrt"] = temp_df[f"{property}_R"].apply(np.sqrt)
    df[f"{property}_M_sqrt"] = temp_df[f"{property}_M"].apply(np.sqrt)
    df[f"{property}_X_sqrt"] = temp_df[f"{property}_X"].apply(np.sqrt)
    return df


def add_R_cbrt_and_M_cbrt_and_X_cbrt(df, property, temp_df):
    df[f"{property}_R_cbrt"] = temp_df[f"{property}_R"].apply(np.cbrt)
    df[f"{property}_M_cbrt"] = temp_df[f"{property}_M"].apply(np.cbrt)
    df[f"{property}_X_cbrt"] = temp_df[f"{property}_X"].apply(np.cbrt)
    return df


def add_R_log_and_M_log_and_X_log(df, property, temp_df):
    df[f"{property}_R_log"] = temp_df[f"{property}_R"].apply(np.log)
    df[f"{property}_M_log"] = temp_df[f"{property}_M"].apply(np.log)
    df[f"{property}_X_log"] = temp_df[f"{property}_X"].apply(np.log)
    return df


def add_R_abs_and_M_abs_and_X_abs(df, property, temp_df):
    df[f"{property}_R_abs"] = temp_df[f"{property}_R"].apply(np.abs)
    df[f"{property}_M_abs"] = temp_df[f"{property}_M"].apply(np.abs)
    df[f"{property}_X_abs"] = temp_df[f"{property}_X"].apply(np.abs)
    return df


def add_R_sixth_and_M_sixth_and_X_sixth(df, property, temp_df):
    df[f"{property}_R_sixth"] = temp_df[f"{property}_R"].apply(lambda x: x**6)
    df[f"{property}_M_sixth"] = temp_df[f"{property}_M"].apply(lambda x: x**6)
    df[f"{property}_X_sixth"] = temp_df[f"{property}_X"].apply(lambda x: x**6)
    return df


def add_R_sin_and_M_sin_and_X_sin(df, property, temp_df):
    df[f"{property}_R_sin"] = temp_df[f"{property}_R"].apply(np.sin)
    df[f"{property}_M_sin"] = temp_df[f"{property}_M"].apply(np.sin)
    df[f"{property}_X_sin"] = temp_df[f"{property}_X"].apply(np.sin)
    return df


def add_R_cos_and_M_cos_and_X_cos(df, property, temp_df):
    df[f"{property}_R_cos"] = temp_df[f"{property}_R"].apply(np.cos)
    df[f"{property}_M_cos"] = temp_df[f"{property}_M"].apply(np.cos)
    df[f"{property}_X_cos"] = temp_df[f"{property}_X"].apply(np.cos)
    return df


def generate_ternary_features(formulas):
    temp_df = parser.get_parsed_ternary_formula_df(formulas)
    oliynyk_df = property_data.get_processed_oliynyk_df()
    # Drop the first column
    oliynyk_df.drop(oliynyk_df.columns[0], axis=1, inplace=True)

    # Drop the last 5 columns from oliynyk_df
    oliynyk_df = oliynyk_df.iloc[:, :-5]

    # Set index to 'symbol' for easier mapping
    oliynyk_indexed = oliynyk_df.set_index("symbol")

    # Loop through each column in oliynyk_indexed and map it
    for column in oliynyk_indexed.columns:
        temp_df[f"{column}_R"] = (
            temp_df["Element R"].map(oliynyk_indexed[column]).astype(float)
        )
        temp_df[f"{column}_M"] = (
            temp_df["Element M"].map(oliynyk_indexed[column]).astype(float)
        )
        temp_df[f"{column}_X"] = (
            temp_df["Element X"].map(oliynyk_indexed[column]).astype(float)
        )

    # String
    atomic_weight_string = "atomic_weight"
    atomic_number_string = "atomic_number"
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

    # Set display option to show all columns
    pd.set_option("display.max_columns", None)

    # index
    df = pd.DataFrame()
    df["Formula"] = temp_df["Formula"]
    df["index_R"] = temp_df["Index_R"]
    df["index_M"] = temp_df["Index_M"]
    df["index_X"] = temp_df["Index_X"]
    df["normalized_index_R"] = temp_df["Normalized_Index_R"]
    df["normalized_index_M"] = temp_df["Normalized_Index_M"]
    df["normalized_index_X"] = temp_df["Normalized_Index_X"]
    df["largest_index"] = temp_df[["Index_R", "Index_M", "Index_X"]].max(axis=1)
    df["smallest_index"] = temp_df[["Index_R", "Index_M", "Index_X"]].min(axis=1)
    df["avg_index"] = (temp_df["Index_R"] + temp_df["Index_M"] + temp_df["Index_X"]) / 3

    # atomic_weight
    df = add_weighted_sum_RMX(df, atomic_weight_string, temp_df)
    df = add_R_by_M(df, atomic_weight_string, temp_df)
    df = add_M_by_X(df, atomic_weight_string, temp_df)
    df = add_R_by_X(df, atomic_weight_string, temp_df)

    # atomic_number
    df = add_R_minus_M(df, atomic_number_string, temp_df)
    df = add_M_minus_X(df, atomic_number_string, temp_df)
    df = add_R_minus_X(df, atomic_number_string, temp_df)
    df = add_avg_RMX(df, atomic_number_string, temp_df)
    df = add_avg_weighted_RMX(df, atomic_number_string, temp_df)
    df = add_avg_RM(df, atomic_number_string, temp_df)
    df = add_avg_MX(df, atomic_number_string, temp_df)
    df = add_avg_RX(df, atomic_number_string, temp_df)

    # period
    df = add_R_M_X(df, period_string, temp_df)
    df = add_weighted_norm_RMX(df, period_string, temp_df)
    df = add_weighted_norm_RM(df, period_string, temp_df)
    df = add_weighted_norm_MX(df, period_string, temp_df)
    df = add_weighted_norm_RX(df, period_string, temp_df)

    # group
    df = add_R_M_X(df, group_string, temp_df)
    df = add_R_minus_M(df, group_string, temp_df)
    df = add_M_minus_X(df, group_string, temp_df)
    df = add_R_minus_X(df, group_string, temp_df)
    df = add_weighted_norm_RMX(df, group_string, temp_df)
    df = add_weighted_norm_RM(df, group_string, temp_df)
    df = add_weighted_norm_MX(df, group_string, temp_df)
    df = add_weighted_norm_RX(df, group_string, temp_df)

    # Mendeleev_number
    df = add_R_M_X(df, Mendeleev_number_string, temp_df)
    df = add_R_minus_M(df, Mendeleev_number_string, temp_df)
    df = add_M_minus_X(df, Mendeleev_number_string, temp_df)
    df = add_R_minus_X(df, Mendeleev_number_string, temp_df)

    df = add_avg_RMX(df, Mendeleev_number_string, temp_df)
    df = add_avg_weighted_RMX(df, Mendeleev_number_string, temp_df)

    df = add_avg_RM(df, Mendeleev_number_string, temp_df)
    df = add_avg_MX(df, Mendeleev_number_string, temp_df)
    df = add_avg_RX(df, Mendeleev_number_string, temp_df)

    df = add_weighted_norm_RM(df, Mendeleev_number_string, temp_df)
    df = add_weighted_norm_MX(df, Mendeleev_number_string, temp_df)
    df = add_weighted_norm_RX(df, Mendeleev_number_string, temp_df)

    # valencee_total
    df = add_R_M_X(df, valencee_total_string, temp_df)
    df = add_sum_RMX(df, valencee_total_string, temp_df)
    df = add_weighted_sum_RMX(df, valencee_total_string, temp_df)
    df = add_weighted_norm_RMX(df, valencee_total_string, temp_df)
    df = add_weighted_norm_RM(df, valencee_total_string, temp_df)
    df = add_weighted_norm_MX(df, valencee_total_string, temp_df)
    df = add_weighted_norm_RX(df, valencee_total_string, temp_df)

    # unpaired_electrons
    df = add_R_M_X(df, unpaired_electrons_string, temp_df)
    df = add_sum_RMX(df, unpaired_electrons_string, temp_df)
    df = add_weighted_sum_RMX(df, unpaired_electrons_string, temp_df)
    df = add_weighted_norm_RMX(df, unpaired_electrons_string, temp_df)
    df = add_weighted_norm_RM(df, unpaired_electrons_string, temp_df)
    df = add_weighted_norm_MX(df, unpaired_electrons_string, temp_df)
    df = add_weighted_norm_RX(df, unpaired_electrons_string, temp_df)

    # Gilman
    df = add_R_M_X(df, Gilman_string, temp_df)
    df = add_sum_RMX(df, Gilman_string, temp_df)
    df = add_weighted_sum_RMX(df, Gilman_string, temp_df)
    df = add_weighted_norm_RMX(df, Gilman_string, temp_df)
    df = add_weighted_norm_RM(df, Gilman_string, temp_df)
    df = add_weighted_norm_MX(df, Gilman_string, temp_df)
    df = add_weighted_norm_RX(df, Gilman_string, temp_df)

    # # Z_eff
    df = add_R_M_X(df, Z_eff_string, temp_df)
    df = add_R_by_M(df, Z_eff_string, temp_df)
    df = add_M_by_X(df, Z_eff_string, temp_df)
    df = add_R_by_X(df, Z_eff_string, temp_df)
    df = add_max_and_min(df, Z_eff_string, temp_df)
    df = add_avg_RMX(df, Z_eff_string, temp_df)

    # ionization_energy
    df = add_R_M_X(df, ionization_energy_string, temp_df)
    df = add_R_by_M(df, ionization_energy_string, temp_df)
    df = add_M_by_X(df, ionization_energy_string, temp_df)
    df = add_R_by_X(df, ionization_energy_string, temp_df)
    df = add_max_and_min(df, ionization_energy_string, temp_df)
    df = add_avg_RMX(df, ionization_energy_string, temp_df)

    # coordination_number
    df = add_R_M_X(df, coordination_number_string, temp_df)
    df = add_R_by_M(df, coordination_number_string, temp_df)
    df = add_M_by_X(df, coordination_number_string, temp_df)
    df = add_R_by_X(df, coordination_number_string, temp_df)
    df = add_max_and_min(df, coordination_number_string, temp_df)
    df = add_avg_RMX(df, coordination_number_string, temp_df)

    # ratio_closest
    df = add_R_M_X(df, ratio_closest_string, temp_df)
    df = add_R_by_M(df, ratio_closest_string, temp_df)
    df = add_M_by_X(df, ratio_closest_string, temp_df)
    df = add_R_by_X(df, ratio_closest_string, temp_df)
    df = add_max_and_min(df, ratio_closest_string, temp_df)
    df = add_avg_RMX(df, ratio_closest_string, temp_df)

    # polyhedron_distortion
    df = add_R_M_X(df, polyhedron_distortion_string, temp_df)
    df = add_R_by_M(df, polyhedron_distortion_string, temp_df)
    df = add_M_by_X(df, polyhedron_distortion_string, temp_df)
    df = add_R_by_X(df, polyhedron_distortion_string, temp_df)
    df = add_max_and_min(df, polyhedron_distortion_string, temp_df)
    df = add_avg_RMX(df, polyhedron_distortion_string, temp_df)

    # CIF_radius
    df = add_R_M_X(df, CIF_radius_string, temp_df)
    df = add_R_by_M(df, CIF_radius_string, temp_df)
    df = add_M_by_X(df, CIF_radius_string, temp_df)
    df = add_R_by_X(df, CIF_radius_string, temp_df)
    df = add_max_and_min(df, CIF_radius_string, temp_df)
    df = add_avg_RMX(df, CIF_radius_string, temp_df)

    # Pauling_radius_CN12
    df = add_R_M_X(df, Pauling_radius_CN12_string, temp_df)
    df = add_R_by_M(df, Pauling_radius_CN12_string, temp_df)
    df = add_M_by_X(df, Pauling_radius_CN12_string, temp_df)
    df = add_R_by_X(df, Pauling_radius_CN12_string, temp_df)
    df = add_max_and_min(df, Pauling_radius_CN12_string, temp_df)
    df = add_avg_RMX(df, Pauling_radius_CN12_string, temp_df)

    # Pauling_EN
    df = add_R_M_X(df, Pauling_EN_string, temp_df)
    df = add_R_by_M(df, Pauling_EN_string, temp_df)
    df = add_M_by_X(df, Pauling_EN_string, temp_df)
    df = add_R_by_X(df, Pauling_EN_string, temp_df)
    df = add_max_and_min(df, Pauling_EN_string, temp_df)
    df = add_avg_RMX(df, Pauling_EN_string, temp_df)

    # Martynov_Batsanov_EN
    df = add_R_M_X(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_R_by_M(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_M_by_X(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_R_by_X(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_max_and_min(df, Martynov_Batsanov_EN_string, temp_df)
    df = add_avg_RMX(df, Martynov_Batsanov_EN_string, temp_df)

    # melting_point_K
    df = add_R_M_X(df, melting_point_K_string, temp_df)
    df = add_R_by_M(df, melting_point_K_string, temp_df)
    df = add_M_by_X(df, melting_point_K_string, temp_df)
    df = add_R_by_X(df, melting_point_K_string, temp_df)
    df = add_max_and_min(df, melting_point_K_string, temp_df)
    df = add_avg_RMX(df, melting_point_K_string, temp_df)

    # density
    df = add_R_M_X(df, density_string, temp_df)
    df = add_R_by_M(df, density_string, temp_df)
    df = add_M_by_X(df, density_string, temp_df)
    df = add_R_by_X(df, density_string, temp_df)
    df = add_max_and_min(df, density_string, temp_df)
    df = add_avg_RMX(df, density_string, temp_df)

    # specific_heat
    df = add_R_M_X(df, specific_heat_string, temp_df)
    df = add_R_by_M(df, specific_heat_string, temp_df)
    df = add_M_by_X(df, specific_heat_string, temp_df)
    df = add_R_by_X(df, specific_heat_string, temp_df)
    df = add_max_and_min(df, specific_heat_string, temp_df)
    df = add_avg_RMX(df, specific_heat_string, temp_df)

    # cohesive_energy
    df = add_R_M_X(df, cohesive_energy_string, temp_df)
    df = add_R_by_M(df, cohesive_energy_string, temp_df)
    df = add_M_by_X(df, cohesive_energy_string, temp_df)
    df = add_R_by_X(df, cohesive_energy_string, temp_df)
    df = add_max_and_min(df, cohesive_energy_string, temp_df)
    df = add_avg_RMX(df, cohesive_energy_string, temp_df)

    # bulk_modulus
    df = add_R_M_X(df, bulk_modulus_string, temp_df)
    df = add_R_by_M(df, bulk_modulus_string, temp_df)
    df = add_M_by_X(df, bulk_modulus_string, temp_df)
    df = add_R_by_X(df, bulk_modulus_string, temp_df)
    df = add_max_and_min(df, bulk_modulus_string, temp_df)
    df = add_avg_RMX(df, bulk_modulus_string, temp_df)

    return df
