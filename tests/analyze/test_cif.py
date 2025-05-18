def test_find_cif_source(cif_ICSD_file, cif_PCD_file):
    assert cif_ICSD_file.db_source == "ICSD"
    assert cif_PCD_file.db_source == "PCD"
