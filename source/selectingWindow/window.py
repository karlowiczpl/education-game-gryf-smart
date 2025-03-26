import pygame
from source import window
from source.window import WindowTemplate

from .button import Button
from .example import Example

examples = [
    pygame.image.load("source/selectingWindow/img/example1.png")
]

class SelectingWindow(WindowTemplate):
    _win: pygame.Surface

    def __init__(self, win):
        self._win = win
        self.background_image = pygame.image.load("source/selectingWindow/img/background.jpg")
        self.resize_background() 
        width, height = self._win.get_size()
        # self._buttons = [Button(win, width//2, height//2, 500, 200)]
        self._examples = []
        print(width,height)
        self._examples.append(Example(win, width * (2/10), height//3, examples[0]))
        self._examples.append(Example(win, width * (5/10), height//3, examples[0]))
        self._examples.append(Example(win, width * (8/10), height//3, examples[0]))

    def resize_background(self):
        self.background_image = pygame.transform.scale(self.background_image, self._win.get_size())

    def draw(self):
        # for button in self._buttons:
        #     button.draw()

        for example in self._examples:
            example.draw()

    def draw_background(self):
        self._win.blit(self.background_image, (0, 0))

    def event(self, event):
        for example in self._examples:
            example.event(event)


