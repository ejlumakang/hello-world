import math

def rectangle(width, height):
    return width * height

def circle(radius):
    return math.pi * radius ** 2

def triangle(base, height):
    return 0.5 * base * height

def main():
    while True: 
        print("\n=== 🧮 Area Calculator 🧮 === \n")
        print("Select a shape to calculate its area:")
        print("  1) 🚃 Rectangle")
        print("  2) 🌀 Circle")
        print("  3) 📐 Triangle")

        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            width = float(input("\nEnter width: "))
            height = float(input("Enter height: "))
            area = (rectangle(width, height))
            print(f"\nThe area of the rectangle is: {area}")
        elif choice == 2:
            radius = float(input("\nEnter radius: "))
            area = (circle(radius))
            print(f"\nThe area of a circle is: {area}")
        elif choice == 3:
            base = float(input("\nEnter base: "))
            height = float(input("Enter height: "))
            area = (triangle(base, height))
            print(f"The area of a triangle is: {area}")
        else:
            print("Invalid input.\n")

        while True:
            try_again = input("\nWould you like to try again? ")
            if try_again.lower() == 'y':
                break
            else:
                return

main()