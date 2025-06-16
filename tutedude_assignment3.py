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

