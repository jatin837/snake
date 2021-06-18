from .body import Body
from .helper import *

class Snake:
    DIRECTION = {
        '0, 1': "D",
        '1, 0': "R",
        '-1, 0': "L",
        '0, -1': "U",
    }
    def __init__(self, x, y, vx, vy, length):
        self.turningPoints = []
        self.snakeBody = [Body(convert(x - i), convert(y), convert(vx), convert(vy)) for i in range(length)]
    
    def get_len(self):
        return len(self.snakeBody)

    @staticmethod 
    def get_direction(direction):
        return Snake.DIRECTION[direction] 

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
        if i == self.get_len() - 1:
            del(self.turningPoints[0])
    def draw(self):
        global WIN
        for part in self.snakeBody:
            pygame.draw.rect(WIN, RED, rect(part.x, part.y))

    def append_body(self):
            temp_x = self.snakeBody[self.get_len() - 1].x
            temp_y = self.snakeBody[self.get_len() - 1].y
            temp_vx = self.snakeBody[self.get_len() - 1].vx
            temp_vy = self.snakeBody[self.get_len() - 1].vy
            self.snakeBody.append(Body(temp_x-temp_vx, temp_y-temp_vy, temp_vx, temp_vy))

            
    def erase(self):
        global WIN
        for part in self.snakeBody:
            pygame.draw.rect(WIN, BLACK, rect(part.x, part.y))

    def update_pos(self):
        global DISPLAY_WIDTH
        global DISPLAY_HEIGHT
        global CRASHED
        for indx, body in enumerate(self.snakeBody):
            for tp in self.turningPoints:
                if body.x == tp['x'] and body.y == tp['y']:
                    self.changeDirection(indx, tp['direction'])
            body.x += body.vx
            body.y += body.vy
            if body.x == convert(i_convert(DISPLAY_WIDTH)):
                body.x = 0
            elif body.x == convert(-1):
                body.x = convert(i_convert(DISPLAY_WIDTH) - 1)
            elif body.y == convert(-1):
                body.y = convert(i_convert(DISPLAY_HEIGHT) - 1)
            elif body.y == convert(i_convert(DISPLAY_HEIGHT)):
                body.y = convert(0)
            if indx > 0 and body.x == self.snakeBody[0].x and body.y == self.snakeBody[0].y:
                CRASHED = True

