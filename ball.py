import pygame
import random
from utils import *

class Ball:
    def __init__(self, surface, left, top, size, colour):
        self.colour = colour
        self.surface = surface
        self.velocity = 10
        self.angle = random.randint(1, 360)
        self.rect = pygame.rect.Rect(left, top, size, size)
    
    def move(self):
        # calculate a movement vector from the angle
        movement = Utils.angle_to_pixels(self.angle, self.velocity)
        self.rect.move_ip(movement[0], movement[1])

    def is_out_of_bounds(self):
        return self.rect.left <= 0 or self.rect.top <= 0 or (self.rect.left + self.rect.width >= self.surface.get_width()) or (self.rect.top + self.rect.height >= self.surface.get_height())
    
    def collides_with(self, paddle):
        return self.rect.colliderect(paddle.rect)
            
    def rebound(self):
        # todo: get this right
        self.angle = self.angle * 3.14
        while (self.angle > 360):
            self.angle = abs(360 - self.angle)

    def draw(self):
        pygame.draw.circle(self.surface, self.colour, self.rect.center, self.rect.width / 2)