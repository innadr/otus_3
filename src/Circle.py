import math
from otus_3.src.Figure import Figure


class Circle(Figure):
    """Circle class documentation"""
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.name = f"Circle {radius}"
        if radius <= 0:
            raise ValueError("Can't create Circle")

    def get_area(self):
        area = round(math.pi * self.radius * self.radius, 2)
        return area

    def get_perimeter(self):
        perimeter = round(math.pi * self.radius * 2, 2)
        return perimeter
