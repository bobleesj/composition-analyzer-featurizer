from os.path import isfile, join

import pandas as pd
import pytest

from CAF.features import generator


@pytest.mark.parametrize(
    "add_extended_features,expected_files",
    [
        # Test when we only have binary formulas. Expect only binary csv files.
        (False, ["binary_only_binary.csv"]),
        (True, ["binary_only_binary_ext.csv", "binary_only_binary.csv"]),
    ],
)
def test_get_composition_with_binary(
    tmpdir, add_extended_features, expected_files
):
    file_prefix = "binary_only"
    formulas = ["NdSi2", "ThOs"]
    save_path = str(tmpdir)
    generator.get_composition_features(
        formulas,
        save_dir=save_path,
        extended_features=add_extended_features,
        file_prefix=file_prefix,
    )
    for filename in expected_files:
        filepath = join(save_path, filename)
        assert isfile(filepath)
        df = pd.read_csv(filepath)
        assert len(df) == 2
    # Just to confrm no file is created for ternary/quaternary
    assert not isfile(join(save_path, "binary_only_ternary.csv"))
    assert not isfile(join(save_path, "binary_only_quaternary.csv"))


@pytest.mark.parametrize(
    "formulas, expected_files",
    [
        (
            # 2 binary, 1 ternary, 1 quaternary
            ["NdSi2", "ThOs", "NdSi2Th2", "YNdThSi2"],
            # Expect the following files to be generated
            [
                "expect_all_features_binary.csv",
                "expect_all_features_binary_ext.csv",
                "expect_all_features_ternary.csv",
                "expect_all_features_ternary_ext.csv",
                "expect_all_features_quaternary.csv",
                "expect_all_features_universal.csv",
                "expect_all_features_universal_ext.csv",
            ],
        ),
    ],
)
def test_get_composition_with_extended_features(
    tmpdir, formulas, expected_files
):
    file_prefix = "expect_all_features"
    save_path = str(tmpdir)

    generator.get_composition_features(
        formulas=formulas,
        save_dir=save_path,
        extended_features=True,
        file_prefix=file_prefix,
    )

    for filename in expected_files:
        filepath = join(save_path, filename)
        assert isfile(filepath)
        df = pd.read_csv(filepath)
        assert len(df) >= 1
