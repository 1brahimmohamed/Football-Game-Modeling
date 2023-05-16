import math
import pygame as pg
import configurations

gravity = 9.8
# assuming resolution is 96 PPI (pixels per inch), convert to PPC (pixels per centimeter)
ppc = 25.4 / 96
ppm = ppc * 100  # convert PPC to PPM (pixels per meter)

ball_path_list = []


def timeOfFlight(theta, intial_velocity):
    return round((2 * intial_velocity * math.sin(theta)) / gravity, 2)


def getMaxHeight(theta, intial_velocity):
    
    T = intial_velocity * math.sin(math.radians(theta)) / gravity
    h = intial_velocity * math.sin(math.radians(theta)) * T - 0.5 * gravity * T ** 2

    configurations.maxHeight = round(h, 2)
    return round(h, 2)


def convertPixeltoMeter(pixels):
    return pixels / ppm


def calculateGoalHeight(init_vel, theta ,distance):
    vel_x = init_vel * math.cos(math.radians(theta))
    vel_y = abs(init_vel * math.sin(math.radians(theta)))
    
    t = distance/vel_x
    height_at_goal = vel_y*t - 0.5 * gravity * t ** 2
    configurations.ballHeightatGoal =  round((configurations.maxHeight - height_at_goal), 2)


def launch(theta, intial_velocity):
    start_time = pg.time.get_ticks()
    start_x_velocity = intial_velocity * math.cos(math.radians(theta))
    start_y_velocity = abs(intial_velocity * math.sin(math.radians(theta)))
    return start_time, start_x_velocity, start_y_velocity


def update(ball, start_time, start_x_velocity, start_y_velocity, max_h):

    time_passed = (pg.time.get_ticks() - start_time) / 1000 * 8

    change_x = start_x_velocity * time_passed

    # Physics formula: final_pos = vi * time_passed + 1/2 * -GRAVITY * time_passed ** 2
    change_y = (start_y_velocity * time_passed) - \
        (0.5 * configurations.GRAVITY * pow(time_passed, 2))
    ball.x = configurations.BALL_POSITION[0] + \
        change_x * configurations.BALL_UPDATE_VELOCITY

    if time_passed == 0:
        return True


    if configurations.BALL_POSITION[1] - change_y * configurations.BALL_UPDATE_VELOCITY < configurations.GAME_HEIGHT - 240:
        if ball.y < configurations.GAME_HEIGHT - 240 and \
                ball.y > configurations.GAME_HEIGHT - 460 and\
                ball.x >= configurations.RIGHT_EDGE_POSITION[0] + 80:
            ball.y = configurations.BALL_POSITION[1]
            return False

        else:
            ball.y = configurations.BALL_POSITION[1] - \
                change_y * configurations.BALL_UPDATE_VELOCITY
    else:
        return False

    return True
