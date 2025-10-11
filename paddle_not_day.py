from turtle import Turtle, Screen
RIGHT_POSITION = (380, 0)
LEFT_POSITION = (-380, 0)
UP = 90
DOWN = 270
MOVE_DISTANCE = 20

myScreen = Screen()
myScreen.listen()

class Paddle:
    def __init__(self):
        self.my_paddle_left = None
        self.my_paddle_right = None
        self.create_left_paddle()
        self.create_right_paddle()

    def create_left_paddle(self):
        self.add_paddle_left(LEFT_POSITION)

    def create_right_paddle(self):
        self.add_paddle_right(RIGHT_POSITION)

    def add_paddle_left(self, position):
        self.my_paddle_left = Turtle('square')
        self.my_paddle_left.color('white')
        self.my_paddle_left.penup()
        self.my_paddle_left.shapesize(5, 1)
        self.my_paddle_left.goto(position)

    def add_paddle_right(self, position):
        self.my_paddle_right = Turtle('square')
        self.my_paddle_right.color('white')
        self.my_paddle_right.penup()
        self.my_paddle_right.shapesize(5, 1)
        self.my_paddle_right.goto(position)

    def paddle_1_go_up(self):
        new_y = self.my_paddle_left.ycor() + MOVE_DISTANCE
        self.my_paddle_left.goto(self.my_paddle_left.xcor(), new_y)

    def paddle_1_go_down(self):
        new_y = self.my_paddle_left.ycor() - MOVE_DISTANCE
        self.my_paddle_left.goto(self.my_paddle_left.xcor(), new_y)

    def paddle_2_go_up(self):
        new_y = self.my_paddle_right.ycor() + MOVE_DISTANCE
        self.my_paddle_right.goto(self.my_paddle_right.xcor(), new_y)

    def paddle_2_go_down(self):
        new_y = self.my_paddle_right.ycor() - MOVE_DISTANCE
        self.my_paddle_right.goto(self.my_paddle_right.xcor(), new_y)

    def move_paddle(self):
        myScreen.onkey(self.paddle_1_go_up, 'Up')
        myScreen.onkey(self.paddle_1_go_down, 'Down')
        myScreen.onkey(self.paddle_2_go_up, 'w')
        myScreen.onkey(self.paddle_2_go_down, 's')
