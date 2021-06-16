import pygame
import numpy as np

pygame.init

DISPLAY_WIDTH:int = 500
DISPLAY_HEIGHT:int = 500

WIN:any = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

CRASHED:bool = False
GRIDWIDTH:int = 25
convert = lambda j: j*GRIDWIDTH
rect = lambda x, y: pygame.Rect(x, y, GRIDWIDTH, GRIDWIDTH)

class Cube:
    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

class Snake:
    def __init__(self):
        self.turningPoints = []
        self.snakeBody = [Cube(convert(15 - i), convert(2), convert(1), convert(0)) for i in range(2)]
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
            pygame.draw.rect(WIN, (255, 0, 0), rect(part.x, part.y))
            
    def erase(self):
        global WIN
        for part in self.snakeBody:
            pygame.draw.rect(WIN, (0, 0, 0), rect(part.x, part.y))
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

class Food(Cube):
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
available = []
clock = pygame.time.Clock()
snake = Snake()
snake.draw()
food = Food(convert(16), convert(17), 0, 0, (0, 255, 0), False)
food.draw()
i = len(snake.snakeBody) - 1
while not CRASHED:
    clock.tick(15)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            CRASHED = True
    snake.erase()
    food.is_eaten(snake.snakeBody[0])
    if food.eaten == True:
        
        x = snake.snakeBody[len(snake.snakeBody) - 1].x
        y = snake.snakeBody[len(snake.snakeBody) - 1].y
        vx = snake.snakeBody[len(snake.snakeBody) - 1].vx
        vy = snake.snakeBody[len(snake.snakeBody) - 1].vy
        snake.snakeBody.append(Cube(x-vx, y-vy, vx, vy))

        
        for i in range(20):
            for j in range(20):
                if (i, j) not in [(snake.snakeBody[k].x/GRIDWIDTH, snake.snakeBody[k].y/GRIDWIDTH) for k in range(len(snake.snakeBody))]:
                    available.append((convert(i), convert(j)))
        idx = np.random.randint(len(available) - 1)

        food.x , food.y = available[idx]
        food.eaten = False
        food.draw()
        available = []


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
    print(f"points:{len(snake.snakeBody)-2}")
    pygame.display.update()
pygame.quit()
print('well played')
