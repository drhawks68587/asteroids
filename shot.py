import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        # Add a rect that matches the circle's position
        self.rect = pygame.Rect(x - SHOT_RADIUS, y - SHOT_RADIUS, 
                              SHOT_RADIUS * 2, SHOT_RADIUS * 2)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)
    
    def update(self, dt):
        self.position += self.velocity * dt
        # Add this line to keep rect in sync with position
        self.rect.center = self.position