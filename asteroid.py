import pygame
import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        new_asteroid1_angle = self.velocity.rotate(random_angle)
        new_asteroid2_angle = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid1.velocity = new_asteroid1_angle * 1.2
        asteroid2 = Asteroid(self.position[0], self.position[1], new_radius)
        asteroid2.velocity = new_asteroid2_angle * 1.2

    def update(self, dt):
        self.position += (self.velocity * dt)

    