import pytest
from data import TEST_DATA

from otus_3.src.Triangle import Triangle


@pytest.mark.parametrize("a, b, c, perimeter, area", TEST_DATA["triangle"])
def test_triangle(a, b, c, perimeter, area):
    if a <= 0 or b <= 0 or c <= 0:
        with pytest.raises(ValueError, match="Can't create Triangle"):
            Triangle(a, b, c)
    else:
        t = Triangle(a, b, c)
        assert t.name == f"Triangle with sides {a}, {b}, {c}"
        assert t.get_perimeter() == perimeter
        assert t.get_area() == area
