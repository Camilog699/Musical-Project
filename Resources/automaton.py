from Resources.cell import Cell
import itertools
from random import randint


class Automaton:
    def __init__(self):
        self.cells = []
        self.cellsT = []
        self.cellsTh = []

    def createBase(self, num):
        arr = []
        for base in range(num):
            arr.append(base)
        comb = list(itertools.product(arr, repeat=3))
        comb = self.assign(comb, num - 1)
        return comb

    def assign(self, arr, lim):
        newArr = []
        for num in arr:
            num2 = randint(0, lim)
            newArr.append([num, num2])
        return newArr

    def createCell(self, comb, lim, limN, instruments):
        vector = []
        vectorT = []
        vectorTh = []
        vect = []
        for i in range(lim):
            cell = Cell(0, 0, "#FFFFFF", randint(0, limN), "")
            cellT = Cell(0, 0, cell.color, cell.number, "")
            cellTh = Cell(0, 0, cell.color, cell.number, "")
            vector.append(cell)
            vectorT.append(cellT)
            vectorTh.append(cellTh)
            vect.append(cell.number)
        self.cells.append(vector)
        self.cellsT.append(vectorT)
        self.cellsTh.append(vectorTh)
        self.createCellR(comb, vector)

    def createCellR(self, comb, vector):
        if len(self.cells) == 100:
            return True
        Prev = 0
        Curr = 0
        Post = 0
        vect = []
        vectT = []
        vectTh = []
        vecto = []
        for i in range(len(vector)):
            if i == 0:
                Curr = vector[i].number
                Post = vector[i + 1].number
            elif i > 0 and i < len(vector) - 1:
                Prev = vector[i - 1].number
                Curr = vector[i].number
                Post = vector[i + 1].number
            elif i == len(vector) - 1:
                Prev = vector[i - 1].number
                Curr = vector[i].number
            point = (Prev, Curr, Post)
            number = self.validateTuple(point, comb)
            if(number != -1):
                cell = Cell(0, 0, "#FFFFFF", number, "")
                cellT = Cell(0, 0, cell.color, cell.number, "")
                cellTh = Cell(0, 0, cell.color, cell.number, "")
                vect.append(cell)
                vectT.append(cell)
                vectTh.append(cell)
                vecto.append(cell.number)
                Prev = 0
                Curr = 0
                Post = 0
        self.cells.append(vect)
        self.cellsT.append(vectT)
        self.cellsTh.append(vectTh)
        self.createCellR(comb, vect)

    def validateTuple(self, point, comb):
        for points in comb:
            if points[0] == point:
                return points[1]
        return -1
