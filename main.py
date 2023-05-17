import pygame
from paddle import *
from ball import *
 
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
 
player = Paddle(screen, screen.get_width() - 50, 50, 100, WHITE)
cpu = Paddle(screen, 0, 50, 100, WHITE)
ball = Ball(screen, screen.get_width() / 2 - 15, screen.get_height() / 2 - 15, 15, RED)

# clock is used to set a max fps
clock = pygame.time.Clock()

running = True
paused = False
while running:
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
        # game logic
        if (cpu.is_at_edge()):
            if (cpu.direction == Direction.LEFT):
                cpu.set_direction(Direction.RIGHT)
            else:
                cpu.set_direction(Direction.LEFT)

        # if ball is at any wall, inverse the angle. I may need to google the math for this.
        if (ball.is_out_of_bounds()):
            print(f"Ball out of bounds! Rebounding. Old angle: {ball.angle}")
            ball.rebound()
            print(f"New angle: {ball.angle}")

        # if the ball is at any paddle, inverse the angle.
        if (ball.collides_with(player)):
            print("Ball collided with player")
            ball.rebound()

        if (ball.collides_with(cpu)):
            print("Ball collided with cpu paddle")
            ball.rebound()

        player.move()
        cpu.move()
        ball.move()

        # drawing logic
        screen.fill(BLACK)
        player.draw()
        cpu.draw()
        ball.draw()
        pygame.display.flip()

        # how many updates per second
        clock.tick(10)

pygame.quit()