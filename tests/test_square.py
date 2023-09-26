import pytest
from data import TEST_DATA

from otus_3.src.Square import Square


@pytest.mark.parametrize("a, perimeter, area", TEST_DATA["square"])
def test_square(a, perimeter, area):
    if a <= 0:
        with pytest.raises(ValueError, match="Can't create Square"):
            Square(a)
    else:
        s = Square(a)
        assert s.name == f"Square {a}"
        assert s.get_perimeter() == perimeter
        assert s.get_area() == area
