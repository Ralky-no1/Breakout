from turtle import Screen
from paddle import Paddle
from ball import Ball
from  bricks import Bricks
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width = 1200,height=700)
screen.bgcolor('black')
screen.title('Breakout')
screen.tracer(0)

paddle = Paddle()
ball= Ball()
bricks = Bricks()
score = Scoreboard()

screen.listen()
screen.onkey(key='Left',fun = paddle.move_left)
screen.onkey(key = 'Right',fun = paddle.move_right)

def collision_with_walls():
    global ball
    if ball.xcor() > 570:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
    if ball.xcor() < -580:
        ball.bounce(x_bounce=True, y_bounce=False)
        return
    if ball.ycor() > 270:
        ball.bounce(x_bounce=False,y_bounce=True)
    if ball.ycor() < -280:
        ball.reset()
        score.lose_life()
        return


def collision_with_paddle():
    global ball, paddle

    paddle_x = paddle.xcor()
    ball_x = ball.xcor()


    if ball.distance(paddle) < 110 and ball.ycor() < -250:


        if paddle_x > 0:
            if ball_x > paddle_x:

                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


        elif paddle_x < 0:
            if ball_x < paddle_x:

                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


        else:
            if ball_x > paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            elif ball_x < paddle_x:
                ball.bounce(x_bounce=True, y_bounce=True)
                return
            else:
                ball.bounce(x_bounce=False, y_bounce=True)
                return


def collision_with_bricks():
    global ball, bricks

    for brick in bricks.bricks:
        if ball.distance(brick) < 40:
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)
                score.increase_score()


            if ball.xcor() < brick.left_wall:
                ball.bounce(x_bounce=True, y_bounce=False)


            elif ball.xcor() > brick.right_wall:
                ball.bounce(x_bounce=True, y_bounce=False)


            elif ball.ycor() < brick.bottom_wall:
                ball.bounce(x_bounce=False, y_bounce=True)


            elif ball.ycor() > brick.upper_wall:
                ball.bounce(x_bounce=False, y_bounce=True)

playing_game = True
while playing_game:
    screen.update()
    time.sleep(0.01)
    ball.move()

    collision_with_walls()

    collision_with_paddle()

    collision_with_bricks()

    score.update_score()

    if score.lives == 0:
        score.game_over()
        playing_game = False

    if len(bricks.bricks) == 0:
        score.win_game()
        playing_game = False


screen.mainloop()