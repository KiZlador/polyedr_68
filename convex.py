from deq import Deq
from r2point import R2Point
from modification import Circle_perimeter


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def perimeter_in_circle(self):
        return 0.0

    def area(self):
        return 0.0


class Void(Figure):
    """ "Hульугольник" """

    def add(self, p, d):
        return Point(p, d)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p, d):
        self.p = p
        self.d = d

    def add(self, q):
        return self if self.p == q else Segment(self.p, q, self.d)


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q, d):
        self.p, self.q = p, q
        self.d = d

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def perimeter_in_circle(self):
        return 2.0 * self.d.ans_recount(self.p, self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r, self.d)
        elif self.q.is_inside(self.p, r):
            return Segment(self.p, r, self.d)
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q, self.d)
        else:
            return self


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c, d):
        self.d = d
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._perimeter_in_circle = self.d.ans_recount(a, b)
        self._perimeter_in_circle += self.d.ans_recount(b, c)
        self._perimeter_in_circle += self.d.ans_recount(c, a)
        self._area = abs(R2Point.area(a, b, c))

    def perimeter(self):
        return self._perimeter

    def perimeter_in_circle(self):
        return self._perimeter_in_circle

    def area(self):
        return self._area

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            pt1 = self.points.first()
            pt2 = self.points.last()
            self._perimeter_in_circle -= self.d.ans_recount(pt1, pt2)
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                pt1 = self.points.first()
                self._perimeter_in_circle -= self.d.ans_recount(p, pt1)
                self._area += abs(R2Point.area(t, p, self.points.first()))
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                pt1 = self.points.last()
                self._perimeter_in_circle -= self.d.ans_recount(p, pt1)
                self._area += abs(R2Point.area(t, p, self.points.last()))
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            pt1 = self.points.first()
            pt2 = self.points.last()
            self._perimeter_in_circle += self.d.ans_recount(t, pt1)
            self._perimeter_in_circle += self.d.ans_recount(t, pt2)
            self.points.push_first(t)

        return self


if __name__ == "__main__":
    f = Void()
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
