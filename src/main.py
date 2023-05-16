import subprocess
import sys
import os
import colors
import configurations
import graphics

# Check if pygame is installed
try:
    print("[GAME] Trying to import pygame")
    import pygame

    print("[GAME] Pygame imported")
except:
    print("[EXCEPTION] Pygame not installed")

WIN = pygame.display.set_mode((configurations.GAME_WIDTH, configurations.GAME_HEIGHT))
pygame.display.set_caption(configurations.GAME_TITLE)


def main():

    ball = pygame.Rect(configurations.BALL_POSITION, configurations.BALL_SCALE)

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(configurations.GAME_FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        graphics.ball_movement_handler(keys_pressed, ball)
        graphics.draw_screen(WIN, ball)

    pygame.quit()


if __name__ == "__main__":
    main()