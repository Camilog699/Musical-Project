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

        x = 0
        y = 0
        for i in range(len(self.automaton.cells)):
            for num in self.automaton.cells[i]:
                if self.automaton.cells[0]:
                    data = num
                if self.automaton.cells[i]:
                    data = num
                    x = x + 30
                    # conditions to assignment of colors
                self.assignColors(data, x, y, screen)
            y = y + 30

        while True:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type is pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                pygame.display.update()

    def assignColors(self, data, x, y, screen):
        # colors
        green = (39, 214, 0)
        blue = (0, 214, 191)
        orange = (214, 159, 0)
        red = (214, 0, 0)
        purple = (175, 0, 214)

        if data is 0:
            pygame.draw.rect(screen, green, ((x, y), (30, 30)))
        elif data is 1:
            pygame.draw.rect(screen, blue, ((x, y), (30, 30)))
        elif data is 2:
            pygame.draw.rect(screen, orange, ((x, y), (30, 30)))
        elif data is 3:
            pygame.draw.rect(screen, red, ((x, y), (30, 30)))
        elif data is 4:
            pygame.draw.rect(screen, purple, ((x, y), (30, 30)))
