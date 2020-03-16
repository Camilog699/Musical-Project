import pygame
import sys
import subprocess
import os
import ctypes
pygame.init()


class GUI:
    def __init__(self, automaton):
        self.automaton = automaton
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

        while True:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.drawAuto(screen)
            pygame.display.update()

    def drawAuto(self, screen):
        x = 0
        y = 0
        for i in range(len(self.automaton.cells)):
            for j in range(len(self.automaton.cells[i])):
                # conditions to assignment of colors
                self.assignColors(self.automaton.cells[i][j], self.automaton.cellsT[i][j], self.automaton.cellsTh[i][j], screen)
            y = y + 40
            x = 0

    def assignColors(self, cell, cellT, cellTh, screen):
        white = (255, 255, 255)
        black = (0, 0, 0)

        pygame.draw.rect(screen, black, ((cell.posX, cell.posY, 35, 35)), 1)
        pygame.draw.rect(screen, white, ((cell.posX+2.9, cell.posY+2.9, 30, 30)))

        pygame.draw.rect(screen, black, ((cellT.posX, cellT.posY, 35, 35)), 1)
        pygame.draw.rect(screen, white, ((cellT.posX+2.9, cell.posY+2.9, 30, 30)))

        pygame.draw.rect(screen, black, ((cellTh.posX, cellTh.posY, 35, 35)), 1)
        pygame.draw.rect(screen, white, ((cellTh.posX+2.9, cellTh.posY+2.9, 30, 30)))
