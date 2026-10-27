import sys
import pygame
from settings import WIDTH, HEIGHT, FPS, BG_COLOUR, ASTEROID_SPAWN_TIME  # CHANGED
from player import Player
from asteroid import Asteroid                                      # NEW


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Dodger")
    clock = pygame.time.Clock()

    player = Player()
    asteroids = pygame.sprite.Group()                              # NEW
    spawn_timer = 0                                                # NEW

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # seconds since last frame

        # 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update
        player.update(dt)

        spawn_timer += dt                                          # NEW
        if spawn_timer >= ASTEROID_SPAWN_TIME:                     # NEW
            spawn_timer -= ASTEROID_SPAWN_TIME                     # NEW
            asteroids.add(Asteroid())                              # NEW

        asteroids.update(dt)                                       # NEW

        # 3. Draw
        screen.fill(BG_COLOUR)
        asteroids.draw(screen)                                     # NEW
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
