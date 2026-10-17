import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SHOOT_SPEED
from constants import LINE_WIDTH
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED

from shot import Shot

class Player (CircleShape):

    def __init__(self, x: float, y: float):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH) # Tell pygame to draw the triangle | color/points/line_width

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        dir = pygame.Vector2(0,1)
        dir = dir.rotate(self.rotation)
        move_in_dir = dir * PLAYER_SPEED * dt
        self.position += move_in_dir


    def update(self, dt: float) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()


    # Get points of the player ship triangle
    def triangle(self) -> list[pygame.Vector2]:
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    # Shots fired
    def shoot(self) -> None:
        bullet = Shot(self.position.x, self.position.y)
        bullet.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        pass
