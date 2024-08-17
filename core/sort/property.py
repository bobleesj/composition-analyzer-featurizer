import click

from core.util import data, parser


def sort_formula_by_selected_property(
    formula_tuple,
    num_elements,
    is_ascending_order,
    element_col_num,
):
    parsed_formulas_set = [
        list(item) for item in parser.get_parsed_formula(formula_tuple)
    ]
    if num_elements not in [2, 3]:
        raise ValueError("num_elements must be either 2 or 3")

    property_values = data.get_element_property_values(
        "data/element_properties_for_ML.xlsx", element_col_num
    )

    # Sort the formulas based on property values
    sorted_formulas_set = sorted(
        parsed_formulas_set,
        key=lambda x: property_values.get(x[0], float("inf")),
        # Reverse sorting if is_ascending_order is False
        reverse=not is_ascending_order,
    )
    sorted_formula_string = "".join(
        [f"{element[0]}{element[1]}" for element in sorted_formulas_set]
    )

    return sorted_formula_string


def display_available_properties():
    # Read the Excel and generate the columns
    available_properties = {
        "Atomic weight": 1,
        "Atomic number": 2,
        "Period": 3,
        "Group": 4,
        "Mendeleev number": 5,
        "Valence e total": 6,
        "Unpaired electrons": 7,
        "Gilman no. of valence electrons": 8,
        "Zeff": 9,
        "Ionization energy (eV)": 10,
        "CN": 11,
        "Ratio n closest/CN": 12,
        "Polyhedron distortion (dmin/dn)": 13,
        "CIF radius element": 14,
        "Pauling, R(CN12)": 15,
        "Pauling EN": 16,
        "Martynov Batsanov EN": 17,
        "Melting point, K": 18,
        "Density, g/mL": 19,
        "Specific heat, J/g K": 20,
        "Cohesive energy": 21,
        "Bulk modulus, GPa": 22,
        "Abundance in Earth's crust": 23,
        "Abundance in solar system (log)": 24,
        "HHI production": 25,
        "HHI reserve": 26,
        "C3ost, pure ($/100g)": 27,
    }

    # Determine the maximum length of the property names to align the output
    max_len = max(len(prop) for prop in available_properties.keys())
    for prop_name, prop_num in available_properties.items():
        click.echo(f"{prop_name.ljust(max_len)} : {prop_num}")
