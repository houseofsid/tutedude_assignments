# tutedude_assignments
CALCULATOR
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






Assignment 4
#Task1
import os
if os.path.exists('sample.txt'):
    with open('sample.txt', 'r') as file:
        line_number = 1
        for line in file:
            print(f"{line.strip()}")
            line_number += 1
else:
    print(f"Error: The file 'sample.txt' was not found.")

#Task2
import os
output_filename = "output.txt"
user_input_initial = input("Enter text to write to the file: ")
with open(output_filename, 'w') as file:
    file.write(user_input_initial + '\n')
print(f"Data successfully written to {output_filename}.")
user_input_append = input("Enter additional text to append: ")
with open(output_filename, 'a') as file:
    file.write(user_input_append + '\n')
print("Data successfully appended.")
print(f"\nFinal content of {output_filename}:")
if os.path.exists(output_filename):
    with open(output_filename, 'r') as file:
        print(file.read().strip())
else:
    print(f"Error: The file '{output_filename}' was not found.")



Assignment 5
#Task1
dict_students = {'Raghav': 54, 'Ayush': 62, 'Priya': 77, 'Alice': 93}
dict_name = input("Enter student's name: ")
dict_marks = dict_students.get(dict_name)
if dict_marks is not None:
    print(f"{dict_name}'s marks: {dict_marks}")
else:
    print("Student not found")


#Task2
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Original list:", my_list)
extracted_first_five = my_list[0:5]
print("Extracted first five elements:", extracted_first_five)
reversed_extracted_elements = extracted_first_five[::-1]
print("Reversed extracted elements:", reversed_extracted_elements)





#Assignment 3
#Task1
n=int(input('Enter a number: '))
def factorial (n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
print("The factorial of", n, "is", factorial(n))


#Task2
n=int(input('Enter a number:'))
import math
print('Square root:',math.sqrt(n))
print('Logarithm:', math.log(n))
print('Sine', math.sin(n))



#assignment 2
#Task1
number=int(input('Enter a number: '))
if number%2==0:
    print(number,'is an even number')
else:
    print(number,'is an odd number')

#Task2
sum=0
for int in range (1, 51):
    sum+=int;
print('The sum of numbers from 1 to 50 is:', sum)





#assignment1
#Task1
number1=int(input('Enter the first number: '))
number2=int(input('Enter the second number: '))
addition=number1+number2
subtraction=number1-number2
multiplication=number1*number2
division=number1/number2
print("addition =",addition)
print("subtraction =",subtraction)
print("multiplication =",multiplication)
print("division =",division)

#Task2
firstname=input('Enter your first name: ')
lastname=input('Enter your last name: ')
fullname=firstname+lastname
print('Hello,', fullname,'Welcome to the python program!')
