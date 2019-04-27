import pygame
import sys

SCREEN_SIZE = [640, 480]
WIDTH = SCREEN_SIZE[0]
HEIGHT = SCREEN_SIZE[1]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BRICK_COLOR = (200, 200, 0)

BRICK_WIDTH = 60
BRICK_HEIGHT = 15

PADDLE_WIDTH = 60
PADDLE_HEIGHT = 12

BALL_DIAMETER = 16
BALL_RADIUS = int(BALL_DIAMETER / 2)

MAX_PADDLE_X = WIDTH - PADDLE_WIDTH
MAX_BALL_X = WIDTH - BALL_DIAMETER
MAX_BALL_Y = HEIGHT - BALL_DIAMETER

PADDLE_Y = HEIGHT - PADDLE_HEIGHT - 10

STATE_BALL_IN_PADDLE = 0
STATE_PLAYING = 1
STATE_WON = 2
STATE_GAME_OVER = 3


class PB:
    def __init__(self):
        pass

    def init_game(self):
        pass

    def create_bricks(self):
        pass

    def draw_bricks(self):
        pass

    def check_input(self):
       pass

    def move_ball(self):
       pass

    def handle_collisions(self):
       pass

    def show_stats(self):
       pass

    def show_message(self, message):
        pass

    def run(self):
        pass


if __name__ == "__main__":
    pass