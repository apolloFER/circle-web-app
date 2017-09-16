import pytest

from .circle import Circle, Point, check_dot_in_circle


def test_is_within():
    point = Point(2.3, 5.5)
    circle = Circle(3.0, 4.8, 3.0)

    assert check_dot_in_circle(point, circle)


