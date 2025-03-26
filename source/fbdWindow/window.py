import pygame
from source.window import WindowTemplate

from .scrolArea import ScrolArea
from .net import Net

examples = [
    pygame.image.load("source/selectingWindow/img/example1.png")
]

class FbdWindow(WindowTemplate):
    _win: pygame.Surface
    def __init__(self, win, exampleNumber, dificult):
        self._win = win
        self._scrol_area = ScrolArea(win)
        self._net = Net(win)
        self._scrol_area_size = 0

    def event(self, event):
        self._scrol_area.event(event)
        self._net.event(event)

    def draw_background(self):
        self._win.fill((255, 255, 255))
        self._net.draw(self._scrol_area_size)
        self._scrol_area_size = self._scrol_area.draw()

