from turtle import Turtle, Screen
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

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_paddle(self, key1, key2):
        myScreen.onkey(self.go_up, key1)
        myScreen.onkey(self.go_down, key2)

