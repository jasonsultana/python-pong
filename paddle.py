import pygame
from direction import *

class Paddle:
    def __init__(self, surface, left, width, height, colour):
        self.rect = pygame.rect.Rect(left, 20, width, height)
        self.colour = colour
        self.surface = surface
        self.direction = Direction.LEFT
        self.velocity = 10

    def set_direction(self, direction):
        self.direction = direction

    def move(self):
        if (self.direction == Direction.LEFT):
            new_y = self.rect.y + self.velocity
            if (new_y + self.rect.height >= self.surface.get_height()):
                self.rect.top = self.surface.get_height() - self.rect.height # move flush to the bottom of the screen
            else:
                self.rect.move_ip((0, self.velocity))
        else:
            new_y = self.rect.y - self.velocity
            if (new_y <= 0):
                self.rect.top = 0 # move flush to the top of the screen
            else:
                self.rect.move_ip((0, -self.velocity))

    def is_at_edge(self):
        return self.rect.top == self.surface.get_height() - self.rect.height or self.rect.top == 0

    def draw(self):
        pygame.draw.rect(self.surface, self.colour, self.rect)