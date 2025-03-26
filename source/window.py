import pygame


class WindowTemplate:
    _win: pygame.Surface

    def draw(self) -> None:
        pass
    
    def key(self, key) -> None:
        pass

    def event(self, event) -> None:
        pass

    def draw_background(self) -> None:
        pass
