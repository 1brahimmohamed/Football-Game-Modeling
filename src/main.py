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
    slider_pos = configurations.slider_position[0]

    pygame.init()
    WIN = pygame.display.set_mode((configurations.GAME_WIDTH, configurations.GAME_HEIGHT))
    pygame.display.set_caption(configurations.GAME_TITLE)

    run = True
    is_dragging = False
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
        slider_pos, is_dragging = graphics.slider_drag_handler(event, slider_pos, is_dragging)

        configurations.BALL_INITIAL_VELOCITY = graphics.calc_slider_value(slider_pos)
        graphics.draw_screen(WIN, ball, current_mouse_position, slider_pos)


    pygame.quit()


if __name__ == "__main__":
    main()
