from otus_3.src.Figure import Figure


class Rectangle(Figure):
    """Rectangle class documentation"""

    def __init__(self, side_a, side_b):
        super().__init__()
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Can't create Rectangle")
        self.side_a = side_a
        self.side_b = side_b
        self.name = f"Rectangle {side_a} and {side_b}"
        # self.area = side_a * side_b
        # self.perimetr = 2 * (side_a + side_b)

    def get_area(self):
        return round(self.side_a * self.side_b, 2)

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
