import pygame
from body import Body
from helper import *


class Snake:
    def __init__(self):
        self.turningPoints = []
        self.snakeBody = [Body(convert(15 - i), convert(2), convert(1), convert(0)) for i in range(2)]
    def changeDirection(self, i, direction):
        if direction == 'D':
            self.snakeBody[i].vx = convert(0)
            self.snakeBody[i].vy = convert(1)
        elif direction == 'R':
            self.snakeBody[i].vx = convert(1)
            self.snakeBody[i].vy = convert(0)
        elif direction == 'U':
            self.snakeBody[i].vx = convert(0)
            self.snakeBody[i].vy = convert(-1)
        elif direction == 'L':
            self.snakeBody[i].vx = convert(-1)
            self.snakeBody[i].vy = convert(0)
        if i == len(self.snakeBody) - 1:
            del(self.turningPoints[0])
    def draw(self):
        global WIN
        for part in self.snakeBody:
            pygame.draw.rect(WIN, RED, rect(part.x, part.y))
            
    def erase(self):
        global WIN
        for part in self.snakeBody:
            pygame.draw.rect(WIN, BLACK, rect(part.x, part.y))
    def update_pos(self):
        global DISPLAY_WIDTH
        global CRASHED
        for i, c in enumerate(self.snakeBody):
            for tp in self.turningPoints:
                if c.x == tp['x'] and c.y == tp['y']:
                    self.changeDirection(i, tp['direction'])
            c.x += c.vx
            c.y += c.vy
            if c.x == convert(20):
                c.x = 0
            elif c.x == convert(-1):
                c.x = convert(19)
            elif c.y == convert(-1):
                c.y = convert(19)
            elif c.y == convert(20):
                c.y = convert(0)
            if i > 0 and c.x == self.snakeBody[0].x and c.y == self.snakeBody[0].y:

                CRASHED = True

     
