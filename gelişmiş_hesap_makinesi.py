from tkinter import *
import math

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # create entry widget to display the result
        self.result = Entry(master, width=25, font=('Arial', 16))
        self.result.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # create buttons
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('C', 4, 2)
        self.create_button('+', 4, 3)

        self.create_button('(', 5, 0)
        self.create_button(')', 5, 1)
        self.create_button('x^y', 5, 2)
        self.create_button('=', 5, 3)

        self.create_button('√', 6, 0)
        self.create_button('%', 6, 1)

    # function to create button
    def create_button(self, text, row, column):
        button = Button(self.master, text=text, width=5, height=2, font=('Arial', 14), command=lambda: self.click(text))
        button.grid(row=row, column=column, padx=2, pady=2)

    # function to handle button click
    def click(self, text):
        if text == '=':
            result = eval(self.result.get())
            self.result.delete(0, END)
            self.result.insert(0, str(result))
        elif text == 'C':
            self.result.delete(0, END)
        elif text == 'x^y':
            self.result.insert(END, '**')
        elif text == '√':
            result = math.sqrt(float(self.result.get()))
            self.result.delete(0, END)
            self.result.insert(0, str(result))
        elif text == '%':
            result = float(self.result.get())/100
            self.result.delete(0, END)
            self.result.insert(0, str(result))
        else:
            self.result.insert(END, text)

root = Tk()
calculator = Calculator(root)
root.mainloop()

