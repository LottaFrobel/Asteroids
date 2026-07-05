import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
from shot import Shot

class Asteroid(CircleShape):

    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position = self.position + (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            angle = random.uniform(20, 50)
            new_velocity = self.velocity.rotate(angle)
            new_velocity_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            bb_1 = Asteroid(self.position.x, self.position.y, new_radius)
            bb_1.velocity = new_velocity * 1.2
            bb_2 = Asteroid(self.position.x, self.position.y, new_radius)
            bb_2.velocity = new_velocity_2 * 1.2


