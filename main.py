class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, radius):
        self.center = Point(x, y)
        self.radius = radius

    def contains(self, p):
        return (p.x - self.center.x) ** 2 + (p.y - self.center.y) ** 2 <= self.radius ** 2


circle_1 = Circle(2, 2, 5)
obj_1 = Point(1, 1)
obj_2 = Point(25, 4)

print(circle_1.contains(obj_1))
print(circle_1.contains(obj_2))
