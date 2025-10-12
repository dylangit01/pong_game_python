from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

myScreen = Screen()
myScreen.title("Pong Game")
myScreen.bgcolor("black")
myScreen.setup(800, 600)
myScreen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()

is_game_on = True

while is_game_on:
    time.sleep(0.15)
    myScreen.update()
    r_paddle.move_paddle('Up', 'Down')
    l_paddle.move_paddle('w', 's')
    ball.move()

    # Detect collision with wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    # Detect collision with paddle:
    # if ball.distance(l_paddle) < 55:
    #     print(f'{ball.xcor()}.....????')
    # print(ball.xcor())
    if ball.distance(r_paddle) < 55 and (371 > ball.xcor() > 360) or ball.distance(l_paddle) < 55 and (-380 < ball.xcor() < -360):
        ball.x_bounce()





myScreen.exitonclick()

