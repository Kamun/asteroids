import pygame
from constants import *

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        self.x = x
        self.y = y
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collision(self, CircleShape):
        r1 = self.radius
        r2 = CircleShape.radius
        distance = self.position.distance_to(CircleShape.position)
        return distance <= r1+r2

class Shot(CircleShape):
    def __init__(self, x, y, shots, radius=SHOT_RADIUS):
        super().__init__(x, y, radius)
        self.shots = shots
        self.velocity = pygame.Vector2(0, 0)  # Initialize velocity
    
    def draw(self, screen):
        # Draw a small white circle
        pygame.draw.circle(screen, (255, 255, 255), (int(self.position.x), int(self.position.y)), self.radius)
    
    def update(self, dt):
        # Update position based on velocity
        self.position += self.velocity * dt