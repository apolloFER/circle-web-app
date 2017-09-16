import math


class Point(object):
    def __init__(self, x=0.0, y=0.0): # type: (float, float) -> None
        self.x = x
        self.y = y


class Circle(object):
    def __init__(self, x=0.0, y=0.0, radius=0.0): # type: (float, float, float) -> None
        self.position = Point(x, y)
        self.radius = radius

    def is_point_within(self, point): # type: (Point) -> bool
        distance = math.sqrt(math.pow(point.y - self.position.y, 2) + math.pow(point.x - self.position.x, 2))
        return distance < self.radius


def check_point_in_circle(point, circle): # type: (Point, Circle) -> bool
    return circle.is_point_within(point)



