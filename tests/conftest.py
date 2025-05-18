import pytest
from bobleesj.utils.sources.oliynyk import Oliynyk
from cifkit import Cif


@pytest.fixture
def oliynyk_obj():
    return Oliynyk()


@pytest.fixture
def oliynyk_db(oliynyk_obj):
    return oliynyk_obj.db


@pytest.fixture
def cif_ICSD_file():
    return Cif("tests/data/cifs/ICSD_43054.cif")


@pytest.fixture
def cif_PCD_file():
    return Cif("tests/data/cifs/PCD_250117.cif")


@pytest.fixture
def custom_sort_labels():
    return {
        2: {
            "A": ["Li", "Er"],
            "B": ["B", "In"],
        },
        3: {
            "R": ["Er"],
            "M": ["Co"],
            "X": ["In"],
        },
        4: {
            "A": ["Er"],
            "B": ["Co"],
            "C": ["In"],
            "D": ["U"],
        },
    }


@pytest.fixture
def custom_sort_element_order_map():
    return {
        2: {"Li": 0, "Er": 0, "B": 1, "In": 1},
        3: {"Er": 0, "Co": 1, "In": 2},
        4: {"Er": 0, "Co": 1, "In": 2, "U": 3},
    }
