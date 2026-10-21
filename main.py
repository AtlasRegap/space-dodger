import sys
import pygame

# --- Settings ---
WIDTH, HEIGHT = 480, 640
FPS = 60
BG_COLOUR = (15, 15, 30)  # dark navy, as (red, green, blue), each 0-255


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Dodger")
    clock = pygame.time.Clock()

    running = True
    while running:
        # 1. Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 2. Update (nothing to update yet)

        # 3. Draw
        screen.fill(BG_COLOUR)
        pygame.display.flip()

        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
