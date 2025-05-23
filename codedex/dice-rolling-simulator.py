import random

print()
print("== 🎲 Dice Rolling Simulator 🎲 ==")

isRunning = True

while isRunning: 
    number = random.randint(0,100)
    print(f"\nYou rolled the dice and got...{number} !")
    roll_again = input("Would you like to roll again? (Y/N) ")
    if roll_again.lower() != 'y':
        isRunning = False
print()
    