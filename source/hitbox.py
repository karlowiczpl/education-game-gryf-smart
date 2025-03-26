import pygame

class HitBox:

    def __init__(self, width, height, window, posX=0, posY=0) -> None:
        self._win = window
        self._width = width
        self._height = height
        self._x = posX
        self._y = posY
        
    def update(self, x, y):
        self._x = x
        self._y = y

    def draw(self):
        pygame.draw.rect(self._win, (255,0,0), (self._x, self._y, self._width, self._height), 3)

    @property
    def rect(self) -> pygame.Rect:
        return pygame.Rect(self._x, self._y, self._width, self._height)
