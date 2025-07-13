from tkinter import *

window = Tk()
window.geometry('700x500')
window.title('Calculator')
window.configure(bg='black')

e = Entry(window, width = 55, borderwidth=10)
e.place(x = 155, y = 50)
def click(num):
    result = e.get()
    e.delete(0, END)
    e.insert(0, str(result) + str(num))

b = Button(window, text = '1', width = 5, borderwidth=5, command = lambda: click(1))
b.place(x = 250, y = 100)

b = Button(window, text = '2', width = 5, borderwidth=5, command = lambda: click(2))
b.place(x = 300, y = 100)

b = Button(window, text = '3', width = 5, borderwidth=5, command = lambda: click(3))
b.place(x = 350, y = 100)

b = Button(window, text = '4', width = 5, borderwidth=5, command = lambda: click(4))
b.place(x = 250, y = 130)

b = Button(window, text = '5', width = 5, borderwidth=5, command = lambda: click(5))
b.place(x = 300, y = 130)

b = Button(window, text = '6', width = 5, borderwidth=5, command = lambda: click(6))
b.place(x = 350, y = 130)

b = Button(window, text = '7', width = 5, borderwidth=5, command = lambda: click(7))
b.place(x = 250, y = 160)

b = Button(window, text = '8', width = 5, borderwidth=5, command = lambda: click(8))
b.place(x = 300, y = 160)

b = Button(window, text = '9', width = 5, borderwidth=5, command = lambda:click(9) )
b.place(x = 350, y = 160)

b = Button(window, text = '0', width = 5, borderwidth=5, command = lambda: click(0))
b.place(x = 300, y = 190)


def add():
    n1 = e.get()
    global math
    math = "addition"
    global i
    i = int(n1)
    e.delete(0, END)

b = Button(window, text = '+', width = 5, borderwidth=5, command = add, bg = 'blue', fg = 'white')
b.place(x = 200, y = 240)

def sub():
    n1 = e.get()
    global math
    math = "subtraction"
    global i
    i = int(n1)
    e.delete(0, END)
b = Button(window, text = '-', width = 5, borderwidth=5, command = sub, bg = 'red', fg = 'white')
b.place(x = 250, y = 240)

def mul():
    n1 = e.get()
    global math
    math = "multiplication"
    global i
    i = int(n1)
    e.delete(0, END)
b = Button(window, text = '*', width = 5, borderwidth=5, command = mul, bg = 'green', fg = 'white')
b.place(x = 300, y = 240)

def div():
    n1 = e.get()
    global math
    math = "division"
    global i
    i = int(n1)
    e.delete(0, END)
b = Button(window, text = '/', width = 5, borderwidth=5, command = div, bg = 'yellow', fg = 'black')
b.place(x = 350, y = 240)

def equal():
    n2 = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, i +int(n2))
    elif math == "subtraction":
        e.insert(0, i - int(n2))
    elif math == "multiplication":
        e.insert(0, i * int(n2))
    elif math == "division":
        e.insert(0, i / int(n2))


b = Button(window, text = '=', width = 5, borderwidth=5, command = equal)
b.place(x = 400, y = 240)


def clear ():
    e.delete(0, END)
b = Button(window, text = 'C', width = 5, borderwidth=5, command = clear, bg= 'gold')
b.place(x = 175, y = 100)



mainloop()
