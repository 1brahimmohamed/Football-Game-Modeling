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

WIN = pygame.display.set_mode((configurations.GAME_WIDTH, configurations.GAME_HEIGHT))
pygame.display.set_caption(configurations.GAME_TITLE)


def main():
    ball = pygame.Rect(configurations.BALL_POSITION, configurations.BALL_SCALE)
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
    current_mouse_position = pygame.mouse.get_pos()

    max_h = physics.getMaxHeight(configurations.BALL_ANGLE, configurations.BALL_INITIAL_VELOCITY)
    start_time, start_x_velocity, start_y_velocity = 0, 0, 0
    flag = False


    while run:
        clock.tick(configurations.GAME_FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start_time, start_x_velocity, start_y_velocity = physics.launch(configurations.BALL_ANGLE,
                                                                                    configurations.BALL_INITIAL_VELOCITY)
                    flag = True

        if flag:
            flag = physics.update(ball, start_time, start_x_velocity, start_y_velocity, max_h)

        current_mouse_position = pygame.mouse.get_pos()

        handle_position_angle, is_dragging_angle = graphics.slider_drag_handler(event, handle_position_angle, is_dragging_angle, configurations.slider_position_angle)
        handle_position_distance, is_dragging_distance = graphics.slider_drag_handler(event, handle_position_distance, is_dragging_distance, configurations.slider_position_distance)
        handle_position_velocity, is_dragging_velocity = graphics.slider_drag_handler(event, handle_position_velocity, is_dragging_velocity, configurations.slider_position_velocity)
        
        graphics.draw_screen(WIN, ball, configurations.BALL_ANGLE ,current_mouse_position, handle_position_angle, handle_position_distance, handle_position_velocity)
        
        configurations.BALL_ANGLE = graphics.calc_slider_value_angle(handle_position_angle)
        configurations.BALL_INITIAL_VELOCITY = graphics.calc_slider_value_velocity(handle_position_velocity)
        configurations.BALL_POSITION = (graphics.calc_slider_value_distance(handle_position_distance), configurations.BALL_POSITION[1])
        
        
        if is_dragging_distance or is_dragging_angle or is_dragging_velocity:
            graphics.ball_movement_handler(ball, graphics.calc_slider_value_distance(handle_position_distance))
            graphics.draw_screen(WIN, ball,configurations.BALL_ANGLE, current_mouse_position, handle_position_angle, handle_position_distance, handle_position_velocity)

    pygame.quit()


if __name__ == "__main__":
    main()
