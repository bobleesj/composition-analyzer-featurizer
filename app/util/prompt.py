import textwrap
import click


def choose_sort_method():
    click.echo("\nWelcome to the chemical formula sorting tool!")
    click.echo("This tool allows you to sort chemical formulas from an Excel file.")

    sorting_methods = [
        "Label - Sort by pre-configured label for each element.",
        "Index - Sort by index.",
        "Property - Sort by elemental chemical property value.",
        "Parse formulas into elements and indices without sorting.",
    ]

    click.echo("\nSorting methods available:")
    for index, method in enumerate(sorting_methods, start=1):
        click.echo(f"  {index}. {method}")
        
    sort_method = click.prompt(
        "Choose one of the sorting methods above by entering the corresponding number",
        type=int,
    )
    return sort_method


def print_match_option():
    introductory_paragraph = textwrap.dedent(
        """\
        ===
        You will be required to provide an Excel file that contains CIF IDs.

        Upon completion, two outputs will be generated:
        1. Filtered Excel file with rows matching CIF content in the folder
        2. Filered .cif folder with rows matching
        3. CSV on unavailable CIF content that are not found in the sheet

        Let's get started!
        ===
        """
    )

    print(introductory_paragraph)

def ascend_order():
    is_ascending_order = click.confirm(
        "\nWould you like to sort the indices in ascending order? (Default is Y)",
        default=True,
    )
    return is_ascending_order


def normalize_formula():
    is_indices_as_fractions = click.confirm(
        "\nWould you like to convert indices into fractions? (Default is N)",
        default=False,
    )
    return is_indices_as_fractions


def get_is_formula_parsed_columns_added():
    is_formula_parsed_columns_added = click.confirm(
        "\nWould you like to also include columns with parsed elements and indices? (Default is N)",
        default=False,
    )
    return is_formula_parsed_columns_added

def print_json_pretty(data, name):
    """
    Prints the contents of a dictionary in a pretty format.
    """
    print(f"\nData from {name}:")
    for key, value in data.items():
        if isinstance(value, (list, str)):
            print(f"- {key}: {value[0]}")
        else:
            print(f"- {key}: {value}")
    print()

