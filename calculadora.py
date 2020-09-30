from tkinter import *

ventana = Tk()
ventana.title("Calculadoriux")

i = 0

#Input
e_text = Entry(ventana, font = ("Calibri 20"))
e_text.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady= 5)

#Functions

def button_click(value):
    global i
    e_text.insert(i, value)
    i += 1

def errase():
    e_text.delete(0, END)
    i = 0

def result(e_text):
    ecuacion = e_text.get()
    e_text.delete(0, END)
    e_text.insert(0, eval(ecuacion))

#Buttons
#button = Button(ventana, text = "", width = 5, height = 2)

button1 = Button(ventana, text = "1", width = 5, height = 2, command = lambda: button_click(1))
button2 = Button(ventana, text = "2", width = 5, height = 2, command = lambda: button_click(2))
button3 = Button(ventana, text = "3", width = 5, height = 2, command = lambda: button_click(3))
button4 = Button(ventana, text = "4", width = 5, height = 2, command = lambda: button_click(4))
button5 = Button(ventana, text = "5", width = 5, height = 2, command = lambda: button_click(5))
button6 = Button(ventana, text = "6", width = 5, height = 2, command = lambda: button_click(6))
button7 = Button(ventana, text = "7", width = 5, height = 2, command = lambda: button_click(7))
button8 = Button(ventana, text = "8", width = 5, height = 2, command = lambda: button_click(8))
button9 = Button(ventana, text = "9", width = 5, height = 2, command = lambda: button_click(9))
button0 = Button(ventana, text = "0", width = 16, height = 2, command = lambda: button_click(0))

button_errase = Button(ventana, text = "AC", width = 5, height = 2, command = lambda: errase())
button_parentesis1 = Button(ventana, text = "(", width = 5, height = 2, command = lambda: button_click("("))
button_parentesis2 = Button(ventana, text = ")", width = 5, height = 2, command = lambda: button_click(")"))

button_div_ = Button(ventana, text = "/", width = 5, height = 2, command = lambda: button_click("/"))
button_mul = Button(ventana, text = "*", width = 5, height = 2, command = lambda: button_click("*"))
button_sum = Button(ventana, text = "+", width = 5, height = 2, command = lambda: button_click("+"))
button_res = Button(ventana, text = "-", width = 5, height = 2, command = lambda: button_click("-"))
button_equal = Button(ventana, text = "=", width = 5, height = 2, command = lambda: result(e_text))
button_point = Button(ventana, text = ".", width = 5, height = 2, command = lambda: button_click("."))

#Adding buttons.

button_errase.grid(row = 1, column = 0, padx = 5, pady = 5)
button_parentesis1.grid(row = 1, column = 1, padx = 5, pady = 5)
button_parentesis2.grid(row = 1, column = 2, padx = 5, pady = 5)
button_div_.grid(row = 1, column = 3, padx = 5, pady = 5)

button7.grid(row = 2, column = 0, padx = 5, pady = 5)
button8.grid(row = 2, column = 1, padx = 5, pady = 5)
button9.grid(row = 2, column = 2, padx = 5, pady = 5)
button_mul.grid(row = 2, column = 3, padx = 5, pady = 5)

button4.grid(row = 3, column = 0, padx = 5, pady = 5)
button5.grid(row = 3, column = 1, padx = 5, pady = 5)
button6.grid(row = 3, column = 2, padx = 5, pady = 5)
button_sum.grid(row = 3, column = 3, padx = 5, pady = 5)

button1.grid(row = 4, column = 0, padx = 5, pady = 5)
button2.grid(row = 4, column = 1, padx = 5, pady = 5)
button3.grid(row = 4, column = 2, padx = 5, pady = 5)
button_res.grid(row = 4, column = 3, padx = 5, pady = 5)

button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
button_point.grid(row = 5, column = 2, padx = 5, pady = 5)
button_equal.grid(row = 5, column = 3, padx = 5, pady = 5)

ventana.mainloop()