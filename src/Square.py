from otus_3.src.Rectangle import Rectangle


class Square(Rectangle):
    """Square class documentation"""
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Can't create Square")
        super().__init__(side, side)
        self.side_a = side
        self.side_b = side
        self.name = f"Square {side}"
