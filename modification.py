from math import pi
from functools import reduce
from operator import add
from common.r3 import R3
from common.tk_drawer import TkDrawer
from math import sqrt
from shadow.polyedr import Polyedr,Facet,Edge

class Square:
    def __init__(self, file):

        # списки вершин, рёбер и граней полиэдра
        self.vertexes, self.edges, self.facets = [], [], []

        # список строк файла
        with open(file) as f:
            for i, line in enumerate(f):
                if i==0:
                    buf = line.split()
                elif i == 1:
                    # во второй строке число вершин, граней и рёбер полиэдра
                    nv, nf, ne = (int(x) for x in line.split())
                elif i < nv + 2:
                    # задание всех вершин полиэдра
                    x, y, z = (float(x) for x in line.split())
                    self.vertexes.append(R3(x, y, z))
                else:
                    # вспомогательный массив
                    buf = line.split()
                    # количество вершин очередной грани
                    size = int(buf.pop(0))
                    # массив вершин этой грани
                    vertexes = list(self.vertexes[int(n) - 1] for n in buf)
                    # задание рёбер грани
                    for n in range(size):
                        self.edges.append(Edge(vertexes[n - 1], vertexes[n]))
                    # задание самой грани
                    self.facets.append(Facet(vertexes))

    def square(self):
        S=0
        for f in self.facets:
            d=0
            s=0
            for i in range(len(f.vertexes)):
                if f.vertexes[i].y>1 or f.vertexes[i].y<-3:
                    d+=1
                if d>2:
                    break
            if d<=2:
                for i in range(2,len(f.vertexes)):
                    a=f.vertexes[i].__sub__(f.vertexes[0])
                    b=f.vertexes[i-1].__sub__(f.vertexes[0])
                    res=a.cross(b)
                    s+=sqrt(res.x**2+res.y**2+res.z**2)
            S+=s
        return S/2
