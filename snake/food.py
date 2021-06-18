from .body import Body
import pygame
from .helper import *

class Food(Body):
    def __init__(self, x, y, vx, vy, color, eaten):
        super().__init__(x, y, vx, vy)
        self.color = color
        self.eaten = eaten
    def draw(self):
        global WIN
        pygame.draw.rect(WIN, self.color, rect(self.x, self.y))

    def is_eaten(self, other):
        if self.x == other.x and self.y == other.y:
            self.eaten = True
 
