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
pygame.draw.circle(win, color['red'], (display_width//2, display_height//2), 10)
pygame.draw.circle(win, color['red'], (display_width//2 - 20, display_height//2), 10)
pygame.draw.circle(win, color['red'], (display_width//2 - 20-20, display_height//2), 10)
pygame.draw.circle(win, color['red'], (display_width//2 - 20-20-20, display_height//2), 10)

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
    pygame.display.update()
pygame.quit()
