import pygame

from source.fbdWindow.element import Element
from source.singleton import gl_data
from source.const import CONF_LEFT_BAR_SIZE

class Connection:
    _element0: Element
    _element1: Element | None
    _win: pygame.Surface

    def __init__(self, element: Element, window: pygame.Surface):
        self._element0 = element
        self._element1 = None
        self._win = window

    def draw(self):
        pass
        # if self._element1 = None:

        
