print("Select from one of the following options:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Surprise!")

x = input("\nWhat option do you want to select? ")

if 1 <= int(x) <= 5:

    if x == '5':
        print("\nSurprise!")

    else:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        if x == '1':
            sum = num1 + num2
            print(f"\n{num1} + {num2} = {sum}")

        elif x == '2':
            difference = num1 - num2
            print(f"\n{num1} - {num2} = {difference}")

        elif x == '3':
            product = num1 * num2
            print(f"\n{num1} * {num2} = {product}")

        elif x == '4':
            quotient = num1 / num2
            print(f"\n{num1} / {num2} = {quotient}")

else:
    print("Invalid input!")