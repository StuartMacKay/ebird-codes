from ebird.codes.locations import is_location_code


def test_is_location_code():
    assert is_location_code("L123456") is True


def test_invalid_code_is_not_location():
    assert is_location_code("A123456") is False


def test_country_code_is_not_location():
    assert is_location_code("US") is False


def test_subnational1_code_is_not_location():
    assert is_location_code("US-NV") is False


def test_subnational12_code_is_not_location_code():
    assert is_location_code("US-NV-11") is False
