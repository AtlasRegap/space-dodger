import pygame
from settings import WIDTH, HEIGHT, PLAYER_SPEED, PLAYER_COLOUR


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, PLAYER_COLOUR, [(20, 0), (40, 40), (0, 40)])
        self.rect = self.image.get_rect(midbottom=(WIDTH // 2, HEIGHT - 20))
        # Exact horizontal position, kept as a float
        self.x = float(self.rect.x)
        self.mask = pygame.mask.from_surface(self.image)






    def update(self, dt):
        keys = pygame.key.get_pressed()
        direction = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            direction -= 1
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            direction += 1

        self.x += direction * PLAYER_SPEED * dt

        # Keep the ship on screen
        if self.x < 0:
            self.x = 0
        if self.x > WIDTH - self.rect.width:
            self.x = WIDTH - self.rect.width

        self.rect.x = round(self.x)

    def draw(self, surface):
        surface.blit(self.image, self.rect)



