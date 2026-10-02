from turtle import Turtle

MOVE_DISTANCE = 10

class Ball(Turtle):
    """Creates ball for the Pong Game"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)

    def move(self):
        """Moved the ball on the screen"""
        new_x = self.xcor() + MOVE_DISTANCE
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(new_x,new_y)