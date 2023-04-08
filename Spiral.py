import tkinter as tk
import math
import time

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

    def spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type):
        angle = start_angle
        golden_ratio = (1 + math.sqrt(5)) / 2 # golden ratio constant
        for i, char in enumerate(text):
            char_angle = i * golden_ratio
            char_radius = radius * math.sqrt(i)
            x1 = x + math.cos(angle + char_angle) * char_radius
            y1 = y + math.sin(angle + char_angle) * char_radius
            canvas.create_text(x1, y1, text=char, fill="purple", font=(font_type, font_size))
        radius += 0.3
        return radius

root = tk.Tk()
root.geometry("800x800")
root.title("Animated Spiraling Text")

canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

text = "God is love"
x, y = 200, 400
radius = 0
start_angle = 0
font_size = 30
font_type = "Opus Special Extra Std"

# Create two spiraling text objects with different parameters
text1 = SpiralText(canvas, 200, 400, "God is Love", ("Opus Special Extra Std", 12), "red", 50, 0.05)
text2 = SpiralText(canvas, 200, 200, "I am the way, the truth and the life", ("Opus Special Extra Std", 14), "blue", 100, -0.05)

# Update the text objects on every frame
def update():
    text1.update()
    text2.update()
    canvas.after(10, update)

while True:
    canvas.delete("all")
    SpiralText.spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type)
    radius = SpiralText.spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type)
    start_angle += 0.1
    x += math.cos(start_angle) * radius / 100
    y += math.sin(start_angle) * radius / 100
    time.sleep(0.01)
    root.update()

    # while True:
    #     canvas.delete("all")
    #     SpiralText.spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type)
    #     radius = SpiralText.spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type)
    #     start_angle += 0.1
    #     x += math.cos(start_angle) * radius / 100
    #     y += math.sin(start_angle) * radius / 100
    #     time.sleep(0.01)
    #     root.update()

    update()
    root.mainloop()




root.mainloop()