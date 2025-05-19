from deepdiff import DeepDiff

from CAF.features.universal_extended import (
    _transform_features_for_single_prop,
    generate_features,
)


def test_generate_features(oliynyk_db):
    db = oliynyk_db
    formula = "NdSi2Th2"
    data = generate_features(formula, db)
    assert data["formula"] == formula
    assert len(data) == 1849


def test_generate_universal_features_for_single_prop():
    prop_values = (5.0, 10.0, 15.0)
    indices_normalized = (0.2, 0.4, 0.6)
    actual_features = _transform_features_for_single_prop(
        "test", prop_values, indices_normalized
    )
    expected_features = {
        "test_avg": 10.0,
        "test_avg_weighted_norm": 11.666666666666664,
        "test_max": 15.0,
        "test_max_by_min": 3.0,
        "test_min": 5.0,
        "test_std_dev": 4.08248290463863,
        "test_variance": 16.666666666666668,
    }

    diff = DeepDiff(expected_features, actual_features, significant_digits=3)
    assert diff == {}
