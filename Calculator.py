# Calculator App
import tkinter

# create the application window
window = tkinter.Tk()

# Set application windows name and size
window.title("Basic Calculator")
window.geometry('315x450')

# Putting the number in the entry window
number_entry = tkinter.Entry(window, width=20, borderwidth=3)
number_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_neg():
    return

def button_percent():
    return

def button_decimal():
    return

def button_sub():
    first_number = int(number_entry.get())
    global math
    global first_num
    math = 'subtraction'
    first_num = int(first_number)
    number_entry.delete(0, 'end')
    return

def button_mult():
    first_number = int(number_entry.get())
    global math
    global first_num
    math = 'multiply'
    first_num = int(first_number)
    number_entry.delete(0, 'end')
    return

def button_divide():
    first_number = int(number_entry.get())
    global first_num
    global math
    math = 'divide'
    first_num = int(first_number)
    number_entry.delete(0, 'end')
    return

def button_equal():
    number_entry.delete(0, 'end')
    total = 0
    if math == 'addition':
        for ele in range(0, len(list_num)):
            total = total + list_num[ele]
            number_entry.insert(0, total)
    if math == 'subtraction':
        number_entry.insert(0, first_num )
    if math == 'multiply':
        number_entry.insert(0, first_num )
    if math == 'divide':
        number_entry.insert(0, first_num )
    return

def button_add():
    num = int(number_entry.get())
    global list_num
    global math
    math = 'addition'
    list_num = list_num.append(num)
    print(list_num)
    return

def button_clear():
    number_entry.delete(0, 'end')
    return

def button_click(number):
    current = number_entry.get()
    number_entry.delete(0, 'end')
    number_entry.insert(0, str(current) + str(number))
    return

# define buttons
# Number Buttons
btn_1 = tkinter.Button(window, text="1", padx=30, pady=30, command=lambda: button_click(1))
btn_2 = tkinter.Button(window, text="2", padx=30, pady=30, command=lambda: button_click(2))
btn_3 = tkinter.Button(window, text="3", padx=30, pady=30, command=lambda: button_click(3))
btn_4 = tkinter.Button(window, text="4", padx=30, pady=30, command=lambda: button_click(4))
btn_5 = tkinter.Button(window, text="5", padx=30, pady=30, command=lambda: button_click(5))
btn_6 = tkinter.Button(window, text="6", padx=30, pady=30, command=lambda: button_click(6))
btn_7 = tkinter.Button(window, text="7", padx=30, pady=30, command=lambda: button_click(7))
btn_8 = tkinter.Button(window, text="8", padx=30, pady=30, command=lambda: button_click(8))
btn_9 = tkinter.Button(window, text="9", padx=30, pady=30, command=lambda: button_click(9))
btn_0 = tkinter.Button(window, text="0", padx=68, pady=30, command=lambda: button_click(0))

# Decimal Button
btn_decimal = tkinter.Button(window, text=".", padx=32, pady=30, command=button_decimal)

# Sign Buttons
btn_mult = tkinter.Button(window, text='X', padx=30, pady=30, command=button_mult)
btn_sub = tkinter.Button(window, text='-', padx=30, pady=30, command=button_sub)
btn_add = tkinter.Button(window, text='+', padx=30, pady=30, command=button_add)
btn_equal = tkinter.Button(window, text='=', padx=30, pady=30, command=button_equal)

btn_clear = tkinter.Button(window, text='AC', padx=25, pady=25, command=button_clear)
btn_neg = tkinter.Button(window, text='Neg', padx=22, pady=25, command=button_neg)
btn_percent = tkinter.Button(window, text='%', padx=28, pady=25, command=button_percent)
btn_divide = tkinter.Button(window, text='/', padx=32, pady=25, command=button_divide)

# Drawing the buttons
# Last Row
btn_0.grid(row=5, column=0, columnspan=2)
btn_decimal.grid(row=5, column=2)
btn_equal.grid(row=5, column=3)

# Forth Row
btn_1.grid(row=4, column=0)
btn_2.grid(row=4, column=1)
btn_3.grid(row=4, column=2)
btn_add.grid(row=4, column=3)

# Third Row
btn_4.grid(row=3, column=0)
btn_5.grid(row=3, column=1)
btn_6.grid(row=3, column=2)
btn_sub.grid(row=3, column=3)

# Second Row
btn_7.grid(row=2, column=0)
btn_8.grid(row=2, column=1)
btn_9.grid(row=2, column=2)
btn_mult.grid(row=2, column=3)

# First Row
btn_clear.grid(row=1, column=0)
btn_neg.grid(row=1, column=1)
btn_percent.grid(row=1, column=2)
btn_divide.grid(row=1, column=3)

# call to the window
window.mainloop()