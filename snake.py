import pygame 
pygame.init
display_width = 500
display_height = 500
win = pygame.display.set_mode((display_width, display_height))
crashed = False
gridWidth = 25 
convert = lambda j: j*gridWidth
rect = lambda x, y: pygame.Rect(x, y, gridWidth, gridWidth)
class Snake:
    def __init__(self):
        self.turningPoints = []
        self.snakeBody = [{'x':convert(5 - i),'y':convert(2), 'vx':convert(1), 'vy':convert(0)} for i in range(5)]
    def changeDirection(self, i, direction):
        if direction == 'D':
            self.snakeBody[i]['vx'] = convert(0)
            self.snakeBody[i]['vy'] = convert(1)
        elif direction == 'R':
            self.snakeBody[i]['vx'] = convert(1)
            self.snakeBody[i]['vy'] = convert(0)
        elif direction == 'U':
            self.snakeBody[i]['vx'] = convert(0)
            self.snakeBody[i]['vy'] = convert(-1)
        elif direction == 'L':
            self.snakeBody[i]['vx'] = convert(-1)
            self.snakeBody[i]['vy'] = convert(0)
        if i == len(self.snakeBody) - 1:
            del(self.turningPoints[0])
    def draw(self):
        global win
        for part in self.snakeBody:           
            pygame.draw.rect(win, (0, 244, 0), rect(part['x'], part['y']))
    def erase(self):
        global win
        for part in self.snakeBody:
            pygame.draw.rect(win, (0, 0, 0), rect(part['x'], part['y']))
    def update_pos(self):
        global display_width
        for i, c in enumerate(self.snakeBody):
            if c['x'] == convert(19):
                print('reset to x = 0')
                c['x'] = -25
            elif c['x'] == convert(-1):
                print('reset to x = max - 1')
                c['x'] = convert(20)
            elif c['y'] == convert(0):
                print('reset to y = max - 1')
                c['y'] = 500
            elif c['y'] == display_width/25:
                print('reset to y = 0')
                c['y'] = convert(0)
            for tp in self.turningPoints:
                if c['x'] == tp['x'] and c['y'] == tp['y']:
                    self.changeDirection(i, tp['direction'])
                
            c['x'] += c['vx']
            c['y'] += c['vy']
        print(f"{snake.snakeBody[0]['x']}, {snake.snakeBody[0]['y']}")
    # def reset(self, i, new_pos, d):
    #     if d == 'x':
    #         self.snakeBody[i]['x'] = new_pos
    #     elif d == 'y':
    #         self.snakeBody[i]['y'] = new_pos

clock = pygame.time.Clock()
snake = Snake()
snake.draw()


i = len(snake.snakeBody) - 1
while not crashed:
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    snake.erase()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN] and snake.snakeBody[0]['vy'] == 0:
        snake.turningPoints.append({'x':snake.snakeBody[0]['x'], 'y': snake.snakeBody[0]['y'], 'direction':'D'})
        
    elif keys[pygame.K_LEFT] and snake.snakeBody[0]['vx'] == 0:
        snake.turningPoints.append({'x':snake.snakeBody[0]['x'], 'y': snake.snakeBody[0]['y'], 'direction':'L'})

    elif keys[pygame.K_UP] and snake.snakeBody[0]['vy'] == 0:
        snake.turningPoints.append({'x':snake.snakeBody[0]['x'], 'y': snake.snakeBody[0]['y'], 'direction':'U'})
    elif keys[pygame.K_RIGHT] and snake.snakeBody[0]['vx'] == 0:
        snake.turningPoints.append({'x':snake.snakeBody[0]['x'], 'y': snake.snakeBody[0]['y'], 'direction':'R'})
    
    snake.update_pos()
    snake.draw()
    pygame.display.update()
pygame.quit()
