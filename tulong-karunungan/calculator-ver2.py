#calculator with randomized operator 

import random


def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return


def display(num1, num2, operator, answer):
    print(f"\n{num1} {operator} {num2} = {answer}")


print("Select from one of the following options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Surprise!")

x = input("\nWhat option do you want to select? ")

if int(x) > 5:
    print("Invalid option!")
else:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

if x == '1':
    answer = calculate(num1, num2, '+')
    display(num1, num2, '+', answer)

elif x == '2':
    answer = calculate(num1, num2, '-')
    display(num1, num2, '-', answer)

elif x == '3':
    answer = calculate(num1, num2, '*')
    display(num1, num2, '*', answer)

elif x == '4':
    answer = calculate(num1, num2, '/')
    display(num1, num2, '/', answer)


elif x == '5':
    surprise = random.choice(["+", "-", "*", "/"])
    answer = calculate(num1, num2, surprise)
    display(num1, num2, surprise, answer)