from ebird.codes.locations import (
    is_region_code,
    is_state_code,
    is_subnational1_code,
)


def test_subnational1_code__returns_true():
    assert is_subnational1_code("US-NV") is True


def test_invalid_code__returns_false():
    assert is_subnational1_code("US-") is False


def test_country_code__returns_false():
    assert is_subnational1_code("US") is False


def test_subnational2_code__returns_false():
    assert is_subnational1_code("US-NV-VMT") is False


def test_location_code__returns_false():
    assert is_subnational1_code("L123456") is False


def test_state_alias__subnational1_code__returns_true():
    assert is_state_code("US-NV") is True


def test_state_alias__subnational2_code__returns_false():
    assert is_state_code("US-NV-VMT") is False


def test_region_alias__subnational1_code__returns_true():
    assert is_region_code("US-NV") is True


def test_region_alias__subnational2_code__returns_false():
    assert is_region_code("US-NV-VMT") is False
