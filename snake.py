import pygame 
pygame.init
display_width = 800
display_height = 600
win = pygame.display.set_mode((display_width, display_height))
crashed = False
color = {
    'red':(255, 0, 0),
    'green': (0, 255, 0), 
    'blue' : (0, 0, 255), 
 }
class Snake:
    def __init__(self):
        self.RADIUS = 10
        self.snakeBody = [ {'x':display_width//2-2*self.RADIUS*i ,'y': display_height//2, 'vx': 2*self.RADIUS, 'vy':0} for i in range(0, 7)]
    def draw(self):
        global win
        for part in self.snakeBody:           
            pygame.draw.circle(win, (255, 0, 0), (part['x'], part['y']), self.RADIUS)
    def erase(self):
        global win
        for part in self.snakeBody:
            pygame.draw.circle(win, (0, 0, 0), (part['x'], part['y']), self.RADIUS)
 

clock = pygame.time.Clock()
snake = Snake()

snake.draw()
i = 0
while not crashed:
    clock.tick(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    snake.erase()
    keys = pygame.key.get_pressed()
    if keys['K_DOWN']:
        i = len(snake.snakeBody)
    for part in snake.snakeBody:
        part['x'] = part['x'] + part['vx']
        part['y'] = part['y'] + part['vy']
    snake.draw()
    pygame.display.update()
pygame.quit()
