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
    time.sleep(0.2)
    myScreen.update()
    r_paddle.move_paddle('Up', 'Down')
    l_paddle.move_paddle('w', 's')
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if r_paddle.xcor() - ball.xcor() < 20 or abs(l_paddle.xcor()) - abs(ball.xcor()) < 20:
        ball.x_bounce()





myScreen.exitonclick()

