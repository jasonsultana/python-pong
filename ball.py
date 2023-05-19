import pygame
import random
import math
from collision_type import CollisionType
from utils import *

class Ball:
    def __init__(self, surface, left, top, size, colour):
        self.colour = colour
        self.surface = surface
        self.rect = pygame.rect.Rect(left, top, size, size)
        self.velocityX = 10
        self.velocityY = 10

    def reangle(self):
        # todo: Let's get rid of angle. Introduce velocityX, velocityY. On a horizontal collision, invert velocityX. On a vertical collision, invert velocityY.
        self.angle = random.randint(1, 360)

    def move(self):
        # calculate a movement vector from the angle
        self.rect.move_ip(self.velocityX, self.velocityY)

    def get_collision_type_screen(self):
        if (self.rect.left <= 0):
            return CollisionType.LEFT
        elif (self.rect.top <= 0):
            return CollisionType.UP
        elif (self.rect.left + self.rect.width >= self.surface.get_width()):
            return CollisionType.RIGHT
        elif (self.rect.top + self.rect.height >= self.surface.get_height()):
            return CollisionType.DOWN
        else:
            return CollisionType.NONE
        
    def get_collision_type(self, object):
        if not self.rect.colliderect(object):
            return CollisionType.NONE
        
        # since the paddles are only on the left and right sides, there can only be a left or right collision
        if (self.rect.left >= object.left and self.rect.left <= object.left + object.width):
            return CollisionType.LEFT
        elif (self.rect.left <= object.left and self.rect.left + self.rect.width >= object.left):
            return CollisionType.RIGHT
            
    def rebound(self, collision_type):
        if (collision_type == CollisionType.LEFT):
            self.velocityX = abs(self.velocityX)
        elif (collision_type == CollisionType.RIGHT):
            self.velocityX = 0 - self.velocityX
        elif (collision_type == CollisionType.UP):
            self.velocityY = abs(self.velocityY)
        elif (collision_type == CollisionType.DOWN):
            self.velocityY = 0 - self.velocityY

    def draw(self):
        pygame.draw.circle(self.surface, self.colour, self.rect.center, self.rect.width / 2)