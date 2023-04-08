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
    # square.draw()

    triangle = Triangle(100, "white")
    # triangle.draw()

    pentagon = Pentagon(100, "blue")
    # pentagon.draw()

    # for i in range(1):
    #     x = random.randint(-200, 200)
    #     y = random.randint(-200, 200)

    #     square.t.right(random. randint(0,360))
    #     square.t.goto(x,y)
    #     square.draw()

    #     triangle.t.right(random. randint(0,360))
        # triangle.t.penup()
        # triangle.t.goto(x,y)
        # triangle.t.pendown()
    #
    #     triangle.draw()

    #     pentagon.t.right(random. randint(0,360))
    #     pentagon.t.goto(x,y)
    #     pentagon.draw()

    # for i in range(1):
    #     x = random.randint(-200, 200)
    #     y = random.randint(-200, 200)

    #     square = Square(150, "green")
    #     square.t.left(150)
    #     square.t.goto(x, y)
    #     square.draw()

    #     triangle = Triangle(150, "red")
    #     triangle.t.left(150)
    #     triangle.t.goto(x, y)
    #     triangle.draw()

    #     pentagon = Pentagon(150, "blue")
    #     pentagon.t.left(150)
    #     pentagon.t.goto(x, y)
    #     pentagon.draw()
  
    for i in range(5):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        angle = random.randint(1,360)
        for i in range(5):
            square.draw()
            # square.t.left(200)

            square.length = square.length + 10

        for i in range(5):
            # x = random.randint(-200, 200)
            # y = random.randint(-200, 200)

            triangle.draw()
            # triangle.t.left(200)

            triangle.length = triangle.length + 10

        for i in range(5):
            # x = random.randint(-200, 200)
            # y = random.randint(-200, 200)

            pentagon.draw()
            # pentagon.t.left(200)

            pentagon.length = pentagon.length + 10

        square.t.goto(x, y)
        square.t.right(angle)
        triangle.t.goto(x, y)
        triangle.t.right(angle)
        pentagon.t.goto(x, y)
        pentagon.t.right(angle)



#     import turtle

# # create turtle and draw first shape
# t = turtle.Turtle()
# t.speed(0)
# t.penup()
# t.goto(100, 100)
# t.pendown()
# for i in range(4):
#     t.forward(50)
#     t.left(90)

# # get position of first shape and set position of second shape
# x, y = t.pos()
# t.penup()
# t.goto(x, y)
# t.pendown()
# for i in range(3):
#     t.forward(50)
#     t.left(120)

# keep the turtle window open until it is manually closed
# turtle.done()


    turtle.done()

if __name__ == "__main__":
    main()