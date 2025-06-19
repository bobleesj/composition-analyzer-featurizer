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
def cif_PCD_file():
    return Cif("tests/data/cifs/PCD_250117.cif")
