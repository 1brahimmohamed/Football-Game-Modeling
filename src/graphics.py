import pygame
import colors
import configurations
import objects



def draw_screen(WIN, ball, slider_pos):
    WIN.blit(objects.STADIUM, configurations.STADIUM_POSITION)
    WIN.blit(objects.LEFT_EDGE, configurations.LEFT_EDGE_POSITION)
    WIN.blit(objects.RIGHT_EDGE, configurations.RIGHT_EDGE_POSITION)
    WIN.blit(objects.BALL, (ball.x, ball.y))
    WIN.blit(objects.LEFT_GOAL, configurations.LEFT_GOAL_POSITION)
    WIN.blit(objects.RIGHT_GOAL, configurations.RIGHT_GOAL_POSITION)

    # Draw vertical slider bar and handle on the screen 
    slider_bar = pygame.Rect(configurations.slider_position, (configurations.slider_width, configurations.slider_height))
    pygame.draw.rect(WIN, configurations.slider_color, slider_bar)

    # Draw the handle
    handle_center = (slider_pos,configurations. slider_position[1] + configurations.slider_height // 2)
    pygame.draw.circle(WIN,configurations. handle_color, handle_center,configurations. handle_radius)

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

def slider_drag_handler(event, slider_pos, is_dragging):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (
            mouse_x >= configurations.slider_position[0]
            and mouse_x <= configurations.slider_position[0] + configurations.slider_width
            and mouse_y >= configurations.slider_position[1]
            and mouse_y <= configurations.slider_position[1] + configurations.slider_height
        ):
            # Start dragging the slider
            is_dragging = True
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        # Stop dragging the slider
        is_dragging = False
    elif event.type == pygame.MOUSEMOTION and is_dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Update the slider position based on the mouse movement
        slider_pos = max(
            configurations.slider_position[0],
            min(mouse_x, configurations.slider_position[0] + configurations.slider_width)
        )

    return slider_pos, is_dragging


def calc_slider_value(slider_pos):
    slider_value = (slider_pos - configurations.slider_position[0]) / configurations.slider_width
    return slider_value

    