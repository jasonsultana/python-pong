import pygame
from paddle import *
 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
 
# initialize pygame
pygame.init()
screen_size = (700, 500)
 
# create a window
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pong")
 
player = Paddle(screen, 50, 100, WHITE)

# clock is used to set a max fps
clock = pygame.time.Clock()

running = True
paused = False
while running:
    print("loop")

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("left key pressed")
                player.set_direction(Direction.LEFT)

            elif event.key == pygame.K_RIGHT:
                print("right key pressed")
                player.set_direction(Direction.RIGHT)

            # cheat codes
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    pygame.mixer.music.pause()
                    continue
                else:
                    pygame.mixer.music.play(-1)
        elif event.type == pygame.QUIT:
            running = False

    if not paused:
        print("game running")

        # game logic
        player.move()

        # drawing logic
        screen.fill(BLACK)
        player.draw()
        pygame.display.flip()

        # how many updates per second
        clock.tick(10)

pygame.quit()