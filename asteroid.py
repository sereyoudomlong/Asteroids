from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            # new angle for the smaller asteroid 
            random_angle = random.uniform(20.00, 50.00)
            # get the new velocity for them
            new_vectorA = self.velocity.rotate(random_angle)
            new_vectorB = self.velocity.rotate(-random_angle)
            # new radius for the split
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            # new asteroid
            asteroid_A = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid_B = Asteroid(self.position.x, self.position.y, new_radius)
            # change its velocity
            asteroid_A.velocity = new_vectorA
            asteroid_B.velocity = new_vectorB
            # speed up cause smaller
            asteroid_A.velocity *= 1.2
            asteroid_B.velocity *= 1.2
            

    
    def update(self, dt):
        self.position += (self.velocity * dt)