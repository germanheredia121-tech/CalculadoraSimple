import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Calculadora")
root.geometry("300x500")
root.resizable(False, False)

color_texto = "#000000"
color_boton = "#E0E0E0"
color_boton_igual = "#FFA500"
color_boton_clear = "#FF4500"

screen_text = tk.StringVar()
screen_label = tk.Label(root, textvariable=screen_text, font=("Arial", 24), bg="#FFFFFF", fg=color_texto, anchor='e', relief='sunken', bd=2)
screen_label.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)

expression = ""

def press(num):
    global expression
    expression += str(num)
    screen_text.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        screen_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Expression")
        expression = ""
        screen_text.set("")
def clear():
    global expression
    expression = ""
    screen_text.set("")

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0) ]
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), bg=color_boton, fg=color_texto, command=lambda t=text: press(t))
    button.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
equal_button = tk.Button(root, text='=', font=("Arial", 18), bg=color_boton_igual, fg=color_texto, command=equalpress)
equal_button.grid(row=4, column=2, sticky="nsew", padx=2, pady=2)

clear_button = tk.Button(root, text='C', font=("Arial", 18), bg=color_boton_clear, fg=color_texto, command=clear)
clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
root.mainloop()