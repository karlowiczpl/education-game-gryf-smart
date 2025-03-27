import pygame
from source.window import WindowTemplate
from source.singleton import gl_data
from source.const import CONF_NET

from .scrolArea import ScrolArea
from .net import Net
from .element import Element

sample_image = pygame.image.load("source/fbdWindow/img/and.png")

examples = [
    pygame.image.load("source/selectingWindow/img/example1.png")
]

class FbdWindow(WindowTemplate):
    _win: pygame.Surface
    def __init__(self, win, exampleNumber, dificult):
        self._win = win
        self._scrol_area = ScrolArea(win)
        self._net = Net(win)
        gl_data[CONF_NET] = self._net
        self._scrol_area_size = 0
        self._elements = [Element(1,1,win,sample_image), Element(30,30,win,sample_image)]

    def event(self, event):
        self._scrol_area.event(event)
        self._net.event(event)
        for element in self._elements:
            element.event(event)

    def draw_background(self):
        self._win.fill((255, 255, 255))
        self._net.draw(self._scrol_area_size)
        self._scrol_area_size = self._scrol_area.draw()
        for element in self._elements:
            element.draw()
