from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random, math

class Asteroid(CircleShape):
    
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.score_value = 0

    def draw(self, screen):
        return pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            pass
        else:
            log_event("asteroid_split")
            # new angle for the smaller asteroid 
            random_angle = random.uniform(20.00, 50.00)
            random_speed_A = random.uniform(0.9, 1.5)
            random_speed_B = random.uniform(0.9, 1.5)
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
            asteroid_A.velocity *= random_speed_A
            asteroid_B.velocity *= random_speed_B

        return self.score_value
            

    
    def update(self, dt):
        self.position += (self.velocity * dt)
        self.score_value = math.ceil(self.velocity.magnitude() * (100/ self.radius))