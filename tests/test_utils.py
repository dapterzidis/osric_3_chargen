import pytest
import utils

@pytest.mark.parametrize("value, expected", [
    ("5", True), ("-2", True), ("abc", False), ("", False), ("3.5", False),
])
def test_is_integer(value, expected):
    assert utils.is_integer(value) == expected