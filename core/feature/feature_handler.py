import json

import numpy as np
import pandas as pd

from core.feature import feature_util, operation


class NumpyEncoder(json.JSONEncoder):
    """Custom encoder for numpy data types"""

    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)


def clean_dataframe_columns(df):
    # Replace 'inf', '-inf' with 'NaN' (numpy.nan)
    df.replace([np.inf, -np.inf], np.nan, inplace=True)

    # Drop columns with any NaN values (this includes those previously set from infinities)
    df.dropna(axis=1, how="any", inplace=True)

    # Remove completely empty columns, if any (e.g., all values are empty strings or similar)
    # Assuming empty means empty strings or similar placeholders not considered 'NaN' by pandas
    for col in df.columns:
        if df[col].apply(lambda x: x == "" or x is None).all():
            df.drop(col, inplace=True, axis=1)

    # Determine columns to keep: all numeric columns plus 'Formula' if it exists
    numeric_cols = df.select_dtypes(include=["float64", "int64"]).columns.tolist()
    columns_to_keep = (
        ["Formula"] + numeric_cols if "Formula" in df.columns else numeric_cols
    )

    # Ensure only the required columns are retained
    df = df[columns_to_keep]

    # Ensure 'Formula' column is first, if it exists
    if "Formula" in df.columns:
        # Reorder columns to make 'Formula' the first column
        columns_order = ["Formula"] + [col for col in df.columns if col != "Formula"]
        df = df[columns_order]

    return df


def fill_long_features_df(formulas, property_df, property_data, feature_type):
    all_features = {}
    data = []
    for formula in formulas:
        feature_dict = {formula: {}}
        for column_name in property_df.columns:
            value_dict = operation.get_feature_entry_values(
                formula, property_data, column_name, feature_type
            )
            feature_dict[formula][column_name] = value_dict

        all_features.update(feature_dict)

        for formula, properties in feature_dict.items():
            row = {"Formula": formula}
            for _, metrics in properties.items():
                row.update(metrics)
            data.append(row)

    return pd.DataFrame(data), all_features


def save_long_features(formulas, feature_type, file_name):
    property_df, property_data = feature_util.get_property_df_data()
    df, all_features = fill_long_features_df(
        formulas, property_df, property_data, feature_type
    )

    # Print the DataFrame to see its structure
    df.index = df.index + 1
    print(df.head())

    filtered_df = clean_dataframe_columns(df)
    filtered_df = filtered_df.round(3)
    file_name_excel = file_name + ".xlsx"
    file_name_json = file_name + "_raw.json"
    # Save to Excel
    filtered_df.to_excel(file_name_excel, index=False)
    print(f"Filtered data saved to {file_name_excel}")

    # Save to JSON
    with open(file_name_json, "w") as file:
        json.dump(all_features, file, cls=NumpyEncoder, indent=4)
    print(f"Data saved to {file_name_json}")


def save_dataframes(
    binary_df,
    ternary_df,
    universal_sorted_df,
    universal_unsorted_df,
    directory,
    base_name_no_ext,
    file_format,
):
    (
        binary_output_path,
        ternary_output_path,
        universal_sorted_output_path,
        universal_unsorted_output_path,
    ) = feature_util.get_output_paths(directory, base_name_no_ext, file_format)

    # Save binary DataFrame to Excel

    if file_format == "xlsx":
        if len(binary_df) > 1:
            binary_df.to_excel(binary_output_path, index=False)
            print(f"{binary_output_path} saved")

        # Save ternary DataFrame to Excel
        if len(ternary_df) > 1:
            ternary_df.to_excel(ternary_output_path, index=False)
            print(f"{ternary_output_path} saved")

        # Save universal sorted and unsorted DataFrames
        if len(universal_sorted_df) > 1:
            universal_sorted_df.to_excel(universal_sorted_output_path, index=False)
            print(f"{universal_sorted_output_path} saved")

        if len(universal_unsorted_df) > 1:
            universal_unsorted_df.to_excel(universal_unsorted_output_path, index=False)
            print(f"{universal_unsorted_output_path} saved")
    elif file_format == "csv":
        if len(binary_df) > 1:
            binary_df.to_csv(binary_output_path, index=False)
            print(f"{binary_output_path} saved")

        # Save ternary DataFrame to Excel
        if len(ternary_df) > 1:
            ternary_df.to_csv(ternary_output_path, index=False)
            print(f"{ternary_output_path} saved")

        # Save universal sorted and unsorted DataFrames
        if len(universal_sorted_df) > 1:
            universal_sorted_df.to_csv(universal_sorted_output_path, index=False)
            print(f"{universal_sorted_output_path} saved")

        if len(universal_unsorted_df) > 1:
            universal_unsorted_df.to_csv(universal_unsorted_output_path, index=False)
            print(f"{universal_unsorted_output_path} saved")
