from turtle import Turtle, Screen
RIGHT_POSITION = [(380, 50), (380, 30), (380, 10), (380, -10), (380, -30), (380, -50)]
LEFT_POSITION = [(-380, 50), (-380, 30), (-380, 10), (-380, -10), (-380, -30), (-380, -50)]
myScreen = Screen()

class Paddle:
    def __init__(self):
        self.paddle = []
        self.create_right_paddle()
        self.create_left_paddle()

    def create_right_paddle(self):
        for position in RIGHT_POSITION:
            self.add_paddle(position)

    def create_left_paddle(self):
        for position in LEFT_POSITION:
            self.add_paddle(position)

    def add_paddle(self, position):
        my_paddle = Turtle('square')
        my_paddle.color('white')
        my_paddle.penup()
        my_paddle.goto(position)
        self.paddle.append(my_paddle)
