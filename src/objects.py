import pygame
import os
import configurations


# Get the absolute path of the assets directory
# assets_dir = os.path.join(os.getcwd(), "src/assets")
assets_dir = "assets"

# Load the images
STADIUM = pygame.image.load(os.path.join(assets_dir, "stadium.jpg"))
LEFT_GOAL = pygame.image.load(os.path.join(assets_dir, "left_goal_e.png"))
RIGHT_GOAL = pygame.image.load(os.path.join(assets_dir, "right_goal_e.png"))

LEFT_EDGE = pygame.image.load(os.path.join(assets_dir, "left_edge.png"))
RIGHT_EDGE = pygame.image.load(os.path.join(assets_dir, "right_edge.png"))


BALL = pygame.image.load(os.path.join(assets_dir, "ball.png"))
BALL = pygame.transform.scale(BALL, configurations.BALL_SCALE)



