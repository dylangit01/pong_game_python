from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 36, "bold")

class Scoreboard(Turtle):
    def __init__(self, side):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        if side == 'left':
            self.goto(-200, 200)
        if side == 'right':
            self.goto(200, 200)
        self.score_update()

    def score_update(self):
        self.write(f'{self.score}', align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.score_update()
