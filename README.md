# tutedude_assignments
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
