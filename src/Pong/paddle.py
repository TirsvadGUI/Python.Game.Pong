from turtle import Turtle


class Paddle(Turtle):
    MOVE_DISTANCE = 20

    def __init__(self, paddle_pos: (int, int)):
        """
        Initialise the paddle for a player in pong game

        :param paddle_pos: Paddle start position
        :type paddle_pos: tuple (int, int)
        """
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(paddle_pos)

    def move_up(self):
        """
        Move paddle up

        :return:
        """
        current_pos = self.ycor()
        if current_pos < 240:
            self.sety(current_pos + self.MOVE_DISTANCE)

    def move_down(self):
        """
        Move paddle down

        :return:
        """
        current_pos = self.ycor()
        if -240 < current_pos:
            self.sety(current_pos - self.MOVE_DISTANCE)
