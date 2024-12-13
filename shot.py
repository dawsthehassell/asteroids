import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS
from constants import PLAYER_SHOOT_SPEED

class Shot(CircleShape):
    containers= []
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.rect = pygame.Rect(x - SHOT_RADIUS, y - SHOT_RADIUS, 
                              SHOT_RADIUS * 2, SHOT_RADIUS * 2)
        for container in self.__class__.containers:
            container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
        self.rect.center = self.position