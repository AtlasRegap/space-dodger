import sys
import pygame
from settings import WIDTH, HEIGHT, FPS, BG_COLOUR
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Dodger")
    clock = pygame.time.Clock()

    player = Player()

    running = True
    while running:
        dt = clock.tick(FPS) / 1000  # seconds since last frame

        # 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update
        player.update(dt)

        # 3. Draw
        screen.fill(BG_COLOUR)
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
