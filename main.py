from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
ball = Ball()

# set the screen
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("github.com/mattbobea")


# creates starting paddles
STARTING_POSITION1 = (-350, 0)
STARTING_POSITION2 = (350, 0)
screen.tracer(0)
l_paddle = Paddle(STARTING_POSITION1)
r_paddle = Paddle(STARTING_POSITION2)
screen.listen()

scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    ball.bounce_y()
    l_paddle.l_move()
    r_paddle.r_move()
    
    # detect collision with right paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or\
            ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() >= 380:
        scoreboard.l_score += 1
        scoreboard.update_scoreboard()
        ball.reset_position()

    if ball.xcor() <= -380:
        scoreboard.r_score += 1
        scoreboard.update_scoreboard()
        ball.reset_position()

screen.exitonclick()
