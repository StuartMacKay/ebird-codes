from ebird.codes.locations import (
    is_region_code,
    is_state_code,
    is_subnational1_code,
)


def test_is_subnational1_code():
    assert is_subnational1_code("US-NV") is True


def test_invalid_code_is_not_subnational1():
    assert is_subnational1_code("U") is False
    assert is_subnational1_code("US-") is False


def test_country_is_not_subnational1():
    assert is_subnational1_code("US") is False


def test_subnational2_is_not_subnational1():
    assert is_subnational1_code("US-NV-VMT") is False


def test_location_is_not_subnational1():
    assert is_subnational1_code("L123456") is False


def test_is_state_code_alias():
    assert is_state_code("US-NV") is True


def test_is_region_code_alias():
    assert is_region_code("US-NV") is True
