import pandas as pd

def read_formula_column_from_excel(file_path):
    # Check for 'Formula' or 'formula' column (case-insensitive)
    formula_col = None
    for col in df.columns:
        if col.lower() == "formula":
            formula_col = col
            break
    if not formula_col:
        raise ValueError("The Excel file does not contain a 'Formula' or 'formula' column.")
    # Keep only the formula column
    df = df[[formula_col]]

    return df