import pygame

pygame.init()
import colors

# Get the size of the screen
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# -------------   Game dimensions ------------- #
GAME_HEIGHT = int(screen_height*0.7 )
GAME_WIDTH = GAME_HEIGHT * 1.85

print(GAME_WIDTH)
print(GAME_HEIGHT)

# -------------  Game FPS ------------- #
GAME_FPS = 60

# -------------   Game Ball Velocity ------------- #
BALL_VELOCITY = 10

# -------------   Game title ------------- #
GAME_TITLE = "Football Modeling Game"

# -------------   Game Positions & Scales ------------- #
ball_scale = 40
# BALL_POSITION = (GAME_WIDTH / 2 - 10, GAME_HEIGHT / 2 - 10)
BALL_POSITION = (125, GAME_HEIGHT - 240)
BALL_SCALE = (ball_scale, ball_scale)

STADIUM_POSITION = (0, 0)

LEFT_GOAL_POSITION = (0, 233)
RIGHT_GOAL_POSITION = (1251, 256)

LEFT_EDGE_POSITION = (100, 257)
RIGHT_EDGE_POSITION = (1251, 256)

# -------------   Game Physics ------------- #
GRAVITY = 9.8
ACCELERATION_MULTIPLIER = 1.5
BALL_UPDATE_VELOCITY = 1

BALL_ANGLE = 45
BALL_INITIAL_VELOCITY = 115

# -------------   Game Fonts ------------- #
fontsize = 20
font = pygame.font.SysFont("poppinssemibold", fontsize)

# ------------- Slider parameters ------------- #
slider_width = 200
slider_height = 12
slider_color = colors.WHITE
handle_radius = 12
handle_color = colors.DARK_GREEN
slider_label = "Initial Velocity"
slider_label_color = colors.WHITE
slider_value_color = colors.WHITE
slider_position = (GAME_WIDTH // 10 - slider_width // 2, GAME_HEIGHT - 80)
slider_label_position = (slider_position[0] + slider_width // 2 - fontsize * 1.5 - 50, slider_position[1] + slider_height + 10)
slider_value_position = (slider_position[0] + slider_width + 15, slider_position[1] - fontsize // 2)


