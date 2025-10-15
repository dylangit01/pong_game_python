from turtle import Turtle, Screen
import time
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

myScreen = Screen()
myScreen.listen()

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(5, 1)
        self.goto(position)


    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        if new_y >= 250:
            self.goto(self.xcor(), 250)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
        if new_y <= -240:
            self.goto(self.xcor(), -240)

    def move_paddle(self, key1, key2):
        myScreen.onkey(self.go_up, key1)
        myScreen.onkey(self.go_down, key2)

