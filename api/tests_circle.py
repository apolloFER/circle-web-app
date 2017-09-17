from .circle import Circle, Point, check_point_in_circle

# Pytest module for testing the Circle, Point classes


# testing when point within circle
def test_is_within():
    point = Point(2.3, 5.5)
    circle = Circle(3.0, 4.8, 3.0)

    assert check_point_in_circle(point, circle)


# testing when point not within circle
def test_is_not_within():
    point = Point(2.3, 5.5)
    circle = Circle(3.0, 4.8, 0.1)

    assert not check_point_in_circle(point, circle)


# testing when radius negative
def test_negative_radius():
    try:
        Circle(2.0, 1.0, -5.0)
    except ValueError:
        pass
    else:
        raise AssertionError()


