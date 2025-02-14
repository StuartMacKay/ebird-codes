from ebird.codes.locations import is_county_code, is_subnational2_code


def test__returns_true():
    assert is_subnational2_code("US-NV-11") is True


def test_invalid_code__returns_false():
    assert is_subnational2_code("US-NV-") is False


def test_country_code__returns_false():
    assert is_subnational2_code("US") is False


def test_subnational1_code__returns_false():
    assert is_subnational2_code("US-NV") is False


def test_location_code__returns_false():
    assert is_subnational2_code("L123456") is False


def test_alias___valid_code__returns_true():
    assert is_county_code("US-NV-11") is True


def test_alias__invalid_code__returns_false():
    assert is_county_code("US-NV") is False
