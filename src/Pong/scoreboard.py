from turtle import Turtle


class Scoreboard(Turtle):

    ALIGNMENT = "center"
    FONT_NAME = "Courier"
    FONT_SIZE = 60
    FONT_SIZE_GAME_OVER = 40
    FONT_TYPE = "normal"
    WINNER_SCORE = 10
    left_paddle_score: int
    right_paddle_score: int

    def __init__(self):
        super().__init__()
        self.left_paddle_score = 0
        self.right_paddle_score = 0
        self.color("yellow")
        self.penup()
        self.goto(0, 200)
        self.hideturtle()
        self.FONT = (self.FONT_NAME, self.FONT_SIZE, self.FONT_TYPE)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Visualize the scoreboard

        :return:
        """
        self.clear()
        self.write(arg=f"{self.left_paddle_score} - {self.right_paddle_score}", align=self.ALIGNMENT, font=self.FONT)

    def increase_score_left_paddle(self):
        """

        :return:
        """
        self.left_paddle_score += 1
        self.update_scoreboard()

    def increase_score_right_paddle(self):
        """

        :return:
        """
        self.right_paddle_score += 1
        self.update_scoreboard()

    def has_a_winner(self) -> bool:
        """
        Check if a paddle has reach a winning score

        :return bool:
        """
        if self.left_paddle_score == self.WINNER_SCORE or self.right_paddle_score == self.WINNER_SCORE:
            return True
        return False

    def who_won(self) -> str:
        """
        Returns a formatted string af the winner

        :return str:
        """
        if self.left_paddle_score == self.WINNER_SCORE:
            return "left paddle win"
        elif self.left_paddle_score == self.WINNER_SCORE:
            return "right paddle win"
        raise Exception

    def game_over(self):
        """
        End result to screen

        :return:
        """
        self.clear()
        self.update_scoreboard()
        self.goto(0, 0)
        font = (self.FONT_NAME, self.FONT_SIZE_GAME_OVER, self.FONT_TYPE)
        self.write(arg=f"Game over", move=True, align=self.ALIGNMENT, font=font)
        self.goto(0, self.ycor() - self.FONT_SIZE_GAME_OVER)
        self.write(arg=f"{self.who_won()}", move=True, align=self.ALIGNMENT, font=font)
