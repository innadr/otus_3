from otus_3.src.Figure import Figure


class Triangle(Figure):
    """Triangle class documentation"""

    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Can't create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle with sides {side_a}, {side_b}, {side_c}"

    def get_area(self):
        half = self.get_perimeter() / 2
        area = (half * (half - self.side_a) * (half - self.side_b) * (half - self.side_c)) ** 0.5
        return round(area, 2)

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c
