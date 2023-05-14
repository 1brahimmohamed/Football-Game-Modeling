import pygame
import os
import configurations

STADIUM = pygame.image.load(os.path.join("assets", "stadium.jpg"))
LEFT_GOAL = pygame.image.load(os.path.join("assets", "left_goal_e.png"))
RIGHT_GOAL = pygame.image.load(os.path.join("assets", "right_goal_e.png"))

LEFT_EDGE = pygame.image.load(os.path.join("assets", "left_edge.png"))
RIGHT_EDGE = pygame.image.load(os.path.join("assets", "right_edge.png"))


BALL = pygame.image.load(os.path.join("assets", "ball.png"))
BALL = pygame.transform.scale(BALL, configurations.BALL_SCALE)

