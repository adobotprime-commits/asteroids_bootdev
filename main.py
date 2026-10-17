import pygame
import sys

from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT

from logger import log_state
from logger import log_event

from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    fps_timer = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    ship = Player(x, y)
    field = AsteroidField()

    # Game Start
    while True:
        log_state()

        # Check for player inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update the game
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(ship):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Draw the game
        screen.fill("black")
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()

        # Track frame time
        dt = fps_timer.tick(60) / 1000


if __name__ == "__main__":
    main()
