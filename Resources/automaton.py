from Resources.cell import Cell
import itertools
from random import randint
from math import inf


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
        color = None
        posX = 0
        posY = 0
        for i in range(lim):
            num = randint(0, limN)
            if num is 0:
                color = (143, 138, 137)
            elif num is 1:
                color = (0, 214, 191)
            elif num is 2:
                color = (214, 159, 0)
            elif num is 3:
                color = (214, 0, 0)
            elif num is 4:
                color = (175, 0, 214)
            cell = Cell(posX, posY, color, num, "Resources/sounds/" +
                        instruments[0] + "/" + instruments[0] + "" + str(num) + ".ogg")
            cellT = Cell(posX + 470, posY, cell.color, cell.number, "Resources/sounds/" +
                         instruments[1] + "/" + instruments[1] + "" + str(cell.number) + ".ogg")
            cellTh = Cell(posX + 940, posY, cell.color, cell.number, "Resources/sounds/" +
                          instruments[2] + "/" + instruments[2] + "" + str(cell.number) + ".ogg")
            vector.append(cell)
            vectorT.append(cellT)
            vectorTh.append(cellTh)
            posX += 40
        self.cells.append(vector)
        self.cellsT.append(vectorT)
        self.cellsTh.append(vectorTh)
        self.createCellR(comb, vector, instruments, posY + 40)

    def createCellR(self, comb, vector, instruments, posY):
        try:
            Prev = 0
            Curr = 0
            Post = 0
            vect = []
            vectT = []
            vectTh = []
            color = None
            posX = 0
            for i in range(len(vector)):
                if posX is 0:
                    posX = vector[i].posX
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
                        color = (143, 138, 137)
                    elif number is 1:
                        color = (0, 214, 191)
                    elif number is 2:
                        color = (214, 159, 0)
                    elif number is 3:
                        color = (214, 0, 0)
                    elif number is 4:
                        color = (175, 0, 214)
                    cell = Cell(posX, posY, color, number, "Resources/sounds/" +
                                instruments[0] + "/" + instruments[0] + "" + str(number) + ".ogg")
                    cellT = Cell(posX + 470, posY, cell.color, cell.number, "Resources/sounds/" +
                                 instruments[1] + "/" + instruments[1] + "" + str(number) + ".ogg")
                    cellTh = Cell(posX + 940, posY, cell.color, cell.number, "Resources/sounds/" +
                                  instruments[2] + "/" + instruments[2] + "" + str(number) + ".ogg")
                    vect.append(cell)
                    vectT.append(cellT)
                    vectTh.append(cellTh)
                    Prev = 0
                    Curr = 0
                    Post = 0
                    posX = 0
            self.cells.append(vect)
            self.cellsT.append(vectT)
            self.cellsTh.append(vectTh)
            self.createCellR(comb, vect, instruments, posY + 40)
        except RecursionError as re:
            return True

    def validateTuple(self, point, comb):
        for points in comb:
            if points[0] == point:
                return points[1]
        return -1
