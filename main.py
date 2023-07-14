import pygame
pygame.init()
import content

WINDOWS_WIDTH = 1900
WINDOWS_HEIGHT = 80
MESSAGE_DELAY = 5

COLOR = (255, 255, 255)
BACKGROUND = (0, 0, 0)
FONT = pygame.font.Font("Calibri.ttf", 70)
CONTENT = [content.hello, content.sponsor, content.result]

display = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT), pygame.NOFRAME, pygame.NOEVENT)
def display_message(txt: str):
    print(txt)
    display.fill(BACKGROUND)
    txt_surface = FONT.render(txt, True, COLOR)
    txt_rect = txt_surface.get_rect()
    txt_rect.center = ((WINDOWS_WIDTH//2), (WINDOWS_HEIGHT//2))
    display.blit(txt_surface, txt_rect)
    pygame.display.update()

def message_generator():
    while True:
        for generator_func in CONTENT:
            lines = generator_func()
            for msg in lines:
                yield msg

if __name__ == '__main__':
    ptick = -MESSAGE_DELAY * 1000
    for msg in message_generator():
        while pygame.time.get_ticks() - ptick < MESSAGE_DELAY * 1000:
            pygame.event.pump()
        ptick = pygame.time.get_ticks()
        display_message(msg)
