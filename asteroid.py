import random
import pygame
from settings import (WIDTH, HEIGHT, ASTEROID_COLOUR,
                      ASTEROID_MIN_SIZE, ASTEROID_MAX_SIZE)


class Asteroid(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        self.speed = speed

        # Pick a random size
        size = random.randint(ASTEROID_MIN_SIZE, ASTEROID_MAX_SIZE)

        # Draw a circle on a transparent square
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        radius = size // 2
        pygame.draw.circle(self.image, ASTEROID_COLOUR, (radius, radius), radius)

        # Pick a random x, and start just above the top of the screen
        x = random.randint(0, WIDTH - size)
        self.rect = self.image.get_rect(topleft=(x, -size))

        # Exact vertical position, kept as a float
        self.y = float(self.rect.y)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, dt):
        self.y += self.speed * dt
        self.rect.y = round(self.y)

        # Off the bottom of the screen? Remove it.
        if self.rect.top > HEIGHT:
            self.kill()
