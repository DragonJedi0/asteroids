import pygame
from constants import *
from circleshape import CircleShape
from bullet import Shot

class Player(CircleShape):
    def __init__(self, pos_x, pos_y, shot_group):
        super().__init__(pos_x, pos_y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_group = shot_group
        self.__rate_limit = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def update(self, dt):
        self.__rate_limit -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            if self.__rate_limit <= 0:
                self.shoot(self.shot_group)
            self.__rate_limit = PLAYER_SHOOT_COOLDOWN

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self, shots):
        forward = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        bullet = Shot(self.position, forward)
        shots.add(bullet)