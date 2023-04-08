import turtle

# def drawCircle(radius,iterations, t): # returns tuples 
#      coords = [] 
#      for i in range(iterations): 
#           t.forward(radius) 
#           t.right(360.0/iterations) 
#           coords.append((t.xcor(), t.ycor()))
#      return tuple(coords)

# t = turtle.Turtle()
# screen = turtle.Screen()
# screen.register_shape('myCircle', drawCircle(1, 72, t))

# t.shape('myCircle')

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


class Pentagon(Shape):
    def __init__(self, length, color):
        super().__init__(5, length, color)

    def draw_pentagon():
        pentagon = Pentagon(100, "pink")
        pentagon.t.penup()
        pentagon.t.goto(0, 0)
        pentagon.t.pendown()
        pentagon.draw()


def main():
    turtle.speed(0)
    turtle.bgcolor("blue")


    #for i in range(9):
    Pentagon.draw_pentagon()

    Pentagon.forward(150)

    for i in range(3):
        for i in range(9):
            Pentagon.draw_pentagon()
        Pentagon.left(90)
        Pentagon.forward(150)

    # for i in range(3):
    #     for i in range(9):
    #         Pentagon.draw_pentagon()
    #     Pentagon.left(90)
    #     Pentagon.forward(150)
    # Pentagon.turt()

        turtle.done()
 


if __name__ == "__main__":
    main()