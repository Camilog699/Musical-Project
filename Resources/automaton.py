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
        vectt = []
        vecth = []
        color = None
        for i in range(lim):
            num = randint(0, limN)
            if num is 0:
                color = (241, 243, 244)
            elif num is 1:
                color = (0, 214, 191)
            elif num is 2:
                color = (214, 159, 0)
            elif num is 3:
                color = (214, 0, 0)
            elif num is 4:
                color = (175, 0, 214)
            cell = Cell(0, 0, color, num, "Resources/sounds/" +
                        instruments[0] + "/" + instruments[0] + "" + str(num) + ".wav")
            cellT = Cell(0, 0, cell.color, cell.number, "Resources/sounds/" +
                         instruments[1] + "/" + instruments[1] + "" + str(cell.number) + ".wav")
            cellTh = Cell(0, 0, cell.color, cell.number, "Resources/sounds/" +
                          instruments[2] + "/" + instruments[2] + "" + str(cell.number) + ".wav")
            vector.append(cell)
            vectorT.append(cellT)
            vectorTh.append(cellTh)
            vect.append(cell.file)
            vectt.append(cellT.file)
            vecth.append(cellTh.file)
        self.cells.append(vector)
        self.cellsT.append(vectorT)
        self.cellsTh.append(vectorTh)
        self.createCellR(comb, vector, instruments)

    def createCellR(self, comb, vector, instruments):
        if len(self.cells) == 100:
            return True
        Prev = 0
        Curr = 0
        Post = 0
        vect = []
        vectT = []
        vectTh = []
        color = None
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
            if (number != -1):
                if number is 0:
                    color = (241, 243, 244)
                elif number is 1:
                    color = (0, 214, 191)
                elif number is 2:
                    color = (214, 159, 0)
                elif number is 3:
                    color = (214, 0, 0)
                elif number is 4:
                    color = (175, 0, 214)
                cell = Cell(0, 0, color, number, "Resources/sounds/" +
                            instruments[0] + "/" + instruments[0] + "" + str(number) + ".wav")
                cellT = Cell(0, 0, cell.color, cell.number, "Resources/sounds/" +
                             instruments[1] + "/" + instruments[1] + "" + str(number) + ".wav")
                cellTh = Cell(0, 0, cell.color, cell.number, "Resources/sounds/" +
                              instruments[2] + "/" + instruments[2] + "" + str(number) + ".wav")
                vect.append(cell)
                vectT.append(cell)
                vectTh.append(cell)
                Prev = 0
                Curr = 0
                Post = 0
        self.cells.append(vect)
        self.cellsT.append(vectT)
        self.cellsTh.append(vectTh)
        self.createCellR(comb, vect, instruments)

    def validateTuple(self, point, comb):
        for points in comb:
            if points[0] == point:
                return points[1]
        return -1
