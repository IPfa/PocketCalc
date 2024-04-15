import operator
import tkinter as tk


OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
ADDITION = "+"
SUBSTRACTION = "-"
MULTIPLICATION = "*"
DIVIDION = "/"
ERROR = "Error!"
MINUS = "-"
POINT = "."


def string_to_task(string):
    string_to_list = string.split(" ")
    task = []
    for i in string_to_list:
        item = i.replace(MINUS, "").replace(".", "")
        if item.isdigit():
            task.append(float(i))
        else:
            task.append(i)
    return task


def calculate_and_remove(result, operator):
    position = result.index(operator)
    arg_1 = result[position - 1]
    arg_2 = result[position + 1]
    if arg_2 == 0 and operator == DIVIDION:
        result = ERROR
        return result
    calculation_result = OPERATORS[operator](arg_1, arg_2)
    result.pop(position)
    result.insert(position, calculation_result)
    result.pop(position + 1)
    result.pop(position - 1)
    return result


def evaluate():
    result = string_to_task(text.get())
    while True:
        for i in range(0, len(result)):
            if result[i] == MULTIPLICATION:
                result = calculate_and_remove(result, MULTIPLICATION)
                break
            elif result[i] == DIVIDION:
                result = calculate_and_remove(result, DIVIDION)
                if result == ERROR:
                    text.set(ERROR)
                break
        if MULTIPLICATION not in result and DIVIDION not in result:
            break
    while True:
        for i in range(0, len(result)):
            if result[i] == ADDITION:
                result = calculate_and_remove(result, ADDITION)
                break
            elif result[i] == SUBSTRACTION:
                result = calculate_and_remove(result, SUBSTRACTION)
                break
        if ADDITION not in result and SUBSTRACTION not in result:
            break
    if result[0].is_integer():
        result = int(result[0])
    else:
        result = round(result[0], 4)
    text.set(result)


def clear():
    text.set("")


def set_plus_minus():
    current_value = text.get()
    new_value = current_value + MINUS
    if current_value != "":
        if current_value[len(current_value) - 1] == MINUS:
            new_value = current_value[0: len(current_value) - 1]
    text.set(new_value)


def set_point():
    current_value = text.get()
    new_value = current_value + POINT
    if current_value != "":
        if current_value[len(current_value) - 1] == POINT:
            new_value = current_value[0: len(current_value) - 1]
    text.set(new_value)


def lenght_control(*args):
    current_value = text.get()
    if len(current_value) >= 25:
        text.set(ERROR)


def set_value(button_pressed):
    global NEW_CALCULATION_FLAG
    current_value = text.get()
    if current_value == ERROR:
        text.set(ERROR)
    else:
        pressed_button_value = globals()[button_pressed].cget("text")
        if pressed_button_value in ("+", "-", "*", "/"):
            pressed_button_value = f' {pressed_button_value} '
        new_value = current_value + pressed_button_value
        text.set(new_value)


window = tk.Tk()
window.title("Calculator")
window.geometry("201x190")


text = tk.StringVar()
text.trace("w", lenght_control)

entry = tk.Entry(
    window,
    width=20,
    disabledbackground="white",
    disabledforeground="black",
    font=('Arial', 15),
    textvariable=text
)
entry.config(state=tk.DISABLED)
entry.place(x=1, y=5)


button_1 = tk.Button(
    window,
    width=1,
    text="1",
    command=lambda: set_value("button_1")
)
button_1.place(x=1, y=35)
button_2 = tk.Button(
    window,
    width=1,
    text="2",
    command=lambda: set_value("button_2")
)
button_2.place(x=49, y=35)
button_3 = tk.Button(
    window,
    width=1,
    text="3",
    command=lambda: set_value("button_3")
)
button_3.place(x=96, y=35)
button_4 = tk.Button(
    window,
    width=1,
    text="4",
    command=lambda: set_value("button_4")
)
button_4.place(x=1, y=65)
button_5 = tk.Button(
    window,
    width=1,
    text="5",
    command=lambda: set_value("button_5")
)
button_5.place(x=49, y=65)
button_6 = tk.Button(
    window,
    width=1,
    text="6",
    command=lambda: set_value("button_6")
)
button_6.place(x=96, y=65)
button_7 = tk.Button(
    window,
    width=1,
    text="7",
    command=lambda: set_value("button_7")
)
button_7.place(x=1, y=95)
button_8 = tk.Button(
    window,
    width=1,
    text="8",
    command=lambda: set_value("button_8")
)
button_8.place(x=49, y=95)
button_9 = tk.Button(
    window,
    width=1,
    text="9",
    command=lambda: set_value("button_9")
)
button_9.place(x=96, y=95)
button_0 = tk.Button(
    window,
    width=1,
    text="0",
    command=lambda: set_value("button_0")
)
button_0.place(x=49, y=125)
button_point = tk.Button(
    window,
    width=1,
    text=".",
    command=set_point
)
button_point.place(x=1, y=125)
button_clear = tk.Button(
    window,
    width=1,
    text="C",
    command=clear
)
button_clear.place(x=96, y=125)
button_sign = tk.Button(
    window,
    width=7,
    text="+/-",
    command=set_plus_minus
)
button_sign.place(x=1, y=155)
button_calculate = tk.Button(
    window,
    width=7,
    text="=",
    command=evaluate
)
button_calculate.place(x=97, y=155)
button_addition = tk.Button(
    window,
    width=2,
    text="+",
    command=lambda: set_value("button_addition")
)
button_addition.place(x=141, y=35)
button_substraction = tk.Button(
    window,
    width=2,
    text="-",
    command=lambda: set_value("button_substraction")
)
button_substraction.place(x=141, y=65)
button_multiplication = tk.Button(
    window,
    width=2,
    text="*",
    command=lambda: set_value("button_multiplication")
)
button_multiplication.place(x=141, y=95)
button_dividion = tk.Button(
    window,
    width=2,
    text="/",
    command=lambda: set_value("button_dividion")
)
button_dividion.place(x=141, y=125)


window.mainloop()
