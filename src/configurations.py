import pygame
pygame.init()
import colors

# Get the size of the screen
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

# -------------   Game dimensions ------------- #
GAME_HEIGHT = int(screen_height*0.9 )
GAME_WIDTH = GAME_HEIGHT * 2

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
BALL_POSITION = (GAME_WIDTH / 2 - 10, GAME_HEIGHT / 2 - 10)
BALL_SCALE = (ball_scale, ball_scale)

STADIUM_POSITION = (0, 0)

LEFT_GOAL_POSITION = (0, 233)
RIGHT_GOAL_POSITION = (1251, 256)

LEFT_EDGE_POSITION = (100, 257)
RIGHT_EDGE_POSITION = (1251, 256)




# Slider parameters
slider_width = 200
slider_height = 10
slider_color = colors.WHITE
handle_radius = 10
handle_color = colors.RED

# Position of the slider 
slider_position =  (GAME_WIDTH // 10 - slider_width // 2, GAME_HEIGHT - 30)


