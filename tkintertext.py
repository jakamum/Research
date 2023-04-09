import tkinter as tk

window = tk.Tk()
text_box = tk.Text()
text_box.pack()
#text_box.get("1.0", "1.5")
def onButtonClick():
    text_box.delete("1.0", "1.5")
    text_box.delete("1.0")
    #text_box.insert(0, "Real ")
    #text_box.delete(0, tk.END)

button = tk.Button(
    text="Click me!",
    width=25,
    height=2,
    bg="pink",
    fg="white",
    command=onButtonClick
)
button.pack()



window.mainloop()