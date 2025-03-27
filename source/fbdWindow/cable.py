import pygame

from source.singleton import gl_data
from source.const import CONF_CONNECTING_MODE, CONF_LEFT_BAR_SIZE 

class Cable:
    def __init__(self, connector, x, y):
        self._connector = connector
        self._win = connector._win
        self._x = x
        self._y = y
        self._mouse_postion = (0,0)
        self._write = True
        self._postions = []

    def draw(self) -> bool:
        posX, posY = self._mouse_postion

        pygame.draw.line(self._win, (0,0,0), (self._x, self._y), ((posX * 20) + gl_data[CONF_LEFT_BAR_SIZE] + 10 , posY * 20), 5)

        for i in range(len(self._postions)):
            if not i:
                posX, posY = self._postions[i]
                pygame.draw.line(self._win, (0,0,0), (self._x, self._y), (posX * 20 + gl_data[CONF_LEFT_BAR_SIZE] + 10, posY* 20))

        return False

    def event(self, event):
        if self._write:
            if hasattr(event, "pos"):
                posX, posY = event.pos
                self._mouse_postion = ((posX - gl_data[CONF_LEFT_BAR_SIZE]) //20 , posY //20)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._postions.append(self._mouse_postion)
