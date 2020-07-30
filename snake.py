import pygame 
pygame.init
display_width = 500
display_height = 500
win = pygame.display.set_mode((display_width, display_height))
crashed = False
gridWidth = 25 
convert = lambda j: j*gridWidth
debugfile = open('debug.txt', 'w')
rect = lambda x, y: pygame.Rect(x, y, gridWidth, gridWidth)
class Snake:
    def __init__(self):
        self.snakeBody = [{'x':convert(5 - i),'y':convert(2), 'vx':convert(1), 'vy':convert(0)} for i in range(4)]
    def draw(self):
        global win
        for part in self.snakeBody:           
            pygame.draw.rect(win, (0, 244, 0), rect(part['x'], part['y']))
    def erase(self):
        global win
        for part in self.snakeBody:
            pygame.draw.rect(win, (0, 0, 0), rect(part['x'], part['y']))
    def update_pos(self):
        dl = []
        for part in self.snakeBody:
            part['x'] += part['vx']
            part['y'] += part['vy']
            dl.append(f'{part["x"]/gridWidth}, {part["y"]/gridWidth}')
        print(dl, file = debugfile)
	

i = -1
clock = pygame.time.Clock()
snake = Snake()
snake.draw()
turning = False
while not crashed:
    clock.tick(10)
    # for i in range(1, display_height):
	#     pygame.draw.line(win, (225, 225, 225), (convert(i), 0), (convert(i), display_height))
	#     pygame.draw.line(win, (225, 225, 225), (0, convert(i)), (display_height, convert(i)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    snake.erase()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and not turning:
        print('turning starts', file = debugfile)
        turning = True
        i = len(snake.snakeBody) - 1

    if turning:
        print(f'turning {i}', file = debugfile)
        if i >=0:
            snake.snakeBody[len(snake.snakeBody) - 1 - i]['vx'] = convert(0)
            snake.snakeBody[len(snake.snakeBody) - 1 - i]['vy'] = convert(1)
            i -= 1
        else:
            turning = False
    
    snake.update_pos()
    snake.draw()
    pygame.display.update()
pygame.quit()
