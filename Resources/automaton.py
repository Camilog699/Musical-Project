from Resources.cell import Cell
import itertools
from random import randint


class Automaton:
    def __init__(self):
        self.cells = []

    def createBase(self, num):
        arr = []
        for base in range(num):
            arr.append(base)
        comb = list(itertools.product(arr, repeat=num))
        comb = self.assign(comb, num-1)
        return comb

    def assign(self, arr, lim):
        newArr = []
        for num in arr:
            num2 = randint(0, lim)
            newArr.append([num, num2])
        return newArr

    def createCell(self, comb, lim, limN, base):
        vector = []
        for i in range(lim):
            cell = Cell(0, 0, "#FFFFFF", randint(0, limN), "")
            vector.append(cell)
        self.cells.append(vector)
        self.createCellR(comb, 0, base)

    def createCellR(self, comb, Pos, base):
        point = (0)
        vector = []
        create = False
        for i in range(self.cells[Pos]):
            if (i + base) % base is 0:
                point.append(self.cells[Pos][i])
                for points in comb:
                    if point == points[0]:
                        cell = Cell(0, 0, "#FFFFFF", points[1], "")
                        vector.append(cell)
                        create = True
                        break
                if not create:
                    point.append(self.cells[Pos][i + 1])


    def validatePoint(self, point, comb):
        pass
