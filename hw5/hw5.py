#!/usr/python3
from math import sqrt, pi


class Point:
    def __init__(self, x=0, y=0):
        
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def getX(self):
        return self.x

    def setX(self, value):
        self.x = value

    def getY(self):
        return self.y

    def setY(self, value):
        self.y = value

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def norm(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def __mul__(self, other):
        ssqr = self.x * other.y - other.x * self.y
        return abs(ssqr)


class Shape:
    def __init__(self):
        
        self.name = "Abstract shape"

    def __str__(self):
        return (
            self.name
            + ": "
            + "S="
            + str(self.square())
            + " "
            + "P="
            + str(self.perimeter())
        )

    def square(self):
        pass

    def perimeter(self):
        pass


class Quadrangle(Shape):
    def __init__(self, p0=Point(), p1=Point(), p2=Point(), p3=Point()):
        
        super().__init__()
        self.name = "Quadrangle"
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def square(self):
        return 0.5 * ((self.p2 - self.p0) * (self.p3 - self.p1))

    def perimeter(self):
        return (
            (self.p0 - self.p1).norm()
            + (self.p1 - self.p2).norm()
            + (self.p2 - self.p3).norm()
            + (self.p3 - self.p0).norm()
        )


class Rectangle(Quadrangle):
    def __init__(self, p0=Point(), p1=Point(), p2=Point(), p3=Point()):
        
        super().__init__(p0, p1, p2, p3)
        self.name = "Rectangle"

    def square(self):
        return (self.p2.x - self.p0.x) * (self.p2.y - self.p0.y)


class Oval(Shape):
    def __init__(self, p=Point(), R=0, r=0):
        
        super().__init__()
        self.name = "Oval"
        self.p = p
        self.R = R
        self.r = r

    def square(self):
        return pi * self.R * self.r

    def perimeter(self):
        return 4.0 * (pi * self.R * self.r + (self.R - self.r)) / (self.R + self.r)


class Circle(Shape):
    def __init__(self, p=Point(), r=0.0):
       
        super().__init__()
        self.name = "Oval"
        self.p = p
        self.r = r

    def square(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2.0 * pi * self.r


class Triangle(Shape):
    def __init__(self, p0=Point(), p1=Point(), p2=Point()):
        
        super().__init__()
        self.name = "Triangle"
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2

    def square(self):
        return 0.5 * ((self.p1 - self.p0) * (self.p2 - self.p0))

    def perimeter(self):
        return (
            (self.p1 - self.p0).norm()
            + (self.p2 - self.p1).norm()
            + (self.p0 - self.p2).norm()
        )


class Rhombus(Quadrangle):
    def __init__(self, p0=Point(), p1=Point(), p2=Point(), p3=Point()):
        
        super().__init__(p0, p1, p2, p3)
        self.name = "Rhombus"

    def square(self):
        return 0.5 * (self.p2 - self.p0).norm() * (self.p3 - self.p1).norm()


if __name__ == "__main__":
    print("Пример:")
    print("Создадим четырёхугольник (0,1) (1,0) (0,-1) (-3, 0)")
    q = Quadrangle(Point(0, 1), Point(1, 0), Point(0, -1), Point(-2, 0))
    print(q)

    print("\nСоздадим прямоугольник (0,0) (10,0) (10,2) (0,2)")
    r = Rectangle(Point(0, 0), Point(10, 0), Point(10, 2), Point(0, 2))
    print(r)

    print("\nСоздадим овал с диагоналями 8 и 4 в точке (0,0)")
    o = Oval(Point(0, 0), 8, 4)
    print(o)

    print("\nСоздадим круг с радиусом 8 в точке (0,0)")
    c = Circle(Point(0, 0), 8)
    print(c)

    print("\nСоздадим треугольник (0,0) (4,0) (0,2")
    t = Triangle(Point(0, 0), Point(4, 0), Point(0, 2))
    print(t)

    print("\nСоздадим ромб (0,4) (2,0) (0,-4) (-2,0)")
    rh = Rhombus(Point(0, 4), Point(2, 0), Point(0, -4), Point(-2, 0))
    print(rh)
