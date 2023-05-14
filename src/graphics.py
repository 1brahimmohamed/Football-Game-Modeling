import pygame
import colors
import configurations
import objects


def draw_screen(WIN, ball):
    WIN.blit(objects.STADIUM, configurations.STADIUM_POSITION)

    WIN.blit(objects.LEFT_EDGE, configurations.LEFT_EDGE_POSITION)
    WIN.blit(objects.RIGHT_EDGE, configurations.RIGHT_EDGE_POSITION)

    WIN.blit(objects.BALL, (ball.x, ball.y))

    WIN.blit(objects.LEFT_GOAL, configurations.LEFT_GOAL_POSITION)
    WIN.blit(objects.RIGHT_GOAL, configurations.RIGHT_GOAL_POSITION)

    pygame.display.update()


def ball_movement_handler(keys_pressed, ball):
    if keys_pressed[pygame.K_LEFT] and ball.x - configurations.BALL_VELOCITY > 0:
        ball.x -= configurations.BALL_VELOCITY
    if keys_pressed[pygame.K_RIGHT] and ball.x + configurations.BALL_VELOCITY < configurations.GAME_WIDTH - 30:
        ball.x += configurations.BALL_VELOCITY
    if keys_pressed[pygame.K_UP] and ball.y - configurations.BALL_VELOCITY > 0:
        ball.y -= configurations.BALL_VELOCITY
    if keys_pressed[pygame.K_DOWN] and ball.y + configurations.BALL_VELOCITY < configurations.GAME_HEIGHT - 240:
        ball.y += configurations.BALL_VELOCITY
