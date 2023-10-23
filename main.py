from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.update()
screen.tracer(1)

ball = Ball()
r_score = Scoreboard(-300, 250)
l_score = Scoreboard(300, 250)

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")



is_on = True
while is_on:
    time.sleep(ball.speed)
    ball.move()
    """top and bottom walls colision"""
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    """colision with paddle"""
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50 or ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.paddle_bounce()




    """right paddle score"""
    if ball.xcor() > 380:
        r_score.increase()
        screen.tracer(0)
        ball.reset_position()
        screen.update()
        screen.tracer(1)
        ball.speed = 0.01

    """left paddle score"""
    if ball.xcor() < -380:
        l_score.increase()
        screen.tracer(0)
        ball.reset_position()
        screen.update()
        screen.tracer(1)
        ball.speed = 0.01

screen.exitonclick()