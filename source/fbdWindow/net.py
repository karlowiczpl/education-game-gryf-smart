from typing import LiteralString
import pygame

from .element import Element

from source.singleton import gl_data
from source.const import CONF_LEFT_BAR_SIZE

class Net:
    def __init__(self, win):
        self._win = win
        self._cell_size = 50  
        self._color = (200, 200, 200)
        self._font = pygame.font.SysFont(None, 24)
        self._win_width, self._win_height = self._win.get_size()
        self._area_size = 0
        self._distance = 20
        self._camera_position_x = 0
        self._camera_position_y = 0
        self._area_width = 0
        self._area_height = 0

    @property
    def max_grid_size(self):
        max_width = (self._win_width - self._left_bar_size) // self._distance
        max_height = self._win_height // self._distance
        return max_width, max_height

    def draw(self, left_bar_size):
        left_bar_size += 10
        self._left_bar_size = left_bar_size
        self._area_width = (self._win_width - left_bar_size) // self._distance
        self._area_height = self._win_height // self._distance

        i = 0
        while i < self._win_height:
            pygame.draw.line(self._win, self._color, (left_bar_size, i), (self._win_width, i))
            i += self._distance

        i = left_bar_size
        while i < self._win_width:
            pygame.draw.line(self._win, self._color, (i, 0), (i, self._win_height))
            i += self._distance

    def event(self, event):
        pass
