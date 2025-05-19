import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, spawn_point, spawn_velocity):
        super().__init__(spawn_point.x, spawn_point.y, SHOT_RADIUS)
        self.velocity = spawn_velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
