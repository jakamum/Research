# import syntax 1 bring it all
from turtle import*

delay(.9)

def draw_star():
    forward(100)
    left(150)
    forward(100)
    left(100)
    forward(50)
    left(200)
    left(350)

for i in range(9):
    draw_star()

forward(150)

for i in range(3):
    for i in range(9):
        draw_star()
    left(90)
    forward(150)

# draw_square()
# left(90)
# draw_square()
if __name__=="main":
    exitonclick()

author = "Jacqui"
print(author)

