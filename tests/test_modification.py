from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon
from modification import Circle_perimeter


class TestPoint:
    def setup_method(self):
        self.X = 1
        self.Y = 2
        self.R = 4
        self.ans = 0
        self.f = Void()
        self.d = Circle_perimeter(self.X, self.Y, self.R)

    def test1(self):
        self.f = self.f.add(R2Point(1.0, 2.0), self.d)
        assert self.f.perimeter_in_circle() == 0

    def test2(self):
        self.f = self.f.add(R2Point(-4.0, 2.0), self.d)
        assert self.f.perimeter_in_circle() == 0


class TestSegment:
    def setup_method(self):
        self.X = 1
        self.Y = 2
        self.R = 4
        self.f = Void()
        self.d = Circle_perimeter(self.X, self.Y, self.R)

# отрезок не касается круга
    def test1(self):
        self.f = self.f.add(R2Point(-10.0, 0.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(0.0, 10.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 0

# отрезок лежит внутри круга (Является его диаметром)
    def test2(self):
        self.f = self.f.add(R2Point(-3.0, 2.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(5.0, 2.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 16

# отрезок пересекает круг два раза
    def test3(self):
        self.f = self.f.add(R2Point(-5.0, 2.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(7.0, 2.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 16

# отрезок пересекает круг один раз
    def test4(self):
        self.f = self.f.add(R2Point(-5.0, 2.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(1.0, 2.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 8

# отрезок касается окружности
    def test5(self):
        self.f = self.f.add(R2Point(-3.0, 6.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(5.0, 6.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 0


class TestPolygon:
    def setup_method(self):
        self.X = -1
        self.Y = 3
        self.R = 3
        self.f = Void()
        self.d = Circle_perimeter(self.X, self.Y, self.R)

    def test1(self):
        self.f = self.f.add(R2Point(-1.0, 0.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(2.0, 3.0))
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-4.0, 3.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 14.485281374238568  # 6+6*sqrt(2)

    def test2(self):
        self.f = self.f.add(R2Point(-1.0, 0.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(2.0, 3.0))
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-4.0, 3.0))
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-1.0, 6.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 16.970562748477136  # 12*sqrt(2)

# в круге содержится только ее часть
    def test3(self):
        self.f = self.f.add(R2Point(-4.0, -2.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(2.0, -2.0))
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-4.0, 3.0))
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(2.0, 3.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 6

    def test4(self):
        self.f = self.f.add(R2Point(-4.0, -2.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-1.0, -2.0))
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-1.0, 3.0))
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-4.0, 3.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 6

    def test5(self):
        self.f = self.f.add(R2Point(-4.0, -2.0), self.d)
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-1.0, -2.0))
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-4.0, -1.0))
        self.ans = self.f.perimeter_in_circle()
        self.f = self.f.add(R2Point(-1.0, -1.0))
        self.ans = self.f.perimeter_in_circle()
        assert self.ans == 0
