import pygame
import subprocess
import os
import sys
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
        for num in self.automaton.cells:
            data = num
            # conditions to assignment of colors
            self.Assigncolors(data)

        screen = pygame.display.set_mode(self.screen_size())
        pygame.display.set_caption('Automaton')
