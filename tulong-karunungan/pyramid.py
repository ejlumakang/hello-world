def user_input():
    while True:
        x = int(input("Enter a number between 1-10: "))
        if 1 <= x <= 10:
            return x
        else:
            print("Invalid number!")


# Pyramid 1
x = user_input()
for i in range(x):
    for j in range(i + 1):
        print("*", end=" ")
    print()

# Pyramid 2
x = user_input()
for i in range(x):
    for j in range(i + 1):
        print(j + 1, end=" ")
    print()

# Pyramid 3
x = user_input()
for i in range(x):
    for j in range(i, x - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()