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
        global display_height
        global display_width
        self.RADIUS = 10
        self.snakeBody = [ {'x':display_width//2-2*self.RADIUS*i ,'y': display_height//2, 'vel': 0} for i in range(0, 7)]
    def draw(self):
        global win
        for part in self.snakeBody:
            pygame.draw.circle(win, (255, 0, 0), (part['x'], part['y']), self.RADIUS)
    def erase(self):
        global win
        for part in self.snakeBody:
            pygame.draw.circle(win, (0, 0, 0), (part['x'], part['y']), self.RADIUS)
    def update_pos(self, vel):
        for part in self.snakeBody:
            part['vel'] = vel
            part['x'] = part['x'] + part['vel']


snake = Snake()

snake.draw()

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    snake.erase()
    snake.update_pos(1)
    snake.draw()
    pygame.display.update()
pygame.quit()
