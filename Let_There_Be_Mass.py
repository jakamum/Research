import tkinter as tk
import math
import time


# def spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type):
#     # Set the initial angle
#     angle = start_angle
    
#     # Calculate the golden ratio constant
#     golden_ratio = (1 + math.sqrt(5)) / 2
    
#     # Loop through each character in the text
#     for i, char in enumerate(text):
#         # Calculate the angle for the current character
#         char_angle = i * golden_ratio
        
#         # Calculate the radius for the current character
#         char_radius = radius * math.sqrt(i)
        
#         # Calculate the x and y coordinates for the current character
#         x1 = x + math.cos(angle + char_angle) * char_radius
#         y1 = y + math.sin(angle + char_angle) * char_radius
        
#         # Create a text object for the current character
#         canvas.create_text(x1, y1, text=char, fill="red", font=(font_type, font_size))
        
#     # Increase the radius for the next spiral
#     radius += 0.3
    
#     # Return the new radius value
#     return radius


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

def spiral_text1(canvas, text1, x, y, radius, start_angle, font_size, font_type):
    angle = start_angle
    golden_ratio = (1 + math.sqrt(5)) / 2 # golden ratio constant
    for i, char in enumerate(text1):
        char_angle = i * golden_ratio
        char_radius = radius * math.sqrt(i)
        x1 = x + math.cos(angle + char_angle) * char_radius
        y1 = y + math.sin(angle + char_angle) * char_radius
        canvas.create_text(x1, y1, text=char, fill="orange", font=(font_type, font_size))
    radius += 0.3
    return radius

def spiral_text3(canvas, text3, x, y, radius, start_angle, font_size, font_type):
    angle = start_angle
    golden_ratio = -(1 + math.sqrt(5)) / 2 # golden ratio constant
    for i, char in enumerate(text3):
        char_angle = i * golden_ratio
        char_radius = radius * math.sqrt(i)
        x1 = x + math.cos(angle - char_angle) * char_radius
        y1 = y + math.sin(angle - char_angle) * char_radius
        canvas.create_text(x1, y1, text=char, fill="yellow", font=(font_type, font_size))
    radius += 0.3
    return radius

root = tk.Tk()
root.geometry("800x800")
root.title("Animated Expanding Text Mass")

canvas = tk.Canvas(root, width=800, height=800)
canvas.configure(bg='blue')
canvas.pack()

text = "God is love. Whoever lives in love lives in God, and God in him. In this way, love is made complete among us so that we will have confidence on the day of judgment, because in this world we are like him. There is no fear in love."
text1 = "Then God said, “Let there be light,” and there was light. And God saw that the light was good. Then he separated the light from the darkness."
text3 = "For God, who commanded the light to shine out of darkness, hath shined in our hearts, to give the light of the knowledge of the glory of God in the face of Jesus Christ."
x, y = 400, 300
radius = 0
start_angle = 0
font_size = 30
font_type = "Opus Special Extra Std"


while True:
    #canvas.delete("all")
    radius = spiral_text(canvas, text, x, y, radius, start_angle, font_size, font_type)
    start_angle += 0.1
    x += math.cos(start_angle) * radius / 100
    y += math.sin(start_angle) * radius / 100
    time.sleep(0.1)
    radius = spiral_text1(canvas, text1, x, y, radius, start_angle, font_size, font_type)
    start_angle += 0.02
    x += math.cos(start_angle) * radius / -300
    y += math.sin(start_angle) * radius / 300
    time.sleep(0.01)
    radius = spiral_text3(canvas, text, x, y, radius, start_angle, font_size, font_type)
    start_angle += 0.3
    x += math.cos(start_angle) * radius / 400
    y += math.sin(start_angle) * radius / 400
    time.sleep(0.01)
    root.update()

root.mainloop()
