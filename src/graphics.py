import pygame
import colors
import configurations
import objects



def draw_screen(WIN, ball, handle_position_angle, handle_position_distance, handle_position_velocity):
    WIN.blit(objects.STADIUM, configurations.STADIUM_POSITION)
    WIN.blit(objects.LEFT_EDGE, configurations.LEFT_EDGE_POSITION)
    WIN.blit(objects.RIGHT_EDGE, configurations.RIGHT_EDGE_POSITION)
    WIN.blit(objects.BALL, (ball.x, ball.y))
    WIN.blit(objects.LEFT_GOAL, configurations.LEFT_GOAL_POSITION)
    WIN.blit(objects.RIGHT_GOAL, configurations.RIGHT_GOAL_POSITION)

    # -------------   Angle Slider ------------- #
    # Draw slider bar and handle on the screen 
    slider_bar = pygame.Rect(configurations.slider_position_angle, (configurations.slider_width, configurations.slider_height))
    pygame.draw.rect(WIN, configurations.slider_color, slider_bar)

    # Add slider value to the screen
    slider_value = configurations.font.render(str(int(calc_slider_value(handle_position_angle)*100)), True, colors.WHITE)
    WIN.blit(slider_value, (configurations.slider_value_position_angle))

    # Add Slider label to the screen under the slider in center
    slider_label_angle = configurations.font.render(configurations.slider_label_angle, True, configurations.slider_label_color)
    WIN.blit(slider_label_angle, (configurations.slider_label_position_angle))

    # Draw the handle
    handle_center = (handle_position_angle,configurations. slider_position_angle[1] + configurations.slider_height // 2)
    pygame.draw.circle(WIN,configurations. handle_color, handle_center,configurations. handle_radius)

    # -------------   Distance Slider ------------- #
    # Draw slider bar and handle on the screen
    slider_bar = pygame.Rect(configurations.slider_position_distance, (configurations.slider_width, configurations.slider_height))
    pygame.draw.rect(WIN, configurations.slider_color, slider_bar)

    # Add slider value to the screen
    slider_value = configurations.font.render(str(int(calc_slider_value(handle_position_distance)*100)), True, colors.WHITE)
    WIN.blit(slider_value, (configurations.slider_value_position_distance))

    # Add Slider label to the screen under the slider in center
    slider_label_distance = configurations.font.render(configurations.slider_label_distance, True, configurations.slider_label_color)
    WIN.blit(slider_label_distance, (configurations.slider_label_position_distance))

    # Draw the handle
    handle_center = (handle_position_distance,configurations. slider_position_distance[1] + configurations.slider_height // 2)
    pygame.draw.circle(WIN,configurations. handle_color, handle_center,configurations. handle_radius)

    # -------------   Velocity Slider ------------- #
    # Draw slider bar and handle on the screen
    slider_bar = pygame.Rect(configurations.slider_position_velocity, (configurations.slider_width, configurations.slider_height))
    pygame.draw.rect(WIN, configurations.slider_color, slider_bar)

    # Add slider value to the screen
    slider_value = configurations.font.render(str(int(calc_slider_value(handle_position_velocity)*100)), True, colors.WHITE)
    WIN.blit(slider_value, (configurations.slider_value_position_velocity))

    # Add Slider label to the screen under the slider in center
    slider_label_velocity = configurations.font.render(configurations.slider_label_velocity, True, configurations.slider_label_color)
    WIN.blit(slider_label_velocity, (configurations.slider_label_position_velocity))

    # Draw the handle
    handle_center = (handle_position_velocity,configurations. slider_position_velocity[1] + configurations.slider_height // 2)
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

def slider_drag_handler(event, handle_position, is_dragging, slider_position):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (
            mouse_x >= slider_position[0]
            and mouse_x <= slider_position[0] + configurations.slider_width
            and mouse_y >= slider_position[1]
            and mouse_y <= slider_position[1] + configurations.slider_height
        ):
            # Start dragging the slider
            is_dragging = True
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        # Stop dragging the slider
        is_dragging = False
    elif event.type == pygame.MOUSEMOTION and is_dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Update the slider position based on the mouse movement
        handle_position = max(
            slider_position[0],
            min(mouse_x, slider_position[0] + configurations.slider_width)
        )

    return handle_position, is_dragging


def calc_slider_value(handle_position_angle):
    slider_value = (handle_position_angle - configurations.slider_position_angle[0]) / configurations.slider_width
    return slider_value

    