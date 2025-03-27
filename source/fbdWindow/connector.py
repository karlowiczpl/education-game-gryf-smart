import pygame

from source.hitbox import HitBox
from source.singleton import gl_data
from source.const import CONF_CONNECTING_MODE

from .cable import Cable

class Connector:
    def __init__(self, win, index):
        self._x = 0
        self._y = 0
        self._win = win
        self._index = index
        self._hitbox = HitBox(20, 20, win)
        self._cable_array = []

        if not index:
            self._x_offset = 10
            self._y_offset = 12
        elif index == 1:
            self._x_offset = 10
            self._y_offset = 64
        else:
            self._x_offset = 178
            self._y_offset = 38

    def draw(self, x, y):
        self._x = x
        self._y = y

        self._hitbox.update(x + self._x_offset, y + self._y_offset)
        self._hitbox.draw()

        for cable in self._cable_array:
            if cable.draw():
                self._cable_array.remove(cable)

    def event(self, event):
        for cable in self._cable_array:
            cable.event(event)
        if hasattr(event, "type"):
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if self._hitbox.rect.collidepoint(event.pos) and not gl_data[CONF_CONNECTING_MODE]:
                    gl_data[CONF_CONNECTING_MODE] = True
                    self._cable_array.append(Cable(self, self._x + self._x_offset, self._y + self._y_offset))
