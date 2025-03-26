import pygame

from source.hitbox import HitBox

class Button:
    _win: pygame.Surface

    def __init__(self, window, x, y, width, height):
        self._win = window
        self._x = int(x - (width//2))
        self._y = int(y - (height//2))
        self._width = width
        self._height = height
        self._hitbox = HitBox(width, height, window)

    def draw(self):
        self._hitbox.update(self._x, self._y)
        self._hitbox.draw()

    def is_pressed(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self._rect.collidepoint(event.pos):
            self._clicked = True
            self._click_timer = pygame.time.get_ticks()
            return True
        return False


