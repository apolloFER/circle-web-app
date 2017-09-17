import math

# Type Annotations are awsome but 3.4 and 2.7 won't recognize them so hence this syntax


class Point(object):
    def __init__(self, x=0.0, y=0.0):  # type: (float, float) -> None
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, x=0.0, y=0.0, radius=0.0):  # type: (float, float, float) -> None
        self.position = Point(x, y)
        if radius <= 0.0:
            raise ValueError("Negative radius not allowed")
        self.radius = radius

    def is_point_within(self, point):  # type: (Point) -> bool
        # could have used something fancier like numpy, but this is just to simple for that kind of lib
        distance = math.sqrt(math.pow(point.y - self.position.y, 2) + math.pow(point.x - self.position.x, 2))
        return distance < self.radius


def check_point_in_circle(point, circle):  # type: (Point, Circle) -> bool
    return circle.is_point_within(point)



