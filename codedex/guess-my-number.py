import random

randomNumber = random.randint(0, 10)

print("\n===== 🔢 Guess The Number 🔢 =====\n")
guess = int(input("Guess my number: "))

while True: 
    if guess != randomNumber:
        guess = int(input("Guess my number: "))
    else: 
        print("\nYou guessed my number! The answer is", randomNumber, "! 🎉\n")
        exit()