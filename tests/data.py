TEST_DATA = {
    "rectangle": [
        # side_a, side_b, perimeter, area
        (5, 10, 30, 50),
        (0, 2, 0, 0)
    ],

    "square": [
        # side_a, perimeter, area
        (5, 20, 25),
        (-1, 0, 0)
    ],

    "circle": [
        # radius, perimeter, area
        (5, 31.42, 78.54),
        (1.5, 9.42, 7.07),
        (-1, 0, 0)
    ],

    "triangle": [
        # side_a, side_b, side_c, perimeter, area
        (5, 7, 9, 21, 17.41),
        (1, -2, 3, 0, 0)
    ],

    "add_area_rectangle_circle": [
        # rectangle_side_a, rectangle_side_b, circle_radius, summary_area
        (2, 5, 5, 88.54),
        (1, 2, 3, 30.27),
        (0, 2, 3, 0),
        (2, 5, 0, 0)
    ],

    "add_area_triangle_square": [
        # triangle_side_a, triangle_side_b,
        # triangle_side_c, square_side, summary_area
        (5, 7, 9, 1.5, 19.66),
        (3.4, 9.3, 8.2, 4, 29.81),
        (0, 2, -3, 1, 0),
        (5, 7, 9, 0, 0)
    ]
}
