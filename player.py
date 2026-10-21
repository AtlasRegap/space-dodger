import pygame
from settings import WIDTH, HEIGHT, PLAYER_SPEED, PLAYER_COLOUR


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Draw the ship once, onto its own small surface
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, PLAYER_COLOUR, [(20, 0), (40, 40), (0, 40)])
        # The rect stores where the ship is on the screen
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += PLAYER_SPEED

    def draw(self, surface):
        surface.blit(self.image, self.rect)
