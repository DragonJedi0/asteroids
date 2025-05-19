import pygame
from circleshape import *
from constants import *

class Player(CircleShape):
    def __init__(self, pos_x, pos_y):
        super().__init__(pos_x, pos_y, PLAYER_RADIUS)
        self.rotation = 0

    
    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        return pygame.draw.polygon(screen, "white", self.triangle(), 2)
    