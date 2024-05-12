from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep
from src.Pong.constants import *


class Pong:
    def __init__(self):

        screen = Screen()
        screen.setup(width=800, height=600)
        screen.bgcolor("black")
        screen.title("Pong game")
        screen.tracer(0)

        l_paddle = Paddle(L_PADDLE_START_POS)
        r_paddle = Paddle(R_PADDLE_START_POS)
        ball = Ball()
        scoreboard = Scoreboard()

        screen.listen()
        screen.onkeypress(fun=l_paddle.move_up, key=L_PADDLE_MOVE_UP)
        screen.onkeypress(fun=l_paddle.move_down, key=L_PADDLE_MOVE_DOWN)
        screen.onkeypress(fun=r_paddle.move_up, key=R_PADDLE_MOVE_UP)
        screen.onkeypress(fun=r_paddle.move_down, key=R_PADDLE_MOVE_DOWN)

        is_game_on = True
        while is_game_on:
            sleep(ball.move_speed)
            screen.update()
            ball.move()

            if ball.ycor() > 280 or ball.ycor() < -280:
                ball.bounce_y()

            if (ball.xcor() == 330 and ball.distance((r_paddle.position()[0], r_paddle.position()[1])) < 60
                    or ball.xcor() == -330 and ball.distance((l_paddle.position()[0], l_paddle.position()[1])) < 60):
                ball.bounce_x()

            # Detect left paddle misses
            if ball.xcor() < -380:
                ball.reset_position()
                scoreboard.increase_score_right_paddle()

            # Detect right paddle misses
            if ball.xcor() > 380:
                ball.reset_position()
                scoreboard.increase_score_left_paddle()

            if scoreboard.has_a_winner():
                is_game_on = False

        scoreboard.game_over()
        screen.exitonclick()
