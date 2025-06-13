
# GRADE CALCULATOR
def grade(gra):
    if gra >= 90:
        print("A")
    elif gra >= 80 and gra <= 89:
        print("B")
    elif gra >= 70 and gra <= 80:
        print("C")
    elif gra >= 60 and gra <= 69:
        print("D")
    else:
        print("F")

gra = int(input("Enter your score: "))
grade(gra)

# EVEN / ODD CHECK
def even(number):
    if number % 2 == 0:
        print("It's even")
    else:
        print("It's odd")

number = int(input("Enter number: "))
even(number)

# TEMPERATURE CONDITION CHECK
def temparature(temp):
    if temp < 15:
        print("It's cold")
    elif temp > 15 and temp < 25:
        print("It's moderate")
    else:
        print("It's hot")

temp = int(input("Enter temperature in celsius: "))
temparature(temp)

# SIDES OF TRIANGLE
def triangle(a, b, c):
    if a == b == c:
        print("Equilateral Triangle")
    elif (a == b or b == c or a == c):
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")

a = int(input("Enter side1: "))
b = int(input("Enter Side 2: "))
c = int(input("Enter Side 3: "))
triangle(a, b, c)

# LEAP YEAR
def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")
year = int(input("Enter a year: "))
leapyear(year)

# AGE
def checkage(age):
    if age <= 12:
        print("Child")
    elif age >= 13 and age <= 19:
        print("Teenager")
    elif age >= 20 and age <= 60:
        print("Adult")
    else:
        print("Senior")
age = int(input("Enter Age: "))
checkage(age)

# Calculator
def calculator(a, b, operator):
    if operator == '+':
        print(a + b)
    elif operator == '-':
        print(a - b)
    elif operator == '*':
        print(a * b)
    elif operator == '/':
        print(a / b)
    else:
        print("It is not an operator")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operator = input("Enter operator: ")
calculator(a, b, operator)

# Login
def login(email, password):
    if email == "nandu@gmail.com" and password == "nandu123":
        print("Access granted")
    else:
        print("Access Denied")

email = input("Enter your Email: ")
password = input("Enter your password: ")
login(email, password)

# BMI Calculator
def bmicalculator(height, weight):
    bmicheck = (weight / height * height)
    if bmicheck < 18.5:
        print("Underweight")
    elif bmicheck >= 18.5 and bmicheck < 24.9:
        print("Normal Weight")
    elif bmicheck >= 25 and bmicheck < 29.9:
        print("Overweight")
    else:
        print("Obese weight")

height = int(input("Enter Height in meters: "))
weight = int(input("Enter weight in kg: "))
bmicalculator(height, weight)