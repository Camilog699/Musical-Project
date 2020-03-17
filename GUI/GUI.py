import pygame
import sys
import subprocess
import os
import ctypes
from time import sleep
pygame.init()


class GUI:
    def __init__(self, automaton):
        self.automaton = automaton
        self.i = 0
        self.draw()

    def screen_size(self):
        size = (None, None)
        args = ["xrandr", "-q", "-d", ":0"]
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if isinstance(line, bytes):
                line = line.decode("utf-8")
                if "Screen" in line:
                    size = (int(line.split()[7]), int(line.split()[9][:-1]))
        return size

    def draw(self):
        screen = pygame.display.set_mode(self.screen_size(), pygame.RESIZABLE)
        pygame.display.set_caption('Automaton')
        cont = True

        while True:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            while cont:
                self.drawAuto(screen)
                if self.i == 0:
                    sleep(1.5)
                cont = self.generateChange(screen)
            pygame.display.update()

    def drawAuto(self, screen):
        for i in range(len(self.automaton.cells)):
            for j in range(len(self.automaton.cells[i])):
                # conditions to assignment of colors
                self.assignColors(
                    self.automaton.cells[i][j], self.automaton.cellsT[i][j], self.automaton.cellsTh[i][j], screen)
        pygame.display.update()

    def assignColors(self, cell, cellT, cellTh, screen):
        white = (255, 255, 255)
        black = (0, 0, 0)

        if cell.paint:
            pygame.draw.rect(
                screen, cell.color, ((cell.posX + 2.9, cell.posY + 2.9, 30, 30)))
        else:
            pygame.draw.rect(
                screen, white, ((cell.posX + 2.9, cell.posY + 2.9, 30, 30)))
        if cellT.paint:
            pygame.draw.rect(
                screen, cellT.color, ((cellT.posX + 2.9, cellT.posY + 2.9, 30, 30)))
        else:
            pygame.draw.rect(
                screen, white, ((cellT.posX+2.9, cellT.posY+2.9, 30, 30)))
        if cellTh.paint:
            pygame.draw.rect(
                screen, cellTh.color, ((cellTh.posX + 2.9, cellTh.posY + 2.9, 30, 30)))
        else:
            pygame.draw.rect(
                screen, white, ((cellTh.posX+2.9, cellTh.posY+2.9, 30, 30)))

    def generateChange(self, screen):
        i = self.i
        j = 0
        while i < len(self.automaton.cells):
            while j < len(self.automaton.cells[i]):
                self.automaton.cells[i][j].paint = True
                self.automaton.cellsT[i][j].paint = True
                self.automaton.cellsTh[i][j].paint = True
                song = pygame.mixer.Sound(self.automaton.cells[i][j].file)
                songT = pygame.mixer.Sound(self.automaton.cellsT[i][j].file)
                songTh = pygame.mixer.Sound(self.automaton.cellsTh[i][j].file)
                songTh.play()
                songT.play()
                song.play()
                sleep(0.5)
                pygame.draw.rect(screen, self.automaton.cells[i][j].color, ((
                    self.automaton.cells[i][j].posX + 2.9, self.automaton.cells[i][j].posY + 2.9, 30, 30)))
                pygame.draw.rect(screen, self.automaton.cellsT[i][j].color, ((
                    self.automaton.cellsT[i][j].posX + 2.9, self.automaton.cellsT[i][j].posY + 2.9, 30, 30)))
                pygame.draw.rect(screen, self.automaton.cellsTh[i][j].color, ((
                    self.automaton.cellsTh[i][j].posX + 2.9, self.automaton.cellsTh[i][j].posY + 2.9, 30, 30)))
                pygame.display.update()
                sleep(0.9)
                song.stop()
                songT.stop()
                songTh.stop()
                sleep(0.1)
                j += 1
            if i >= 17 and i < len(self.automaton.cells):
                i += 1
                self.i = i
                self.revaluate(screen)
                return True
            i += 1
            self.i = i
            j = 0
        return False

    def revaluate(self, screen):
        for i in range(len(self.automaton.cells)):
            for j in range(len(self.automaton.cells[i])):
                self.automaton.cells[i][j].posY -= 40
                self.automaton.cellsT[i][j].posY -= 40
                self.automaton.cellsTh[i][j].posY -= 40
