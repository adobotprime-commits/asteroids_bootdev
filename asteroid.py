import pygame
import random
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen) -> None:
        pygame.draw.circle(
            screen,
            "white",
            self.position,
            self.radius,
            LINE_WIDTH
        )

    def update(self, dt) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
           log_event("asteroid_split")
           split_angle = random.uniform(20, 50)
           vector1 = self.velocity.rotate(split_angle)
           vector2 = self.velocity.rotate(-split_angle)
           smaller1 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
           smaller2 = Asteroid(self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS)
           smaller1.velocity = vector1 * 1.2
           smaller2.velocity = vector2 * 1.2
