# tutedude_assignments
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
