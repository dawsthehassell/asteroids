import pygame
import random
from pygame.math import Vector2
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers = []
    def __init__(self, x, y, radius, velocity=None):
        super().__init__(x, y, radius)
        self.velocity = velocity or pygame.Vector2(0, 0)
        self.rect = pygame.Rect(x - radius, y - radius,
                              radius * 2, radius * 2)
        for container in self.__class__.containers:
            container.add(self)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=2)

    def update(self, dt):
        self.position = self.position + (self.velocity * dt)
        self.rect.center = self.position

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20.0, 50.0)
            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)
            new_asteroid_radius = self.radius - (ASTEROID_MIN_RADIUS)
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_radius, Vector2(new_velocity1 * 1.2))
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_radius, Vector2(new_velocity2 * 1.2))
            for group in self.groups():
                group.add(new_asteroid1, new_asteroid2)