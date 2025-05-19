from deepdiff import DeepDiff

from CAF.features.ternary_extended import (
    _transform_features_for_single_prop,
    generate_features,
)


def test_generate_features(oliynyk_db):
    db = oliynyk_db
    formula = "NdSi2Th2"
    data = generate_features(formula, db)
    assert data["formula"] == formula
    assert data["atomic_weight_R_square"] == 20805.754564
    assert len(data) == 9241


def test_transform_features_for_single_prop():
    RMX_prop_values = (5.0, 10.0, 15.0)
    RMX_indices = (1, 2, 3)
    actual_features = _transform_features_for_single_prop(
        "test", RMX_prop_values, RMX_indices
    )

    expected_features = {
        "test_R": 5.0,
        "test_M": 10.0,
        "test_X": 15.0,
        "test_R+M": 15.0,
        "test_M+X": 25.0,
        "test_R+X": 20.0,
        "test_R+M_weighted": 25.0,
        "test_M+X_weighted": 65.0,
        "test_R+X_weighted": 50.0,
        "test_R-M": -5.0,
        "test_M-X": -5.0,
        "test_R-X": -10.0,
        "test_R-M_weighted": -15.0,
        "test_M-X_weighted": -25.0,
        "test_R-X_weighted": -40.0,
        "test_R/M": 0.5,
        "test_M/X": 0.6666666666666666,
        "test_R/X": 0.3333333333333333,
        "test_R/M_weighted": 0.25,
        "test_M/X_weighted": 0.4444444444444444,
        "test_R/X_weighted": 0.1111111111111111,
        "test_RMX_avg": 10.0,
        "test_RM_avg": 7.5,
        "test_MX_avg": 12.5,
        "test_RX_avg": 10.0,
        "test_max": 15.0,
        "test_min": 5.0,
        "test_max/min": 3.0,
        "test_max-min": 10.0,
        "test_max/mid": 1.5,
        "test_max-mid": 5.0,
        "test_mid/min": 2.0,
        "test_mid-min": 5.0,
        "test_std_dev": 4.08248290463863,
        "test_variance": 16.666666666666668,
    }

    diff = DeepDiff(expected_features, actual_features, significant_digits=3)
    assert diff == {}
