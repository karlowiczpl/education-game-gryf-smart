import asyncio
import pygame
from source.singleton import gl_data
from source.selectingWindow import SelectingWindow
from source.const import (
    CONF_SELECTED_WINDOW,
    CONF_CONNECTING_MODE,
)

pygame.init()
window = pygame.display.set_mode()

async def main():
    gl_data[CONF_SELECTED_WINDOW] = SelectingWindow(window)
    gl_data[CONF_CONNECTING_MODE] = False

    isRunning = True
    while isRunning:
        selected_window = gl_data[CONF_SELECTED_WINDOW]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

            selected_window.event(event)


        selected_window.draw_background()
        selected_window.draw()
        pygame.display.update()


        await asyncio.sleep(0.02)

if __name__ == "__main__":
    asyncio.run(main())


