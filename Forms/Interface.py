from tkinter import *

# Ref: javatpoint.com/simple-registration-form-using-tkinter-in-python


base = Tk()
base.geometry('500x500')
base.title('Submit Form')

labl_0 = Label(base, text="Submit Form", width = 20, font = ("bold", 20))
labl_0.place(x=90, y=53)



labl_1 = Label(base, text = "Staff Name", width = 20, font = ("bold", 10))
labl_1.place(x = 80, y = 130)

entry_1 = Entry(base)
entry_1.place(x = 240, y = 130)


labl_2 = Label(base, text = "Staff Id", width = 20, font = ("bold", 10))
labl_2.place(x = 90, y = 180)

entry_2 = Entry(base)
entry_2.place(x = 240, y = 180)


# Radiobutton code
# labl_2a = Label(base, text="Gender", width=20, font=("bold", 10))
# labl_2a.place(x=80, y=230)
# varblbl = IntVar()
# Radiobutton(base, text="Male", padx=5, variable=varblbl, value=1).place(x=235, y=230)
# Radiobutton(base, text="Female", padx=20, variable=varblbl, value=2).place(x=290, y=230)


labl_3 = Label(base, text = "Email", width = 20, font = ("bold", 10))
labl_3.place(x = 94, y = 230)

entry_3 = Entry(base)
entry_3.place(x = 240, y = 230)


labl_4 = Label(base, text = "Description", width = 20, font = ("bold", 10))
labl_4.place(x = 80, y = 280)

entry_4 = Entry(base, width=40)
entry_4.place(x = 240, y = 280)


labl_5 = Label(base, text = "Response", width = 20, font = ("bold", 10))
labl_5.place(x = 84, y = 330)

entry_5 = Entry(base, text = "to be entered")
entry_5.place(x = 240, y = 330)


# labl_6 = Label(base, text = "status", width = 20, font = ("bold", 10))
# labl_6.place(x = 80, y = 130)

# entry_6 = Entry(base)
# entry_6.place(x = 240, y = 130)

Button(base, text = "Submit", width = 20, bg = "brown", fg = "white").place(x = 180, y = 380)

base.mainloop()

print("Your ticket has been added")


