import turtle
import random

# generate random position



class Shape:
    def __init__(self, sides, length, color):
        self.sides = sides
        self.length = length
        self.color = color
        self.t = turtle.Turtle()

    def draw(self):
        self.t.pencolor(self.color)
        for _ in range(self.sides):
            self.t.forward(self.length)
            self.t.right(360 / self.sides)

class Square(Shape):
    def __init__(self, length, color):
        super().__init__(4, length, color)

class Triangle(Shape):
    def __init__(self, length, color):
        super().__init__(3, length, color)

class Pentagon(Shape):
    def __init__(self, length, color):
        super().__init__(5, length, color)

def main():
    turtle.speed(0)
    turtle.bgcolor("black")

    square = Square(100, "red")

    triangle = Triangle(100, "white")

    pentagon = Pentagon(100, "blue")


    for i in range(5):

        square.draw()
        square.length = square.length + 10

    for i in range(5):

        triangle.draw()
        triangle.length = triangle.length + 10

    for i in range(5):

        pentagon.draw()
        pentagon.length = pentagon.length + 10


    turtle.done()

if __name__ == "__main__":
    main()