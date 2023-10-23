from turtle import Turtle



class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.goto(position)
        self.setheading(90)


    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(x=self.xcor(), y=new_y)


    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(x=self.xcor(), y=new_y)

