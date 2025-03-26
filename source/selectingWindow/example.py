import pygame

from source.hitbox import HitBox
from source.singleton import gl_data
from source.const import CONF_SELECTED_WINDOW
from source.fbdWindow import FbdWindow

class Example:
    _win: pygame.Surface

    def __init__(self, window, x, y, image):
        self._width = 700
        self._height = 700
        self._win = window
        self._x = int(x - (self._width//2))
        self._y = int(y - (self._height//2))
        self._start_x = x
        self._start_y = y
        self._hitbox = HitBox(self._width, self._height, window)
        self._image = image
        self._first_image = image
        self._animation_counter = 0
        self._animation_enable = False

    def draw(self):
        if self.is_hovered():
            if self._animation_enable:
                if self._animation_counter < 5:
                    self._width += 15
                    self._height += 15
                    self._animation_counter += 1
            else:
                self._animation_enable = True
                self._animation_counter = 0
        else:
            if self._animation_enable:
                self._width = 700
                self._height = 700
                self._animation_enable = False
                self._image = self._first_image


        self._x = int(self._start_x - (self._width//2))
        self._y = int(self._start_y - (self._height//2))
        self._image = pygame.transform.scale(self._first_image, (self._height,self._width))
        self._hitbox.update(self._x, self._y)
        self._win.blit(self._image, (self._x, self._y))
        pygame.draw.rect(self._win, (0x00,0x00,0x00), (self._x, self._y, self._height, self._width), 10)

    def event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect = pygame.Rect(self._x, self._y, self._width, self._height)
            if rect.collidepoint(event.pos):
                gl_data[CONF_SELECTED_WINDOW] = FbdWindow(self._win, 0, 1)

    def is_hovered(self):
        mouse_pos = pygame.mouse.get_pos()
        rect = pygame.Rect(self._x, self._y, self._width, self._height)
        return rect.collidepoint(mouse_pos)
        



