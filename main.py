import tkinter as tk
from math import *

def clear():
    label.config(text="")

def press_number(number):
    current=label["text"]
    label.config(text=current+number)


def evaluate():
    try:
        result = eval(label["text"],globals())
        label.config(text=str(result))
    except ZeroDivisionError:
        label.config(text="Error: ÷0")
    except Exception:
        label.config(text="Error")





root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="lightblue")

label = tk.Label(root, text="", height=2, font=("Arial", 16))
label.grid(row=0, column=0, columnspan=4, sticky="nsew")


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), ("C", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("pi", 5, 0), ("e", 5, 1), ("sin", 5, 2), ("cos", 5, 3),
    ("(", 7, 0), (")", 7, 1), ("%", 7, 2),
]

for (text, row, col) in buttons:
    if text == "C":
        action = clear
    elif text == "=":
        action = evaluate
    else:
        action = lambda t=text: press_number(t)

    tk.Button(root, text=text, width=5, height=2, command=action).grid(row=row, column=col)


root.mainloop()