import os
import click
import pandas as pd
from filter_util.parser import parse_formula1
from filter_util.processor import process_cif_folder, get_excel_df


def sort_formulas_in_excel_or_folder(script_dir, available_files):
    available_folders = [
        folder
        for folder in available_files
        if os.path.isdir(os.path.join(script_dir, folder))
        and any(
            file.endswith(".cif")
            for file in os.listdir(os.path.join(script_dir, folder))
        )
    ]

    excel_sheets = [f for f in available_files if f.endswith(".xlsx")]
    cif_folders = [
        f
        for f in available_folders
        if os.path.isdir(os.path.join(script_dir, f))
    ]

    if not excel_sheets and not cif_folders:
        click.secho(
            "No Excel sheets or CIF folders available in the script's directory.",
            fg="cyan",
        )
        return

    choice = click.prompt(
        "Do you want to filter an Excel sheet/CIFs [1] or do you have a filtered sheet ready [2]? Enter the number corresponding to your choice",
        type=int,
    )

    if choice == 1:
        click.secho("Available folders containing .cif files:", fg="cyan")
        for idx, folder in enumerate(cif_folders, start=1):
            click.echo(f"{idx}. {folder}")
        excel_sheets.sort()  # Sort the list alphabetically
        click.secho("Available .xlsx files:", fg="cyan")
        for idx, sheet in enumerate(excel_sheets, start=len(cif_folders) + 1):
            click.echo(f"{idx}. {sheet}")

        choice = click.prompt(
            "Enter the number corresponding to your choice", type=int
        )

        if 1 <= choice <= len(cif_folders):
            folder_path = os.path.join(script_dir, cif_folders[choice - 1])
            df = process_cif_folder(folder_path)
            df.index = df.index + 1
            click.secho("Data processed from CIF folder:", fg="cyan")
            click.echo(df)

            # Save raw data to Excel sheet if it is a CIF folder
            script_dir = os.path.dirname(os.path.abspath(__file__))
            parent_dir = os.path.dirname(script_dir)
            file_name = os.path.basename(folder_path)
            output_folder = parent_dir
            os.makedirs(output_folder, exist_ok=True)

            # raw_output_file_name = f"{file_name}_raw_data.xlsx"
            # raw_output_file_path = os.path.join(
            #     output_folder, raw_output_file_name
            # )
            # data.to_excel(raw_output_file_path, index=False)
            # click.secho(
            #     f"Raw data saved to: {raw_output_file_path}", fg="cyan"
            # )

            # Parse formulas and append elements and counts to DataFrame
            click.secho(
                "Currently processing elements of your sheet",
                fg="cyan",
            )

            data_copy = df.copy()

            # Apply the function to each row in the DataFrame
            data_copy[["Elements", "Counts"]] = (
                data_copy["Formula"].apply(parse_formula1).apply(pd.Series)
            )

            # Split the lists into separate columns
            for i in range(max(map(len, data_copy["Elements"]))):
                data_copy[f"Element {i+1}"] = data_copy["Elements"].str[i]
                data_copy[f"# Element {i+1}"] = data_copy["Counts"].apply(
                    lambda x: x[i] if len(x) > i else None
                )

            # Drop temporary columns
            data_copy.drop(["Elements", "Counts"], axis=1, inplace=True)

            click.secho(
                "Elements and counts appended to DataFrame:",
                fg="cyan",
            )
            data_copy.index = data_copy.index + 1
            click.echo(data_copy)

            # Save DataFrame to Output folder
            output_file_name = f"{file_name}_elements_sorted.xlsx"
            output_file_path = os.path.join(output_folder, output_file_name)
            data_copy.to_excel(output_file_path, index=False)
            click.secho(
                f"Appended DataFrame saved to: {output_file_path}",
                fg="cyan",
            )

        elif len(cif_folders) < choice <= len(cif_folders) + len(excel_sheets):
            sheet_idx = choice - len(cif_folders) - 1
            file_name = excel_sheets[sheet_idx]
            file_path = os.path.join(script_dir, file_name)
            df = get_excel_df(file_path)
            click.secho("Data processed from Excel sheet:", fg="cyan")
            click.echo(df)

            # Parse formulas and append elements and counts to DataFrame
            click.secho(
                "Currently processing elements of your sheet",
                fg="cyan",
            )

            data_copy = df.copy()

            # Apply the function to each row in the DataFrame
            data_copy[["Elements", "Counts"]] = (
                data_copy["Formula"].apply(parse_formula1).apply(pd.Series)
            )

            # Split the lists into separate columns
            for i in range(max(map(len, data_copy["Elements"]))):
                data_copy[f"Element {i+1}"] = data_copy["Elements"].str[i]
                data_copy[f"# Element {i+1}"] = data_copy["Counts"].apply(
                    lambda x: x[i] if len(x) > i else None
                )

            # Drop temporary columns
            data_copy.drop(["Elements", "Counts"], axis=1, inplace=True)
            data_copy.index = data_copy.index + 1
            click.secho(
                "Elements and counts appended to DataFrame:",
                fg="cyan",
            )
            click.echo(data_copy)

            # Save DataFrame to the same directory as the input Excel sheet
            output_folder = os.path.dirname(file_path)
            os.makedirs(output_folder, exist_ok=True)

            output_file_name = (
                f"{os.path.splitext(file_name)[0]}_elements_sorted.xlsx"
            )
            output_file_path = os.path.join(output_folder, output_file_name)
            data_copy.to_excel(output_file_path, index=False)
            click.secho(
                f"Appended DataFrame saved to: {output_file_path}",
                fg="cyan",
            )

        else:
            click.secho("Invalid choice.", fg="red")

    elif choice == 2:
        # Here you can implement the logic for handling a filtered sheet
        pass
    else:
        click.secho("Invalid choice.", fg="red")


def dataframe_to_dict(results, elements):
    """
    Convert DataFrame to dictionary with Element as keys and # Element as values.

    Args:
    results (DataFrame): DataFrame with 'Element' and '# Element' columns.
    elements (list): List of all elements to include in the dictionary.

    Returns:
    dict: Dictionary with Element as keys and # Element as values.
    """
    # Initialize an empty dictionary with all elements and counts set to 0
    d = {element: 0 for element in elements}

    # Iterate through DataFrame rows and update the counts
    for index, row in results.iterrows():
        d[row["Element"]] = row["# Element"]

    return d


def dataframe_to_dict(results, elements):
    """
    Convert DataFrame to dictionary with Element as keys and # Element as values.

    Args:
    results (DataFrame): DataFrame with 'Element' and '# Element' columns.
    elements (list): List of all elements to include in the dictionary.

    Returns:
    dict: Dictionary with Element as keys and # Element as values.
    """
    # Initialize an empty dictionary with all elements and counts set to 0
    d = {element: 0 for element in elements}

    # Iterate through DataFrame rows and update the counts
    for index, row in results.iterrows():
        d[row["Element"]] = row["# Element"]

    return d
