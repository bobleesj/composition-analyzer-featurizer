import os

import pandas as pd
from bobleesj.utils.parsers.formula import Formula
from bobleesj.utils.sources.oliynyk import Oliynyk

from CAF.features import (
    binary,
    binary_extended,
    quaternary,
    ternary,
    ternary_extended,
    universal,
    universal_extended,
)


def get_composition_features(
    formulas, extended_features=False, save_dir="./", file_prefix="features"
) -> tuple[list[str], list[str]]:
    """Generate composition-based features for a list of chemical formulas
    using the Oliynyk elemental property dataset.

    This function processes the provided chemical formulas, filters out
    unsupported ones, and computes core and optional extended features for
    binary, ternary, quaternary, and universal compositions. Optionally,
    the generated features can be saved as CSV files in the specified
    directory.

    Parameters
    ----------
    formulas : list of str
        The List of chemical formulas to process.
    extended_features : bool=False
        Whether to compute and save extended features in addition
        to the core features (default is False).
    save_dir : str="./"
        The path where the generated feature CSV files are saved
        (default is the working directory).
    file_prefix : str="features"
        The prefix for the saved CSV filenames (default is "features").

    Returns
    -------
    (supported_formulas, unsupported_formulas) : tuple(list[str], list[str])
        The tuple containing two lists of supported and unsupported formulas.
    """
    print(
        "Getting the Oliynyk compositional database...\n"
        "(DOI: https://doi.org/10.1016/j.dib.2024.110178)"
    )
    db = Oliynyk().db
    # Ensure the formulas are supported by the Oliynyk database
    print(
        "Filtering formulas with elements provided\n"
        " in the Oliynyk elemental property dataset..."
    )
    formulas, formulas_unsupported = Oliynyk().get_supported_formulas(formulas)
    print("Sorting formulas into binary, ternary, quaternary...")
    sorted_formula_dict = Formula.filter_by_composition(formulas)
    # Sort into binary, ternary, quaternary
    bi_formulas = sorted_formula_dict.get(2, [])
    ter_formulas = sorted_formula_dict.get(3, [])
    quat_formulas = sorted_formula_dict.get(4, [])

    # Core features
    print("Generarting features...")
    bi_features = _collect(bi_formulas, binary, db)
    ter_features = _collect(ter_formulas, ternary, db)
    quat_features = _collect(quat_formulas, quaternary, db)
    uni_features = _collect(formulas, universal, db)

    features_to_save = {
        "binary": bi_features,
        "ternary": ter_features,
        "quaternary": quat_features,
        "universal": uni_features,
    }

    # (Optional) Add extended features
    if extended_features:
        print("Generating extended features... (This may take a while)")
        features_to_save.update(
            {
                "binary_ext": _collect(bi_formulas, binary_extended, db),
                "ternary_ext": _collect(ter_formulas, ternary_extended, db),
                "universal_ext": _collect(formulas, universal_extended, db),
            }
        )

    # (Optional) Save .csv files
    print("Saving features to CSV files...")
    os.makedirs(save_dir, exist_ok=True)
    for name, features in features_to_save.items():
        if features:  # Only save when it's not empty
            df = pd.DataFrame.from_dict(features, orient="index")
            csv_path = os.path.join(save_dir, f"{file_prefix}_{name}.csv")
            df.to_csv(csv_path, index=False)

    print("Done!")
    return formulas, formulas_unsupported


def _collect(formulas, feature_module, db) -> dict[str, dict]:
    # Return an empty dictionary if no formulas
    if not formulas:
        return {}
    feature_dict = {}
    for formula in formulas:
        features = feature_module.generate_features(formula, db)
        feature_dict[formula] = features
    return feature_dict
