import pygame

from source.hitbox import HitBox

from .gate import Gate
from source.singleton import gl_data
from source.const import CONF_LEFT_BAR_SIZE

gates = [
    pygame.image.load("source/fbdWindow/img/and.png"),
    pygame.image.load("source/fbdWindow/img/and.png"),
    pygame.image.load("source/fbdWindow/img/and.png"),
    pygame.image.load("source/fbdWindow/img/and.png"),
]

class ScrolArea:
    _win: pygame.Surface

    def __init__(self, win):
        self._gates = []
        for gate in gates:
            self._gates.append(Gate(100,100,win,gate))
        self._win = win
        width, height = self._win.get_size()
        self._win_height = height
        self._win_width = width
        self._left_menu_size = self._win_width // 7
        self._dragging = False  
        self._examples = []
        self._left_menu_hitbox = HitBox(10, self._win_height, win)

        gl_data[CONF_LEFT_BAR_SIZE] = self._left_menu_size

    def draw(self):
        # pygame.draw.rect(self._win, (255, 255, 255), (0, 0, self._left_menu_size, self._win_height))
        pygame.draw.rect(self._win, (0, 0, 0), (self._left_menu_size, 0, 10, self._win_height))
        self._left_menu_hitbox.update(self._left_menu_size, 0)

        # for i in range(len(self._gates)):
        #     x = [0, size//2]
        #     y = int(i/2) * size * 0.24
        #
        #     self._gates[i].draw(size*0.5,size*0.48*0.5,x[i%2],y)
        return self._left_menu_size

    def event(self, event):
        mouse_x, _ = pygame.mouse.get_pos()
        hitbox_rect = pygame.Rect(self._left_menu_size, 0, 10, self._win_height)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitbox_rect.collidepoint(mouse_x, 0):  
                self._dragging = True  

        elif event.type == pygame.MOUSEBUTTONUP:
            self._dragging = False  

        elif event.type == pygame.MOUSEMOTION and self._dragging:
            new_width = max((self._win_width//9), min(mouse_x, self._win_width//7))
            self._left_menu_size = new_width
            gl_data[CONF_LEFT_BAR_SIZE] = new_width
