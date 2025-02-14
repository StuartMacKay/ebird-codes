import re

COUNTRY_CODE = re.compile(r"^[A-Z]{2}$")

SUBNATIONAL1_CODE = re.compile(r"^[A-Z]{2}-[A-Z0-9]{2,3}$")

SUBNATIONAL2_CODE = re.compile(r"^[A-Z]{2}-[A-Z0-9]{2,3}-[A-Z0-9]{2,3}$")

LOCATION_CODE = re.compile(r"^L\d+$")

LOCATION_TYPES = ["country", "subnational1", "subnational2"]


def is_national_code(code: str) -> bool:
    """Is the code for a country, e.g. 'US'."""
    return COUNTRY_CODE.match(code) is not None


def is_subnational1_code(code: str) -> bool:
    """Is the code for a subnational1 region or state, e.g. 'US-NY'."""
    return SUBNATIONAL1_CODE.match(code) is not None


def is_subnational2_code(code: str) -> bool:
    """Is the code for a subnational2 region or county, e.g. 'US-NY-109'."""
    return SUBNATIONAL2_CODE.match(code) is not None


def is_location_code(code: str) -> bool:
    """Is the code for a hotspot or private location, e.g. 'L347355622'."""
    return LOCATION_CODE.match(code) is not None


def is_country_code(code: str) -> bool:
    """An alias for is_national_code, since country is easier to remember."""
    return is_national_code(code)


def is_state_code(code: str) -> bool:
    """An alias for is_subnational1_code, since working with states is easier
    for some countries."""
    return is_subnational1_code(code)


def is_region_code(code: str) -> bool:
    """An alias for is_subnational1_code, since working with regions is easier
    for some countries."""
    return is_subnational1_code(code)


def is_county_code(code: str) -> bool:
    """An alias for is_subnational2_code, since working with counties is easier
    for some countries."""
    return is_subnational2_code(code)
