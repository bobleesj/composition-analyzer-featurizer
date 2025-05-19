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
def custom_label_excel_path():
    return "tests/data/sort/test-custom-labels.xlsx"


@pytest.fixture
def custom_labels_from_excel():
    return {
        2: {"A": ["Fe", "Co", "Ni"], "B": ["Si", "Ga", "Ge"]},
        3: {
            "R": ["Sc", "Y", "La"],
            "M": ["Fe", "Co", "Ni"],
            "X": ["Si", "Ga", "Ge"],
        },
        4: {
            "A": ["Sc", "Y", "La"],
            "B": ["Fe", "Co", "Ni"],
            "C": ["Si", "Ga", "Ge"],
            "D": ["Gd", "Tb", "Dy"],
        },
    }


#
