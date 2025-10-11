from turtle import Screen
from paddle import Paddle
import time

myScreen = Screen()
myScreen.title("Pong Game")
myScreen.bgcolor("black")
myScreen.setup(800, 600)
myScreen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))

is_game_on = True

while is_game_on:
    myScreen.update()
    time.sleep(0.1)
    r_paddle.move_paddle('Up', 'Down')
    l_paddle.move_paddle('w', 's')







myScreen.exitonclick()

