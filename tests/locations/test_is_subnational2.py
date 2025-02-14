from ebird.codes.locations import is_county_code, is_subnational2_code


def test_is_subnational2_code():
    assert is_subnational2_code("US-NV-11") is True


def test_invalid_code_is_not_subnational2():
    assert is_subnational2_code("US-NV-") is False


def test_country_is_not_subnational2():
    assert is_subnational2_code("US") is False


def test_subnational1_is_not_subnational2():
    assert is_subnational2_code("US-NV") is False


def test_location_is_not_subnational2():
    assert is_subnational2_code("L123456") is False


def test_is_county_code_alias():
    assert is_county_code("US-NV-11") is True
