import turtle

class MyTurtle(turtle.Turtle):
    def grow(self):
        w, l, o = self.shapesize()
        self.shapesize(w + 0.5, l + 0.5)

t = MyTurtle()
t.shape("turtle")
t.color("green")

for _ in range(5):
    t.grow()
    t.forward(50)

turtle.done()