import os

import click
import pandas as pd


def get_formula_from_cif(file_path):
    """
    Simply parse the formula from a CIF file
    Remove "'", empty space
    Order alphabetically

    """

    target_line_start = "_chemical_formula_sum"

    with open(file_path, "r") as file:
        for line in file:
            if line.strip().startswith(target_line_start):
                # Extract the formula part, assuming it's after the key
                formula = (
                    line.split(target_line_start)[-1].strip().replace("'", "")
                )
                formula = formula.replace(" ", "")

                return formula
    return "Formula not found"


def get_excel_df(file_path):
    """
    Process data from an Excel sheet
    """
    # Read the Excel file into a DataFrame
    data = pd.read_excel(file_path)
    return data


def parse_entry_formula(folder_path):
    entries = []
    formulas = []

    # Loop through the directory and its subdirectories
    for root, _, files in os.walk(folder_path):
        for file in files:
            # Check if the file is a CIF file
            if file.endswith(".cif"):
                # Get the full path of the CIF file
                file_path = os.path.join(root, file)
                # Get the formula from the CIF file
                formula = get_formula_from_cif(file_path)
                # Append the entry and formula to the lists
                entries.append(file)
                formulas.append(formula)

    data = pd.DataFrame({"Entry": entries, "Formula": formulas})
    return data


def compile_element_counts(filtered, Output_folder, chosen_file):
    """Compile the total number of elements in the DataFrame."""
    element_counts = {}
    for i in range(1, (len(filtered.columns) // 2) + 1):
        element_col = f"Element {i}"
        count_col = f"# Element {i}"
        if (
            element_col not in filtered.columns
            or count_col not in filtered.columns
        ):
            continue
        for index, row in filtered.iterrows():
            element = row[element_col]
            count = row[count_col]
            if pd.notnull(element) and pd.notnull(count):
                element_counts[element] = (
                    element_counts.get(element, 0) + count
                )

    df = pd.DataFrame(
        list(element_counts.items()), columns=["Element", "# Element"]
    )
    file_path = os.path.join(
        Output_folder,
        f"{os.path.splitext(os.path.basename(chosen_file))[0]}_element_count.xlsx",
    )
    df.to_excel(file_path, index=False)
    click.secho(f"Element counts saved to: {file_path}", fg="cyan")
    click.secho("Element counting is completed", fg="cyan")

    # Print the results to the terminal
    df.index = df.index + 1
    click.echo(df)

    return df
