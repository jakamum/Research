import tkinter as tk
import math

# from Chat GBT 
# create class
class SpiralText:
    def __init__(self, canvas, x, y, text, font, color, radius, speed):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.color = color
        self.radius = radius
        self.speed = speed
        self.angle = 0
        self.id = None

    def update(self):
        self.angle += self.speed
        x = self.x + math.cos(self.angle) * self.radius
        y = self.y + math.sin(self.angle) * self.radius
        if self.id is not None:
            self.canvas.delete(self.id)
        self.id = self.canvas.create_text(x, y, text=self.text, font=self.font, fill=self.color)

root = tk.Tk()
root.title("Circling Words")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create two spiraling text objects with different parameters - like size of font, radius of travelling circle and speed of travel
text1 = SpiralText(canvas, 200, 200, "Hello, world!", ("Helvetica", 12), "red", 50, 0.1)
text2 = SpiralText(canvas, 200, 200, "Goodbye, world!", ("Arial", 14), "blue", 100, -0.05)

# Update the text objects on every frame
def update():
    text1.update()
    text2.update()
    canvas.after(10, update)

update()
root.mainloop()
