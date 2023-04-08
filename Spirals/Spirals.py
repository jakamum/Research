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
        canvas.create_text(x1, y1, text=char, fill="red", font=(font_type, font_size))
    radius += 0.3
    return radius

root = tk.Tk()
root.geometry("800x800")
root.title("Animated Expanding Text")

canvas = tk.Canvas(root, width=800, height=800)
canvas.pack()

texts = [("God is love", 200, 400), ("the way the truth and the life", 600, 400)]
start_angles = [0, 0.001]
font_size = 30
font_type = "Opus Special Extra Std"
radii = [0, 0]

while True:
    canvas.delete("all")
    for i, (text, x, y) in enumerate(texts):
        radii[i] = spiral_text(canvas, text, x, y, radii[i], start_angles[i], font_size, font_type)
        start_angles[i] += 0.001
        x += math.cos(start_angles[i]) * radii[i] / 50
        y += math.sin(start_angles[i]) * radii[i] / 50
        time.sleep(0)

        root.update()

root.mainloop()
