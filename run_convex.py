#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void
from modification import Circle_perimeter

f = Void()
try:
    X = float(input("Введите x координату центра круга -> "))
    Y = float(input("Введите y координату центра круга -> "))
    R = float(input("Введите значение радиуса -> "))
    d = Circle_perimeter(X, Y, R)
    d_ed = False
    while True:
        if not d_ed:
            f = f.add(R2Point(), d)
            d_ed = True
        else:
            f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}")
        print(f"P части выпуклой оболочки внутри замкнутого круга:")
        print(f"{f.perimeter_in_circle()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
