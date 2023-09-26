from otus_3.src.Rectangle import Rectangle
from otus_3.src.Square import Square
from otus_3.src.Triangle import Triangle
from otus_3.src.Circle import Circle
import pytest
from data import TEST_DATA


@pytest.mark.parametrize("a, b, c, sum_area",
                         TEST_DATA["add_area_rectangle_circle"])
def test_add_area_rectangle_circle(a, b, c, sum_area):
    if a <= 0 or b <= 0:
        with pytest.raises(ValueError, match="Can't create Rectangle"):
            r = Rectangle(a, b)
    elif c <= 0:
        with pytest.raises(ValueError, match="Can't create Circle"):
            circle = Circle(c)
    else:
        r = Rectangle(a, b)
        circle = Circle(c)
        assert r.add_area(circle) == sum_area


@pytest.mark.parametrize("a, b, c, d, sum_area",
                         TEST_DATA["add_area_triangle_square"])
def test_add_area_triangle_square(a, b, c, d, sum_area):
    if a <= 0 or b <= 0 or c <= 0:
        with pytest.raises(ValueError, match="Can't create Triangle"):
            Triangle(a, b, c)
    elif d <= 0:
        with pytest.raises(ValueError, match="Can't create Square"):
            Square(d)
    else:
        t = Triangle(a, b, c)
        s = Square(d)
        assert t.add_area(s) == sum_area
        assert s.add_area(t) == sum_area
