import math
import pygame as pg
import configurations

# assuming resolution is 96 PPI (pixels per inch), convert to PPC (pixels per centimeter)
ppc = 25.4 / 96
ppm = ppc * 100  # convert PPC to PPM (pixels per meter)

ball_path_list = []


def timeOfFlight(theta, initial_velocity):
    """
    Calculates the time of flight of the ball

    :param theta: angle of launch
    :param initial_velocity: initial velocity of the ball
    :return: The time of flight of the ball
    """
    return round((2 * initial_velocity * math.sin(theta)) / configurations.GRAVITY, 2)


def getMaxHeight(theta, initial_velocity):
    """
    Calculates the maximum height of the ball

    :param theta: angle of launch
    :param initial_velocity: initial velocity of the ball
    :return: The maximum height of the ball
    """

    # get time of flight of the ball then calculate the maximum height
    T = initial_velocity * math.sin(math.radians(theta)) / configurations.GRAVITY
    h = initial_velocity * math.sin(math.radians(theta)) * T - 0.5 * configurations.GRAVITY * T ** 2

    configurations.maxHeight = round(h, 2)
    return round(h, 2)


def convertPixelToMeter(pixels):
    """'
    Converts pixels to meters

    :param pixels: pixels to be converted
    :return: meters
    """
    return pixels / ppm


def calculateGoalHeight(init_vel, theta, distance):
    """
    Calculates the height of the ball at the goal

    :param init_vel: initial velocity of the ball
    :param theta: angle of launch
    :param distance: distance of the ball from the goal
    :return: Goal height
    """

    # calculate the x and y components of the initial velocity
    vel_x = init_vel * math.cos(math.radians(theta))
    vel_y = abs(init_vel * math.sin(math.radians(theta)))

    # calculate the time of flight of the ball
    t = distance / vel_x

    # calculate the height of the ball at the goal
    height_at_goal = vel_y * t - 0.5 * configurations.GRAVITY * t ** 2

    configurations.ballHeightAtGoal = round((configurations.maxHeight - height_at_goal), 2)


def launch(theta, initial_velocity):
    """
    Calculates the initial velocity of the ball in the x and y direction

    :param theta: angle of launch
    :param initial_velocity: initial velocity of the ball
    :return: start_time, start_x_velocity, start_y_velocity
    """
    start_time = pg.time.get_ticks()
    start_x_velocity = initial_velocity * math.cos(math.radians(theta))
    start_y_velocity = abs(initial_velocity * math.sin(math.radians(theta)))
    return start_time, start_x_velocity, start_y_velocity


def update(ball, start_time, start_x_velocity, start_y_velocity, max_h):
    """
    Updates the position of the ball based on the time passed since launch and the initial velocity of the ball in the
    x and y direction

    :param ball: ball object
    :param start_time: start time of the ball
    :param start_x_velocity: start x velocity of the ball
    :param start_y_velocity: start y velocity of the ball
    :param max_h: maximum height of the ball
    :return: True if the ball is still in the air, False if the ball has landed
    """

    # calculate the time passed since launch
    time_passed = (pg.time.get_ticks() - start_time) / 1000 * 8

    # if this is the first time the ball is updating, pass
    if time_passed == 0:
        return True

    # calculate the change in x and y position of the ball
    change_x = start_x_velocity * time_passed

    # Physics formula: final_pos = vi * time_passed + 1/2 * - configurations.GRAVITY * time_passed ** 2
    change_y = (start_y_velocity * time_passed) - \
               (0.5 * configurations.GRAVITY * pow(time_passed, 2))

    # update the position of the ball
    ball.x = configurations.BALL_POSITION[0] + change_x * configurations.BALL_UPDATE_VELOCITY

    # if the ball is still in the air, update the position of the ball
    if configurations.BALL_POSITION[1] - change_y * configurations.BALL_UPDATE_VELOCITY < configurations.GAME_HEIGHT - 240:

        # if the ball is in the goal, update the position of the ball
        if configurations.GAME_HEIGHT - 240 > ball.y > configurations.GAME_HEIGHT - 460 and \
                ball.x >= configurations.RIGHT_EDGE_POSITION[0] + 80:
            ball.y = configurations.BALL_POSITION[1]
            return False

        else:
            ball.y = configurations.BALL_POSITION[1] - \
                     change_y * configurations.BALL_UPDATE_VELOCITY
    else:
        return False

    return True
