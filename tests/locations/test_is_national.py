from ebird.codes.locations import is_country_code, is_national_code


def test_national_code__returns_true():
    assert is_national_code("US") is True


def test_invalid_code__returns_false():
    assert is_national_code("USA") is False


def test_subnational1_code__returns_false():
    assert is_national_code("US-NV") is False


def test_subnational2_code__returns_false():
    assert is_national_code("US-NV-VMT") is False


def test_location_code__returns_false():
    assert is_national_code("L123456") is False


def test_alias__country_code__returns_true():
    assert is_country_code("US") is True


def test_alias__country_code__returns_false():
    assert is_country_code("USA") is False
