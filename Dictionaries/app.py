from tkinter import *

def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(0, result)
    except:
        entry.delete(0, END)
        entry.insert(0, "Error")

root = Tk()
root.title("Calculator")
root.geometry("300x400")

entry = Entry(root, font=("Arial", 20), justify="right")
entry.pack(fill=BOTH, padx=10, pady=10)

frame = Frame(root)
frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row = 0
col = 0

for button in buttons:
    if button == "=":
        Button(frame, text=button, width=7, height=3,
               command=calculate).grid(row=row, column=col)
    else:
        Button(frame, text=button, width=7, height=3,
               command=lambda b=button: click(b)).grid(row=row, column=col)

    col += 1
    if col > 3:
        col = 0
        row += 1

Button(root, text="Clear", command=clear).pack(fill=BOTH, padx=10, pady=10)

root.mainloop()