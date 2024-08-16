import os
import pandas as pd
import click


def get_excel_df(file_path):
    """
    Process data from an Excel sheet
    """
    # Read the Excel file into a DataFrame
    data = pd.read_excel(file_path)
    return data


def process_cif_folder(folder_path):
    entries = []
    formulas = []

    # Loop through the directory and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".cif"):
                # Extract the filename without extension
                entry = os.path.splitext(filename)[0]
                file_path = os.path.join(root, filename)

                # Read the file and extract the desired information
                with open(file_path, "r") as file:
                    # Keep track of which line we're processing
                    line_count = 0
                    for line in file:
                        line_count += 1
                        if line_count == 3:  # Check if it's the third line
                            # Split the line by '#'
                            parts = line.split("#")
                            if len(parts) > 2:
                                # Extract the second part, and remove leading/trailing whitespace
                                formula = parts[2].strip()
                                # Break the formula at the first space
                                formula = formula.split(" ")[0]
                                # Append the extracted data to the lists
                                entries.append(entry)
                                formulas.append(formula)
                            else:
                                click.secho(
                                    f"Warning: Line '{line}' in file '{filename}' does not contain enough '#' characters.",
                                    fg="yellow",
                                )
                            break  # Break the loop after finding the formula

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
