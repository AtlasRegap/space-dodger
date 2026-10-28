import sys
import pygame
from settings import (WIDTH, HEIGHT, FPS, BG_COLOUR,             # CHANGED
                      ASTEROID_SPAWN_TIME, TEXT_COLOUR)
from player import Player
from asteroid import Asteroid


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Dodger")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 64)                             # NEW

    player = Player()
    asteroids = pygame.sprite.Group()
    spawn_timer = 0
    game_over = False                                             # NEW

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # seconds since last frame

        # 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update (only while the game is still going)
        if not game_over:                                         # NEW
            player.update(dt)                                     # indented

            spawn_timer += dt                                     # indented
            if spawn_timer >= ASTEROID_SPAWN_TIME:                # indented
                spawn_timer -= ASTEROID_SPAWN_TIME
                asteroids.add(Asteroid())

            asteroids.update(dt)                                  # indented

            if pygame.sprite.spritecollide(                       # NEW
                player, asteroids, False, pygame.sprite.collide_mask
            ):
                game_over = True                                  # NEW

        # 3. Draw
        screen.fill(BG_COLOUR)
        asteroids.draw(screen)
        player.draw(screen)

        if game_over:                                             # NEW
            text = font.render("GAME OVER", True, TEXT_COLOUR)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
