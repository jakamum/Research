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

    def randanglepos(shape):
            x = random.randint(-200, 200)
            y = random.randint(-200, 200)
            angle = random.randint(1,360)
            shape.t.penup()
            shape.t.goto(x,y)
            shape.t.pendown()
            shape.draw()
            shape.length = shape.length + 10
            shape.t.left(angle)


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

    square = Square(100, "blue")

    triangle = Triangle(100, "green")

    pentagon = Pentagon(100, "purple")

    # for i in range(2):
    for i in range(5):
        Square.randanglepos(square)

    triangle.t.right(180)

    for i in range(5):
        Triangle.randanglepos(triangle)

    pentagon.t.left(180)

    for i in range(5):
        Pentagon.randanglepos(pentagon)

    turtle.done()

if __name__ == "__main__":
    main()