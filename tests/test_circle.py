import pytest
from data import TEST_DATA

from otus_3.src.Circle import Circle


@pytest.mark.parametrize("a, perimeter, area", TEST_DATA["circle"])
def test_circle(a, perimeter, area):
    if a <= 0:
        with pytest.raises(ValueError, match="Can't create Circle"):
            Circle(a)
    else:
        c = Circle(a)
        assert c.name == f"Circle {a}"
        assert c.get_perimeter() == perimeter
        assert c.get_area() == area
