from tkinter import *

def btn_click(item):
    global expression
    try:
        input_field['state'] = "normal"

        if expression and expression[-1] == '=':
            expression = expression[:-1]

        expression += item
        input_field.delete(0, END)
        input_field.insert(END, expression)

        if item == '=':
            result = str(eval(expression[:-1]))
            input_field.delete(0, END)
            input_field.insert(END, result)
            expression = result + "="

        input_field['state'] = "readonly"
    except (ZeroDivisionError, SyntaxError):
        handle_error('Помилка')

def bt_clear():
    global expression
    expression = ""
    input_field['state'] = "normal"
    input_field.delete(0, END)
    input_field['state'] = "readonly"

def handle_error(error_msg):
    input_field.delete(0, END)
    input_field.insert(0, error_msg)

root = Tk()
root.geometry("268x288")
root.title("Калькулятор")
root.resizable(0, 0)

frame_input = Frame(root)
frame_input.grid(row=0, column=0, columnspan=4, sticky="nsew")

input_field = Entry(frame_input, font='Arial 15 bold', width=24, state="readonly")
input_field.pack(fill=BOTH)

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('0', '.', '=', '+', '4')
           )

expression = ""

button = Button(root, text='C', command=bt_clear)
button.grid(row=1, column=3, sticky="nsew")

for row in range(4):
    for col in range(4):
        Button(root, width=2, height=3, text=buttons[row][col],
               command=lambda r=row, c=col: btn_click(buttons[r][c])).grid(row=row + 2, column=col, sticky="nsew", padx=1, pady=1)

root.mainloop()
