import sys
import pygame
from settings import (WIDTH, HEIGHT, FPS, BG_COLOUR, TEXT_COLOUR,      # CHANGED
                      ASTEROID_SPEED, ASTEROID_SPAWN_TIME,
                      SCORE_PER_SECOND, SPEED_INCREASE,
                      SPAWN_TIME_DECREASE, SPAWN_TIME_MIN)
from player import Player
from asteroid import Asteroid


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Dodger")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 64)
    small_font = pygame.font.Font(None, 36)                               # NEW

    player = Player()
    asteroids = pygame.sprite.Group()
    spawn_timer = 0
    elapsed = 0                                                           # NEW
    game_over = False

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # seconds since last frame

        # 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update (only while the game is still going)
        if not game_over:
            elapsed += dt                                                 # NEW

            # Difficulty for this moment in the game                     # NEW
            asteroid_speed = ASTEROID_SPEED + elapsed * SPEED_INCREASE    # NEW
            spawn_time = max(SPAWN_TIME_MIN,                              # NEW
                             ASTEROID_SPAWN_TIME - elapsed * SPAWN_TIME_DECREASE)

            player.update(dt)

            spawn_timer += dt
            if spawn_timer >= spawn_time:                                 # CHANGED
                spawn_timer -= spawn_time                                 # CHANGED
                asteroids.add(Asteroid(asteroid_speed))                   # CHANGED

            asteroids.update(dt)

            if pygame.sprite.spritecollide(
                player, asteroids, False, pygame.sprite.collide_mask
            ):
                game_over = True

        # 3. Draw
        screen.fill(BG_COLOUR)
        asteroids.draw(screen)
        player.draw(screen)

        score = int(elapsed * SCORE_PER_SECOND)                           # NEW
        score_text = small_font.render(f"Score: {score}", True, TEXT_COLOUR)  # NEW
        screen.blit(score_text, score_text.get_rect(topleft=(10, 10)))   # NEW

        if game_over:
            text = font.render("GAME OVER", True, TEXT_COLOUR)
            text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text, text_rect)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
