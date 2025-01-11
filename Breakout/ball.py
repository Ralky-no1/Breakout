from turtle import Turtle
import random
MOVE_DISTANCE = 5

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x = 0, y = -230 )
        self.shape('circle')
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.color('white')
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x = new_x, y = new_y)

    def bounce(self, y_bounce, x_bounce):
        if y_bounce:
            self.y_move *= -1

        if x_bounce:
            self.x_move *= -1

    def reset(self):
        self.goto(x = 0, y = -230)
        self.y_move = 10

