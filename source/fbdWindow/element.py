import pygame

from source.hitbox import HitBox
from source.singleton import gl_data
from source.const import CONF_LEFT_BAR_SIZE, CONF_NET, CONF_CONNECTING_MODE

from .connector import Connector

class Element:
    _win: pygame.Surface

    def __init__(self, x, y, win, image):
        self._x = x
        self._y = y
        self._win = win
        self._dragging = False
        self._offset_x = 0
        self._offset_y = 0
        self._net = gl_data[CONF_NET]

        original_width, original_height = image.get_size()
        new_height = int(200 * original_height/original_width)  
        self._image = pygame.transform.scale(image, (200, new_height))
        self._hitbox = HitBox(self._image.get_width(), self._image.get_height(), win)
        self._connectors = [
            Connector(win, 0),
            Connector(win, 1),
            Connector(win, 2),
        ]


    def draw(self):
        x = self._x * 20 + gl_data[CONF_LEFT_BAR_SIZE]
        y = self._y * 20
        
        self._win.blit(self._image, (x, y))
        self._hitbox.update(x, y)
        self._hitbox.draw()
        
        for connector in self._connectors:
            connector.draw(x, y)

    def event(self, event):
        for connector in self._connectors:
            connector.event(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                gl_data[CONF_CONNECTING_MODE] = False

        if not gl_data[CONF_CONNECTING_MODE]:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos

                if self._hitbox.rect.collidepoint(event.pos):
                    self._dragging = True
                    self._offset_x = self._x * 20 - mouse_x
                    self._offset_y = self._y * 20 - mouse_y

            elif event.type == pygame.MOUSEBUTTONUP:
                self._dragging = False

            elif event.type == pygame.MOUSEMOTION and self._dragging:
                mouse_x, mouse_y = event.pos
                x = (mouse_x + self._offset_x) // 20
                y = (mouse_y + self._offset_y) // 20
                max_x, max_y = self._net.max_grid_size
                if x > 0 and x < max_x - 8:
                    self._x = x
                if y >= 0 and y < max_y - 7:
                    self._y = y

    @property
    def image(self):
        return self._image

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
