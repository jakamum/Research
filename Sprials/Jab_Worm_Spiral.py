import tkinter as tk
import math
import time

def spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type):
    angle = start_angle
    step = 0.05
    for char in text:
        x1 = x + math.cos(angle) * radius
        y1 = y + math.sin(angle) * radius
        canvas.create_text(x1, y1, text=char, font=(font_type, font_size))
        angle += step
        radius += 0.4

root = tk.Tk()
root.geometry("800x800")
root.title("Animated Spiraling Text Worm")

canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

text = "’Twas brillig, and the slithy toves"
text += "\nDid gyre and gimble in the wabe;"
x, y = 400, 400
radius = 0
start_angle = 0
font_size = 20
font_type = "Helvetica"

while True:
    canvas.delete("all")
    spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type)
    start_angle += 0.05
    time.sleep(0.01)
    root.update()

root.mainloop()
