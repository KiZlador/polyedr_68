from shadow.polyedr import Polyedr
from pytest import approx
from modification import Square

class TestPolyedr:

#квадрат 2X2 у которого нет хороших вершин
    def test_square1(self):
        p = Polyedr("data/test1.geom")
        ans = Square(f"data/test1.geom")
        assert ans.square() == 4
#Куб, грань которого - квадрат 2X2, у которого нет хороших вершин
    def test_square2(self):
        p = Polyedr("data/test2.geom")
        ans = Square(f"data/test2.geom")
        assert ans.square() == 24
#Коробка, грань которой - квадрат 2X2, у которой нет хороших вершин
    def test_square3(self):
        p = Polyedr("data/test3.geom")
        ans = Square(f"data/test3.geom")
        assert ans.square() == 20
#Квадрат, у которого все вершины - хорошие
    def test_square4(self):
        p = Polyedr("data/test4.geom")
        ans = Square(f"data/test4.geom")
        assert ans.square() == 0
#Куб, у которого все вершины хорошие
    def test_square5(self):
        p = Polyedr("data/test5.geom")
        ans = Square(f"data/test5.geom")
        assert ans.square() == 0
#Коробка, у которой все вершины - хорошие
    def test_square6(self):
        p = Polyedr("data/test6.geom")
        ans = Square(f"data/test6.geom")
        assert ans.square() == 0
#Квадрат 5x5, у которого 2 вершины хорошие
    def test_square7(self):
        p = Polyedr("data/test7.geom")
        ans = Square(f"data/test7.geom")
        assert ans.square() == 25
#Куб, с гранью 5x5, у которого только две грани имеют не боллее двух хороших вершин
    def test_square8(self):
        p = Polyedr("data/test8.geom")
        ans = Square(f"data/test8.geom")
        assert ans.square() == 50
#Коробка, с гранью 5x5, у которой только одна грань имеет не боллее двух хороших вершин
    def test_square9(self):
        p = Polyedr("data/test9.geom")
        ans = Square(f"data/test9.geom")
        assert ans.square() == 25
