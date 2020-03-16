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
        screen = pygame.display.set_mode(self.screen_size())
        pygame.display.set_caption('Automaton')

        for i in self.automaton.cells:
            for num in self.automaton.cells[i]:
                data = num
                # conditions to assignment of colors
                self.assignColors(data, screen)

        while True:
            screen.fill((0, 0, 0))
            if event.type is pygame.QUIT:
                pygame.quit()
                sys.exit()
            pygame.display.update()

    def assignColors(self, data, screen):
        # colors
        green = (39, 214, 0)
        blue = (0, 214, 191)
        orange = (214, 159, 0)
        red = (214, 0, 0)
        purple = (175, 0, 214)

        if data == 0:
            pygame.draw.polygon(screen, green, )
