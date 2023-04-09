import tkinter as tk
#import tkinter.ttk as ttk

window = tk.Tk()

greeting = tk.Label(text="Welcome to the Tkinter Experiment!")
greeting.pack()

label = tk.Label(
    text="Name",
    #fg="white",  # Set the text color to white
    bg="lightblue",  # Set the background color to purple
    width = 10,
    height= 1
)
entry1 = tk.Entry()
# entry = tk.Entry(fg="yellow", bg="blue", width=50)

# name

label.pack()
entry1.pack()


# def onEntryRemove():
#     entry1.delete(0, tk.END)

def onButtonClick():
    name = entry1.get()
    entry1.insert(0, "Real ")
    #entry1.delete(0, tk.END)

button = tk.Button(
    text="Click me!",
    width=25,
    height=2,
    bg="pink",
    fg="white",
    command=onButtonClick
)
button.pack()

#window.destroy()

window.mainloop()





