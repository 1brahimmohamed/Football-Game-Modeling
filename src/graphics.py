import pygame
import colors
import configurations
import objects
import math

# Title at the center of the screen
font = pygame.font.SysFont("poppinsbold", 40)
text_surface = font.render(
    "Sports Engineering - Team 10 Project", True, colors.WHITE)


def draw_screen(WIN,
                ball,
                angle,
                current_mouse_position,
                handle_position_angle,
                handle_position_distance,
                handle_position_velocity):
    """
    Draws the screen with all the objects and text every frame.

    :param WIN: The window to draw on
    :param ball: The ball object
    :param angle: The angle of the ball
    :param current_mouse_position: The current mouse position
    :param handle_position_angle: The position of the angle handle
    :param handle_position_distance: The position of the distance handle
    :param handle_position_velocity: The position of the velocity handle
    :return: None

    """
    # Draw the background
    WIN.blit(objects.STADIUM, configurations.STADIUM_POSITION)

    # Draw the title
    WIN.blit(text_surface, (configurations.GAME_WIDTH // 2 - 250, 100))

    # Draw Goal Edge
    WIN.blit(objects.LEFT_EDGE, configurations.LEFT_EDGE_POSITION)
    WIN.blit(objects.RIGHT_EDGE, configurations.RIGHT_EDGE_POSITION)

    # Draw the Text of Max Height and Goal Height
    text_goal_height = font.render(
        "Goal Height: " + str(configurations.ballHeightAtGoal), True, colors.WHITE)
    text_max_height = font.render(
        "Max Height: " + str(configurations.maxHeight), True, colors.WHITE)

    WIN.blit(text_goal_height, (configurations.GAME_WIDTH - 300, 665))
    WIN.blit(text_max_height, (configurations.GAME_WIDTH - 300, 710))

    # Draw the angle line from the ball
    angle = math.radians(angle)
    length = 60  # Example line length

    end_x = ball.centerx + length * math.cos(angle)
    end_y = ball.centery - length * math.sin(angle)

    pygame.draw.line(WIN,
                     colors.WHITE,
                     (ball.x + 20, ball.y + 20),
                     (end_x, end_y),
                     3)

    # Draw the ball
    WIN.blit(objects.BALL, (ball.x, ball.y))

    # Draw the goal
    WIN.blit(objects.LEFT_GOAL, configurations.LEFT_GOAL_POSITION)
    WIN.blit(objects.RIGHT_GOAL, configurations.RIGHT_GOAL_POSITION)

    # ---------------------------------------   Angle Slider --------------------------------------- #
    # Draw slider bar and handle on the screen
    slider_bar = pygame.Rect(configurations.slider_position_angle,
                             (configurations.slider_width, configurations.slider_height))
    pygame.draw.rect(WIN, configurations.slider_color, slider_bar)

    # Add slider value to the screen
    slider_value = configurations.font.render(
        str(int(calc_slider_value_angle(handle_position_angle))), True, colors.WHITE)
    WIN.blit(slider_value, (configurations.slider_value_position_angle))

    # Add Slider label to the screen under the slider in center
    slider_label_angle = configurations.font.render(
        configurations.slider_label_angle, True, configurations.slider_label_color)
    WIN.blit(slider_label_angle, (configurations.slider_label_position_angle))

    # Draw the handle
    handle_center = (handle_position_angle,
                     configurations.slider_position_angle[1] + configurations.slider_height // 2)
    pygame.draw.circle(WIN, configurations.handle_color,
                       handle_center, configurations.handle_radius)

    # ---------------------------------------   Distance Slider --------------------------------------- #
    # Draw slider bar and handle on the screen
    slider_bar = pygame.Rect(configurations.slider_position_distance,
                             (configurations.slider_width, configurations.slider_height))
    pygame.draw.rect(WIN, configurations.slider_color, slider_bar)

    # Add slider value to the screen
    slider_value = configurations.font.render(str(
        50 - int(calc_slider_value_distance(handle_position_distance))), True, colors.WHITE)
    WIN.blit(slider_value, (configurations.slider_value_position_distance))

    # Add Slider label to the screen under the slider in center
    slider_label_distance = configurations.font.render(
        configurations.slider_label_distance, True, configurations.slider_label_color)
    WIN.blit(slider_label_distance,
             (configurations.slider_label_position_distance))

    # Draw the handle
    handle_center = (handle_position_distance,
                     configurations.slider_position_distance[1] + configurations.slider_height // 2)
    pygame.draw.circle(WIN, configurations.handle_color,
                       handle_center, configurations.handle_radius)

    # ---------------------------------------   Velocity Slider --------------------------------------- #
    # Draw slider bar and handle on the screen
    slider_bar = pygame.Rect(configurations.slider_position_velocity,
                             (configurations.slider_width, configurations.slider_height))
    pygame.draw.rect(WIN, configurations.slider_color, slider_bar)

    # Add slider value to the screen
    slider_value = configurations.font.render(str(
        int(calc_slider_value_velocity(handle_position_velocity))), True, colors.WHITE)
    WIN.blit(slider_value, (configurations.slider_value_position_velocity))

    # Add Slider label to the screen under the slider in center
    slider_label_velocity = configurations.font.render(
        configurations.slider_label_velocity, True, configurations.slider_label_color)
    WIN.blit(slider_label_velocity,
             (configurations.slider_label_position_velocity))

    # Draw the handle
    handle_center = (handle_position_velocity,
                     configurations.slider_position_velocity[1] + configurations.slider_height // 2)
    pygame.draw.circle(WIN, configurations.handle_color,
                       handle_center, configurations.handle_radius)
    pygame.display.update()


def ball_movement_handler(ball, sliderVal):
    """
    Moves the ball to the left or right based on the slider value

    :param ball: The ball object
    :param sliderVal: The value of the slider
    :return: None
    """
    ball.x = sliderVal
    configurations.BALL_POSITION = (sliderVal, configurations.BALL_POSITION[1])


def slider_drag_handler(event, handle_position_angle, is_dragging, slider_position):
    """
    Handles the dragging of the slider

    :param event: The event that is happening
    :param handle_position_angle: The position of the handle
    :param is_dragging: Whether the slider is being dragged or not
    :param slider_position: The position of the slider
    :return: None
    """
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (
                slider_position[0] <= mouse_x <= slider_position[0] + configurations.slider_width
                and slider_position[1] <= mouse_y <= slider_position[1] + configurations.slider_height
        ):
            # Start dragging the slider
            is_dragging = True
    elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
        # Stop dragging the slider
        is_dragging = False
    elif event.type == pygame.MOUSEMOTION and is_dragging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        # Update the slider position based on the mouse movement
        handle_position_angle = max(
            slider_position[0],
            min(mouse_x, slider_position[0] + configurations.slider_width)
        )

    return handle_position_angle, is_dragging


def calc_slider_value_angle(handle_position_angle):
    """
    Calculates the angle slider value based on the handle position

    :param handle_position_angle: The position of the handle
    :return: None
    """

    slider_value = (handle_position_angle -
                    configurations.slider_position_angle[0]) / configurations.slider_width
    proportion = (slider_value - 0) / (1 - 0)
    return (proportion * (89 - 0)) + 0


def calc_slider_value_distance(handle_position_distance):
    """
    Calculates the distance slider value based on the handle position
    :param handle_position_distance:  The position of the handle
    :return: None
    """

    slider_value = (handle_position_distance -
                    configurations.slider_position_distance[0]) / configurations.slider_width
    proportion = (slider_value - 0) / (1 - 0)
    return (proportion * (45 - 5)) + 5


def calc_slider_value_velocity(handle_position_velocity):
    """
    Calculates the velocity slider value based on the handle position

    :param handle_position_velocity: The position of the handle
    :return: None
    """
    slider_value = (handle_position_velocity -
                    configurations.slider_position_velocity[0]) / configurations.slider_width
    proportion = (slider_value - 0) / (1 - 0)
    return (proportion * (150 - 20)) + 20
