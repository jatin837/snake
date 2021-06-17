import pygame

RED = (255, 0, 0)
BLACK = (0, 0, 0)
DISPLAY_WIDTH:int = 500
DISPLAY_HEIGHT:int = 500

WIN:any = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

CRASHED:bool = False
GRIDWIDTH:int = 25



AVAILABLE:list = []
clock = pygame.time.Clock()


convert = lambda x: x*GRIDWIDTH # convert coordinate into grid location
i_convert = lambda x: x/GRIDWIDTH # inverse of convert function

rect = lambda x, y: pygame.Rect(x, y, GRIDWIDTH, GRIDWIDTH)