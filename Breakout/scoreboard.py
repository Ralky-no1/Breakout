from turtle import Turtle
import time

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(y = 270, x = -150)
        self.score = 0
        self.lives = 3



    def increase_score(self):
        self.score += 10

    def update_score(self):
        self.clear()
        self.write(f"|Score: {self.score}|              |Lives : {self.lives}|" , font = ('Ariel',30,'bold'))

    def win_game(self):
        self.goto(0, 0)
        self.write('YOU WON!', font=('Ariel', 20, 'bold'))

    def lose_life(self):
        self.lives -= 1

    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER!' , font = ('Ariel',20,'bold'))
