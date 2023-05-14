import pygame

class Ball:
    def __init__(self, surface, left, top, size, colour):
        self.left = left
        self.top = top
        self.size = size
        self.colour = colour
        self.surface = surface
        self.velocity = 10
    
    def draw(self):
        pygame.draw.circle(self.surface, self.colour, (self.left, self.top), self.size)