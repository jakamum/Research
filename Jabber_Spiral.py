import tkinter as tk
import math
import time

def spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type):
    angle = start_angle
    golden_ratio = (1 + math.sqrt(5)) / 2 # golden ratio constant
    for i, char in enumerate(text):
        char_angle = i * golden_ratio
        char_radius = radius * math.sqrt(i)
        x1 = x + math.cos(angle + char_angle) * char_radius
        y1 = y + math.sin(angle + char_angle) * char_radius
        canvas.create_text(x1, y1, text=char, font=(font_type, font_size))
    radius += 30
    return radius

root = tk.Tk()
root.geometry("800x800")
root.title("Animated Spiraling Text")

canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

text ="’Twas brillig, and the slithy toves did gyre and gimble in the wabe...."
x, y = 400, 400
radius = 0
start_angle = 0
font_size = 20
font_type = "Helvetica"

while True:
    canvas.delete("all")
    radius = spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type)
    start_angle += 0.01
    x += math.cos(start_angle) * radius / 30
    y += math.sin(start_angle) * radius / 30
    time.sleep(0.75)
    root.update()

root.mainloop()


