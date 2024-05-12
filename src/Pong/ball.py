from turtle import Turtle


class Ball(Turtle):

    x_move: int
    y_move: int
    move_speed: float

    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.color("white")
        self.setheading(45)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """
        Move the ball a step

        :return:
        """
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(x=new_xcor, y=new_ycor)

    def bounce_y(self):
        """
        Make the ball bounce at y aisle

        :return:
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Make the ball bounce at x aisle

        :return:
        """
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.setposition(0, 0)
        self.bounce_x()
        self.move_speed = 0.1
