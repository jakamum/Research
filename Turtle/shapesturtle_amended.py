import turtle
import random

# generate random position


# create abstract class 'Shape'
class Shape:
    def __init__(self, sides, length, color):
        self.sides = sides
        self.length = length
        self.color = color
        self.t = turtle.Turtle()

    #draw method    
    def draw(self):
        self.t.pencolor(self.color)
        for _ in range(self.sides):
            self.t.forward(self.length)
            self.t.right(360 / self.sides)

# create class 'Square', child of 'Shape'
class Square(Shape):
    def __init__(self, length, color):
        super().__init__(4, length, color)

# create class 'Triangle', child of 'Shape'        
class Triangle(Shape):
    def __init__(self, length, color):
        super().__init__(3, length, color)

# create class 'Pentagon', child of 'Shape'           
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

    # for loop to randomly position each completed iteration of the shapes
    for i in range(5):
        x = random.randint(-400, 400)
        y = random.randint(-400, 400)
        angle = random.randint(1,360)
        
        # iteration of 5 squares increasing in size each time
        for i in range(5):
            square.draw()
            # square.t.left(200)

            square.length = square.length + 10

        # iteration of 5 triangles increasing in size each time    
        for i in range(5):

            triangle.draw()
            triangle.length = triangle.length + 10

        # iteration of 5 pentagons increasing in size each time
        for i in range(5):

            pentagon.draw()
            pentagon.length = pentagon.length + 10

        #send shapes to the randomly selected coordinates for x and y
        square.t.goto(x, y)
        square.t.right(angle)
        triangle.t.goto(x, y)
        triangle.t.right(angle)
        pentagon.t.goto(x, y)
        pentagon.t.right(angle)


    turtle.done()

if __name__ == "__main__":
    main()
