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

    # Slider handle positions 
    handle_position_angle = configurations.slider_position_angle[0]
    handle_position_distance = configurations.slider_position_distance[0]
    handle_position_velocity = configurations.slider_position_velocity[0]

    pygame.init()
    WIN = pygame.display.set_mode((configurations.GAME_WIDTH, configurations.GAME_HEIGHT))
    pygame.display.set_caption(configurations.GAME_TITLE)

    run = True
    is_dragging_angle = False
    is_dragging_distance = False
    is_dragging_velocity = False
    clock = pygame.time.Clock()
    while run:
        clock.tick(configurations.GAME_FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        graphics.ball_movement_handler(keys_pressed, ball)
        handle_position_angle, is_dragging_angle = graphics.slider_drag_handler(event, handle_position_angle, is_dragging_angle, configurations.slider_position_angle)
        handle_position_distance, is_dragging_distance = graphics.slider_drag_handler(event, handle_position_distance, is_dragging_distance, configurations.slider_position_distance)
        handle_position_velocity, is_dragging_velocity = graphics.slider_drag_handler(event, handle_position_velocity, is_dragging_velocity, configurations.slider_position_velocity)

        graphics.draw_screen(WIN, ball, handle_position_angle, handle_position_distance, handle_position_velocity)
        print("Angle Value: ", graphics.calc_slider_value(handle_position_angle))
        print("Distance Value: ", graphics.calc_slider_value(handle_position_distance))
        print("Velocity Value: ", graphics.calc_slider_value(handle_position_velocity))

    pygame.quit()


if __name__ == "__main__":
    main()
    
