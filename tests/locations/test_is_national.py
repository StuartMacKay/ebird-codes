from ebird.codes.locations import is_country_code, is_national_code


def test_is_national_code():
    assert is_national_code("US") is True


def test_invalid_code_is_not_national_code():
    assert is_national_code("") is False
    assert is_national_code("U") is False
    assert is_national_code("USA") is False


def test_subnational1_code_is_not_national_code():
    assert is_national_code("US-NV") is False
    assert is_national_code("MX-OXA") is False


def test_subnational2_code_is_not_national_code():
    assert is_national_code("US-NV-VMT") is False


def test_location_code_is_not_national_code():
    assert is_national_code("L123456") is False


def test_is_country_code_alias():
    assert is_country_code("US") is True
