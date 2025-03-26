import pygame

class Gate:
    _win: pygame.Surface

    def __init__(self, x, y, win, image):
        self._x = x
        self._y = y
        self._win = win
        self._image = image
        self._scale = 1.0  
        self._hovered = False
        self._counter = 0

    def draw(self, height, width, x, y):
        rect = pygame.Rect(x, y, height * self._scale, width * self._scale)

        if rect.collidepoint(pygame.mouse.get_pos()):
            if self._counter < 5:  
                self._scale += 0.03
                self._counter += 1
            self._hovered = True
        else:
            if self._hovered:  
                self._scale = 1.0
                self._counter = 0
                self._hovered = False

        scaled_width = int(height * self._scale)
        scaled_height = int(width * self._scale)
        image = pygame.transform.scale(self._image, (scaled_width, scaled_height))

        new_x = x - (scaled_width - height) // 2
        new_y = y - (scaled_height - width) // 2

        self._win.blit(image, (new_x, new_y))
