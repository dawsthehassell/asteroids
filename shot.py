import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        for container in self.__class__.containers:
            container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)