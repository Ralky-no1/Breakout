from turtle import Turtle
MOVE_DISTANCE = 30

class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x = 0, y = -270 )
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.color('steel blue')

    def move_right(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.backward(MOVE_DISTANCE)


