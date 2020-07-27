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
    RADIUS = 10
 
    def draw(self, body):
        global win
        for part in body:
            pygame.draw.circle(win, (255, 0, 0), part, self.RADIUS)


snake = Snake()
snakeBody = [(display_width//2-2*Snake.RADIUS*i, display_height//2) for i in range(0, 7)]
snake.draw(body)
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    pygame.display.update()
pygame.quit()
