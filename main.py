import pygame
import os
import numpy as np
import json

pygame.font.init() 
myfont = pygame.font.SysFont('Comic Sans MS', 50)


GRIDWIDTH:int = 10

convert = lambda x: int(x*GRIDWIDTH) # convert coordinate into grid location
i_convert = lambda x: int(x/GRIDWIDTH) # inverse of convert function

SCORE_WIDTH_PX:int = 10
DISPLAY_WIDTH_PX:int = 60
DISPLAY_HEIGHT_PX:int = 50

RED:tuple = (255, 0, 0)
GREEN:tuple = (0, 255, 0)
BLUE:tuple = (0, 0, 255)
BLACK:tuple = (0, 0, 0)
WHITE:tuple = (255, 255, 255)
YELLOW:tuple = (255, 255, 153)


SCORE_WIDTH:int = convert(SCORE_WIDTH_PX) 
DISPLAY_WIDTH:int = convert(DISPLAY_WIDTH_PX)
DISPLAY_HEIGHT:int = convert(DISPLAY_HEIGHT_PX)

WIN:any = pygame.display.set_mode((DISPLAY_WIDTH + SCORE_WIDTH, DISPLAY_HEIGHT))


vel_to_str = lambda x, y : f'{i_convert(x)}, {i_convert(y)}'

INIT_SNAKE_HEAD_COORDINATE:list = [15, 2]
INIT_SNAKE_HEAD_VELOCITY:list = [1, 0]
INIT_SNAKE_LENGTH:int = 8 
CRASHED:bool = False


rect = lambda x, y, i = 1, j = 1: pygame.Rect(x, y, convert(i), convert(j))

AVAILABLE:list = []
clock = pygame.time.Clock()

def _add_data(head_pos, food_pos, current_direction, length, next_direction, status):
    DATA_FILE:str = os.path.abspath('./snake.dat.json')
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        data["headPos"].append(head_pos)
        data["foodPos"].append(food_pos)
        data["length"].append(length)
        data["current-direction"].append(current_direction)
        data["next-direction"].append(next_direction)
        data["status"].append(status)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent = 2)

class Body:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

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

class Score_Board(object):
    def __init__(self):
        self.value = 0
        self.x = DISPLAY_WIDTH
        self.y = 0
        self.WIDTH = SCORE_WIDTH_PX
        self.HEIGHT = DISPLAY_HEIGHT_PX
        print(self.x, self.y)
    def get_score(self):
        return myfont.render(f'{self.value}', False, BLACK)                   
    def update(self):
        self.value += 1
    def draw(self):
        global WIN
        global textsurface
        pygame.draw.rect(WIN, WHITE, rect(self.x, self.y, self.WIDTH, self.HEIGHT))
        WIN.blit(self.get_score(),(DISPLAY_WIDTH + SCORE_WIDTH//8, DISPLAY_HEIGHT//2))
    def __str__(self):
        return f"score = {self.value}"
      
def main():
    global INIT_SNAKE_HEAD_COORDINATE
    global INIT_SNAKE_HEAD_VELOCITY
    global INIT_SNAKE_LENGTH
    global BLUE
    global RED
    global GREEN
    global SCORE_WIDTH
    global DISPLAY_HEIGHT
  
    global CRASHED
    global AVAILABLE

    snake = Snake(INIT_SNAKE_HEAD_COORDINATE[0], INIT_SNAKE_HEAD_COORDINATE[1], INIT_SNAKE_HEAD_VELOCITY[0], INIT_SNAKE_HEAD_VELOCITY[1], INIT_SNAKE_LENGTH)
    food = Food(convert(16), convert(17), 0, 0, GREEN, False)
    board = Score_Board()
    board.draw()
    food.draw()
    i:int = INIT_SNAKE_LENGTH - 1
    while not CRASHED:
        clock.tick(15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                CRASHED = True
        snake.erase()
        food.is_eaten(snake.snakeBody[0])
        if food.eaten == True:
            snake.append_body() 
            board.update()
            
            for i in range(i_convert(DISPLAY_WIDTH)):
                for j in range(i_convert(DISPLAY_HEIGHT)):
                    if (i, j) not in [(i_convert(snake.snakeBody[k].x), i_convert(snake.snakeBody[k].y)) for k in range(snake.get_len())]:
                        AVAILABLE.append([i, j])

            idx = np.random.randint(len(AVAILABLE) - 1)

            food.x , food.y = list(map(convert, AVAILABLE[idx]))
            food.eaten = False
            food.draw()
            AVAILABLE.clear()


        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN] and snake.snakeBody[0].vy == 0:
            snake.turningPoints.append({'x':snake.snakeBody[0].x, 'y': snake.snakeBody[0].y, 'direction':'D'})

        elif keys[pygame.K_LEFT] and snake.snakeBody[0].vx == 0:
            snake.turningPoints.append({'x':snake.snakeBody[0].x, 'y': snake.snakeBody[0].y, 'direction':'L'})

        elif keys[pygame.K_UP] and snake.snakeBody[0].vy == 0:
            snake.turningPoints.append({'x':snake.snakeBody[0].x, 'y': snake.snakeBody[0].y, 'direction':'U'})
        elif keys[pygame.K_RIGHT] and snake.snakeBody[0].vx == 0:
            snake.turningPoints.append({'x':snake.snakeBody[0].x, 'y': snake.snakeBody[0].y, 'direction':'R'})

        snake.update_pos()
        snake.draw()
        board.draw()
        print(board)
        pygame.display.update()
        #_add_data(head_pos = [snake.snakeBody[0].x, snake.snakeBody[0].y], food_pos = [food.x, food.y], current_direction = Snake.get_direction(vel_to_str(snake.snakeBody[1].vx, snake.snakeBody[1].vy)), length = snake.get_len(), next_direction = Snake.get_direction(vel_to_str(snake.snakeBody[0].vx, snake.snakeBody[0].vy)), status = CRASHED)
    pygame.quit()
    print('well played')

if __name__ == "__main__":
    main()
