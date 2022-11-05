import ceps

def test_compare():
    assert ceps.compare("03939100", "03939100") == ["region", "subregion", "sector", "subsector", "divison"], "Should match everything for equal CEPs"

    assert ceps.compare("03939100", "03938100") == ["region", "subregion", "sector", "subsector"], "Should match everything except for divison"

    assert ceps.compare("03939100", "03929100") == ["region", "subregion", "sector"], "Should match sector, subregion and region"

    assert ceps.compare("03939100", "03531100") == ["region", "subregion"], "Should match subregion and region"

    assert ceps.compare("03939100", "08939100") == ["region"], "Should match region"

    assert ceps.compare("83939100", "03939100") == [], "Should match nothing"

    assert ceps.compare("", "") == [], "Should match nothing for empty strings"