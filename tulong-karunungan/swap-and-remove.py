# Swap & Remove
# Get two indices as user input (x and y) - x should always be less than y.
# Swap the elements in those indices and print the list.
# Remove the values between those two indices and print the list.

fruits = ["mango", "strawberry", "banana", "apple", "kiwi"]

x = int(input("Enter first index: "))
y = int(input("Enter second index: "))

if x >= y or x < 0 or x >= len(fruits) or y < 0 or y >= len(fruits):
    print("Invalid input!")

else:

    #swaps elements from user input
    fruits[x], fruits[y] = fruits [y], fruits[x]

    #pops the next index from the user input within the range of y
    for i in range (x + 1, y):
        fruits.pop(x + 1)

    print(fruits)