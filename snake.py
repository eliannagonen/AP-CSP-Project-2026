import turtle
import random
import time

class Snake:
    def __init__(self, head_color, body_color, x, y):
        self.head_color = head_color
        self.body_color = body_color
        self.x = x
        self.y = y
        self.direction = "right"

    def draw(self):
        t = turtle.Turtle()
        t.penup()
        t.goto(self.x * 20 - 190, self.y * 20 - 190)
        t.shape("square")
        t.color(self.head_color)
        t.stamp()
