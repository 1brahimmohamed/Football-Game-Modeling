import configurations
import graphics
import physics

# Check if pygame is installed
try:
    print("[GAME] Trying to import pygame")
    import pygame

    print("[GAME] Pygame imported")
except:
    print("[EXCEPTION] Pygame not installed")


# Initialize pygame window and set caption
WIN = pygame.display.set_mode((configurations.GAME_WIDTH, configurations.GAME_HEIGHT))
pygame.display.set_caption(configurations.GAME_TITLE)


def main():
    global WIN

    # create ball object rectangle
    ball = pygame.Rect(configurations.BALL_POSITION, configurations.BALL_SCALE)

    # set initial slider positions
    handle_position_angle = configurations.slider_position_angle[0]
    handle_position_distance = configurations.slider_position_distance[0]
    handle_position_velocity = configurations.slider_position_velocity[0]

    # initialize pygame
    pygame.init()

    # initialize pygame window width and height
    WIN = pygame.display.set_mode((configurations.GAME_WIDTH, configurations.GAME_HEIGHT))

    run = True

    # initialize dragging variables
    is_dragging_angle = False
    is_dragging_distance = False
    is_dragging_velocity = False

    # initialize clock
    clock = pygame.time.Clock()

    # initialize ball variables
    start_time, start_x_velocity, start_y_velocity, max_h = 0, 0, 0, 0
    flag = False

    # main game loop
    while run:
        # set the game fps
        clock.tick(configurations.GAME_FPS)

        # listen for events
        for event in pygame.event.get():

            # check if the user wants to quit the game
            if event.type == pygame.QUIT:
                run = False

            # check if the user is kicking the ball
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # calculate the initial velocity and start time
                    start_time, start_x_velocity, start_y_velocity = physics.launch(configurations.BALL_ANGLE,
                                                                                    configurations.BALL_INITIAL_VELOCITY * configurations.BALL_INITIAL_VELOCITY_FACTOR)
                    # get the maximum height of the ball
                    max_h = physics.getMaxHeight(configurations.BALL_ANGLE, configurations.BALL_INITIAL_VELOCITY)
                    flag = True

        # check if the ball is launched
        if flag:
            # update the ball position
            flag = physics.update(ball, start_time, start_x_velocity, start_y_velocity, max_h)

            # calculate the ball height
            physics.calculateGoalHeight(configurations.BALL_INITIAL_VELOCITY,
                                        configurations.BALL_ANGLE,
                                        configurations.BALL_DISTANCE)

        # get the current mouse position
        current_mouse_position = pygame.mouse.get_pos()

        # check if the user is dragging the sliders
        handle_position_angle, is_dragging_angle = graphics.slider_drag_handler(event, handle_position_angle, is_dragging_angle, configurations.slider_position_angle)
        handle_position_distance, is_dragging_distance = graphics.slider_drag_handler(event, handle_position_distance, is_dragging_distance, configurations.slider_position_distance)
        handle_position_velocity, is_dragging_velocity = graphics.slider_drag_handler(event, handle_position_velocity, is_dragging_velocity, configurations.slider_position_velocity)

        # draw the screen
        graphics.draw_screen(WIN, ball, configurations.BALL_ANGLE ,current_mouse_position, handle_position_angle, handle_position_distance, handle_position_velocity)

        # update the ball settings based on the slider positions
        configurations.BALL_ANGLE = graphics.calc_slider_value_angle(handle_position_angle)
        configurations.BALL_INITIAL_VELOCITY = graphics.calc_slider_value_velocity(handle_position_velocity)

        # update the ball distance based on the slider positions but invert the value
        sliderDist = graphics.calc_slider_value_distance(handle_position_distance)
        configurations.BALL_DISTANCE = 50 - sliderDist

        # check if the user is dragging the sliders
        if is_dragging_distance or is_dragging_angle or is_dragging_velocity:
            # update the ball position
            graphics.ball_movement_handler(ball, sliderDist * physics.ppm)
            # draw the screen
            graphics.draw_screen(WIN, ball,configurations.BALL_ANGLE, current_mouse_position, handle_position_angle, handle_position_distance, handle_position_velocity)

    pygame.quit()


if __name__ == "__main__":
    main()
