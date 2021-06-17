from snake import Snake
from food import Food
from body import Body
from helper import *
import numpy as np
import pygame
pygame.init

def main():
    global CRASHED
    global AVAILABLE
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
            snake.snakeBody.append(Body(x-vx, y-vy, vx, vy))

            
            for i in range(20):
                for j in range(20):
                    if (i, j) not in [(i_convert(snake.snakeBody[k].x), i_convert(snake.snakeBody[k].y)) for k in range(len(snake.snakeBody))]:
                        AVAILABLE.append((convert(i), convert(j)))
            idx = np.random.randint(len(AVAILABLE) - 1)

            food.x , food.y = AVAILABLE[idx]
            food.eaten = False
            food.draw()
            AVAILABLE = []


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

if __name__ == "__main__":
    main()