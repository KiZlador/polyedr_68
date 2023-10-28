from r2point import R2Point
from math import sqrt
import sympy as sp
from deq import Deq


class Circle_perimeter:
    def __init__(self, X, Y, R):
        self.X, self.Y, self.R = X, Y, R

    def ans_recount(self, pt1, pt2):
        p1 = ((pt1.x-self.X)**2 + (pt1.y-self.Y)**2 <= self.R**2)
        p2 = ((pt2.x-self.X)**2 + (pt2.y-self.Y)**2 <= self.R**2)
        ans = 0
        if p1 and p2:
            ans += pt1.dist(pt2)
        else:
            x, y = sp.symbols('x y', real=True)
            x1, y1, x2, y2 = pt1.x, pt1.y, pt2.x, pt2.y
            if y1 == y2:
                f1 = sp.Eq(y, y1)
            elif x1 == x2:
                f1 = sp.Eq(x, x1)
            else:
                k = ((y2 - y1)/(x2 - x1))
                b = y2 - k*x2
                f1 = sp.Eq(y, k*x+b)
            f2 = sp.Eq((x-self.X)**2 + (y-self.Y)**2, self.R**2)
            sol_1 = sp.solve((f1, f2), (x, y))
            sol = []
            for i in sol_1:
                check_interval_x = i[0] >= min(x1, x2) and i[0] <= max(x1, x2)
                check_interval_y = i[1] >= min(y1, y2) and i[1] <= max(y1, y2)
                if check_interval_x and check_interval_y:
                    sol.append(i)
            if len(sol) == 2:
                point1 = R2Point(sol[0][0], sol[0][1])
                point2 = R2Point(sol[1][0], sol[1][1])
                ans += point1.dist(point2)
            elif len(sol) == 1:
                if p1:
                    point1 = R2Point(sol[0][0], sol[0][1])
                    ans += point1.dist(pt1)
                elif p2:
                    point1 = R2Point(sol[0][0], sol[0][1])
                    ans += point1.dist(pt2)
        return ans
