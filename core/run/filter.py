import os

import click
import pandas as pd

from core.filter_util import (
    composition,
    data,
    handler,
    parser,
    prevalence,
    processor,
    prompt,
)


def run_filter_option(script_dir):
    prompt.sort_formulas_in_excel_or_folder(script_dir, os.listdir(script_dir))

    # Display .cif files and .xlsx files in the script's directory
    available_files = [
        file
        for file in os.listdir(script_dir)
        if file.endswith(".xlsx") and not file.endswith("_errors.xlsx")
    ]
    available_files.sort()

    if not available_files:
        click.secho(
            "No files found in the directory",
            fg="yellow",
        )
        return

    click.secho(
        "Which file would you like to summarize (If you picked option 1, select the file ending with _sorted.xlsx):",
        fg="cyan",
    )
    for idx, file_name in enumerate(available_files, start=1):
        click.echo(f"[{idx}] {file_name}")
    file_choice = click.prompt(
        "Enter the number corresponding to your choice", type=int
    )
    if 1 <= file_choice <= len(available_files):
        chosen_file = os.path.join(
            script_dir, available_files[file_choice - 1]
        )
        click.secho(f"Summarizing file: {chosen_file}", fg="cyan")

    # Define a list of symbols that are not elements
    elements = data.get_element_list()

    # Define a DataFrame with invalid formulas
    invalid_formulas = pd.read_excel(chosen_file)

    # Apply the function to each row in the DataFrame
    parsed_data = (
        invalid_formulas["Formula"]
        .apply(parser.parse_formula2)
        .apply(pd.Series)
    )
    invalid_formulas[["Elements", "Counts", "Error"]] = parsed_data.iloc[:, :3]

    view_errors = "y"  # Default to 'yes' without prompting

    if view_errors == "y":
        # Filter the DataFrame for rows where the Error column is not None
        errors_df = invalid_formulas[invalid_formulas["Error"].notna()]
        handler.handle_errors(errors_df, chosen_file, script_dir)

    # Classification of formulas
    invalid_formulas_copy = composition.numerical_classification(
        invalid_formulas
    )

    summary_file_path = os.path.join(
        script_dir,
        f"{os.path.splitext(os.path.basename(chosen_file))[0]}_summary.xlsx",
    )
    invalid_formulas_copy.to_excel(summary_file_path, index=False)
    click.secho(f"Summary saved to: {summary_file_path}", fg="cyan")

    click.secho("Filtering errors out of your dataframe", fg="cyan")
    filtered = invalid_formulas_copy[invalid_formulas_copy["Error"].isnull()]

    # Save the filtered DataFrame to an Excel file with '_filtered' suffix
    filtered_file_path = os.path.join(
        script_dir,
        f"{os.path.splitext(os.path.basename(chosen_file))[0]}_filtered.xlsx",
    )
    filtered.to_excel(filtered_file_path, index=False)

    # Compile element counts
    results = processor.compile_element_counts(
        filtered, script_dir, chosen_file
    )

    data_dict = prompt.dataframe_to_dict(results, elements)

    # Call the function with the list of elements and the relative path to the parent directory
    prevalence.element_prevalence(
        pd.Series(data_dict),
        sheet_path=chosen_file,
        log_scale=False,
    )

    click.secho("Periodic table created successfully", fg="cyan")

    # Call numerical_and_elemental_filtering function
    composition.numerical_and_elemental_filtering(
        filtered_file_path, invalid_formulas_copy
    )
