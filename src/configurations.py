import pygame

pygame.init()
import colors

# Get the size of the screen
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# -------------   Game dimensions ------------- #
GAME_HEIGHT = int(screen_height*0.7)
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

# ------------- Slider Constants ------------- #
slider_width = 200
slider_height = 12
handle_radius = 12

slider_color = colors.WHITE
handle_color = colors.DARK_GREEN
slider_label_color = colors.WHITE
slider_value_color = colors.WHITE

# ------------- Slider Positions ------------- #
slider_position_angle =  (GAME_WIDTH // 10 - slider_width // 2 - 10, GAME_HEIGHT - 80)
slider_label_position_angle = (slider_position_angle[0] + slider_width // 2 - fontsize*1.5 - 10, slider_position_angle[1] + slider_height)
slider_value_position_angle = (slider_position_angle[0] + slider_width + 10, slider_position_angle[1] - fontsize // 2)

slider_position_distance = (GAME_WIDTH // 10 * 3 - 20, GAME_HEIGHT - 80)
slider_label_position_distance = (slider_position_distance[0] + slider_width // 2 - fontsize*1.5 - 20, slider_position_distance[1] + slider_height)
slider_value_position_distance = (slider_position_distance[0] + slider_width + 10, slider_position_distance[1] - fontsize // 2)

slider_position_velocity = (GAME_WIDTH // 10 * 6 - 60, GAME_HEIGHT - 80)
slider_label_position_velocity = (slider_position_velocity[0] + slider_width // 2 - 20  - fontsize*1.5 - 30, slider_position_velocity[1] + slider_height)
slider_value_position_velocity = (slider_position_velocity[0] + slider_width + 15, slider_position_velocity[1] - fontsize // 2)

# -------------   Slider Labels ------------- #
slider_label_angle = "Angle"
slider_label_distance = "Distance"
slider_label_velocity = "Inital Velocity"