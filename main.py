# Exercise 1. Write a Python-script that displays the message “Hello world”.

print ('Hello world')

# Exercise 2. Rewrite the first script to display three any messages.

print ('''
    Hello world
    слава Україні
    Героям слава
    ''')

# Exercise 3. Write a Python-script to reads values for the length and width of a rectangle
# and returns the area of the rectangle.

length = float(input('length='))
width = float(input('width='))

print(length*width)

# Exercise 4. Write a program that requests the user to enter two numbers
# and prints the sum, product, difference and quotient of the two numbers.

number1 = float(input('number1= '))
number2 = float(input('number2= '))

sum = number1+number2
product = number1*number2
difference = number1-number2
quotient = number1/number2

str1 = 'The sum is ', sum
str2 = 'The difference is ', difference
str3 = 'The product is ', product
str4 = 'The quotient is ', quotient

print (str1, str2, str3, str4, sep='\n')

#не розумію, чому в виводі в мене дужки і лапки

# Exercise 5. Write a program that reads in the radius of a circle and prints the circle’s diameter,
# circumference and area. Use the constant value 3.14159 for π.
# Do these calculations in output statements.

radius = float(input('radius= '))
pi = 3.14159

diam = 2*radius
circumference = 2*pi*radius
area = pi*radius**2

print ('diam = ', diam, 'circumference = ', circumference, 'area = ', area, sep='\n')

# Homework 2
# 1. Construct an integer from the string "123"

x = '123'

print(int(x))

# 2. Construct a float from the integer 123

y = int(123)

print(float(y))

# 3. Construct an integer from the float 12.345

z = float(12.345)

print(int(z))

# 4. Write a Python-script that detects the last 4 digits of a credit card
# знайшла методи рішення до наступних задач в підручнику, але це не є мої базові знання

card = input('Номер карти: ')

print (card[-4:])

# 5. Write a Python-script that calculates the sum of the digits of a three-digit number
# 6. Write a program that calculates and displays the area of a triangle if its sides are known
# 7. *Write a Python-script that calculates the sum of the digits of a number
# 8. *Determine the number of digits in a number
# 9. *Print the digits in reverse order