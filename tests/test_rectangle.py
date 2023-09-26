import pytest
from data import TEST_DATA

from otus_3.src.Rectangle import Rectangle


@pytest.mark.parametrize("a, b, perimeter, area", TEST_DATA["rectangle"])
def test_rectangle(a, b, perimeter, area):
    if a <= 0 or b <= 0:
        with pytest.raises(ValueError, match="Can't create Rectangle"):
            Rectangle(a, b)
    else:
        r = Rectangle(a, b)
        assert r.name == f"Rectangle {a} and {b}"
        assert r.get_perimeter() == perimeter
        assert r.get_area() == area
