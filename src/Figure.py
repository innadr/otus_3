from abc import ABC, abstractmethod


class Figure(ABC):
    """Figure class documentation"""
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise AssertionError("Can't add area")
        return round(self.get_area() + other_figure.get_area(), 2)
