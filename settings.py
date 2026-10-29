# Screen
WIDTH, HEIGHT = 480, 640
FPS = 60
BG_COLOUR = (15, 15, 30)

# Player
PLAYER_SPEED = 300  # pixels per second
PLAYER_COLOUR = (80, 200, 255)

# Asteroids
ASTEROID_SPEED = 200        # pixels per second, falling down
ASTEROID_SPAWN_TIME = 0.8   # seconds between new asteroids
ASTEROID_COLOUR = (160, 160, 160)
ASTEROID_MIN_SIZE = 20
ASTEROID_MAX_SIZE = 50

# Text
TEXT_COLOUR = (255, 255, 255)

# Score and difficulty
SCORE_PER_SECOND = 10
SPEED_INCREASE = 5          # extra pixels per second, for each second survived
SPAWN_TIME_DECREASE = 0.01  # seconds less between asteroids, for each second survived
SPAWN_TIME_MIN = 0.25       # never spawn faster than this
