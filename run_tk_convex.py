#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon
from modification import Circle_perimeter


def void_draw(self, tk):
    pass


def point_draw(self, tk):
    tk.draw_point(self.p)


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
tk.clean()
f = Void()

try:
    X = float(input("Введите x координату центра круга -> "))
    Y = float(input("Введите y координату центра круга -> "))
    R = float(input("Введите значение радиуса -> "))
    d = Circle_perimeter(X, Y, R)
    tk.draw_circle(R2Point(X, Y), R)
    d_ed = False
    while True:
        if not d_ed:
            f = f.add(R2Point(), d)
            d_ed = True
        else:
            f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        tk.draw_circle(R2Point(X, Y), R)
        print(f"S = {f.area()}, P = {f.perimeter()}\n")
        print(f"P части выпуклой оболочки внутри замкнутого круга:")
        print(f"{f.perimeter_in_circle()}")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
