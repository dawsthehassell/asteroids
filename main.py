import pygame
import sys
from player import Player
from constants import *
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from shot import Shot
  
def main():
    pygame.init
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}, Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    while True:
        dt = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            if player.collision(asteroid):
                print("Game over!")
                sys.exit()
        hits = pygame.sprite.groupcollide(shots, asteroids, True, False)
        if hits:
            for shot, hit_asteroids in hits.items():
                for asteroid in hit_asteroids:
                    asteroid.split()
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

if __name__== "__main__":
    main()