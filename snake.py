import turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.snake_body = []
        self.snake()
        self.head = self.snake_body[0]

    def snake(self):
        for turtles in STARTING_POSITIONS:
            self.add_segments(turtles)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(5000, 5000)
        self.snake_body.clear()
        self.snake()
        self.head = self.snake_body[0]

    def add_segments(self, position):
        turt = turtle.Turtle(shape="square")
        turt.color("white")
        turt.penup()
        turt.goto(position)
        self.snake_body.append(turt)
        turtle.Screen().update()

    def snake_increase(self):
        self.add_segments(self.snake_body[-1].position())

    def move(self):
        for body_seg in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[body_seg].goto(self.snake_body[body_seg - 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left_side(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right_side(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
