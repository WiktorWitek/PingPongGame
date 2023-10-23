from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,x, y):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=x, y=y)
        self.update_scoreboard()

    def increase(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=('Arial', 24, 'normal'))