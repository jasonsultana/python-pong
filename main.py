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

win_sound = pygame.mixer.Sound("assets/win.wav")
lose_sound = pygame.mixer.Sound("assets/lose.wav")

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

        elif event.type == pygame.QUIT:
            running = False

    if not paused:
        # game logic
        if (cpu.is_at_edge()):
            if (cpu.direction == Direction.LEFT):
                cpu.set_direction(Direction.RIGHT)
            else:
                cpu.set_direction(Direction.LEFT)

        # if the ball is about to go off screen, play the win or lose sound and just rebound
        collision_type = ball.get_collision_type_screen()
        if (collision_type == CollisionType.LEFT):
            win_sound.play()
        elif (collision_type == CollisionType.RIGHT):
            lose_sound.play()

        ball.rebound(collision_type)

        # if the ball is at any paddle, inverse the angle.
        collision_type = ball.get_collision_type(player.rect)
        ball.rebound(collision_type)

        collision_type = ball.get_collision_type(cpu.rect)
        ball.rebound(collision_type)

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