from deepdiff import DeepDiff

from CAF.features.binary_extended import (
    _transform_features_for_single_prop,
    generate_features,
)


def test_generate_features(oliynyk_db):
    db = oliynyk_db
    formula = "NdSi2"
    data = generate_features(formula, db)
    assert data["formula"] == formula
    assert data["atomic_weight_A_square"] == 20805.754564
    assert len(data) == 3961


def test_transform_features_for_single_prop():
    AB_prop_values = (5.0, 10.0)
    AB_indices = (1, 2)
    actual_features = _transform_features_for_single_prop(
        "test", AB_prop_values, AB_indices
    )

    expected_features = {
        "test_A": 5.0,
        "test_B": 10.0,
        "test_A+B": 15.0,
        "test_A+B_weighted": 25.0,
        "test_A-B": -5.0,
        "test_A-B_weighted": -15.0,
        "test_A*B": 50.0,
        "test_A*B_weighted": 100.0,
        "test_A/B": 0.5,
        "test_A/B_weighted": 0.25,
        "test_avg": 7.5,
        "test_max": 10.0,
        "test_min": 5.0,
        "test_std_dev": 2.5,
        "test_variance": 6.25,
    }

    diff = DeepDiff(expected_features, actual_features, significant_digits=3)
    assert diff == {}
