import random

while True:
    print()
    print("===== 🪨 Rock, 📄 Paper, 👈 Scissors! =====")
    print("\nSelect your move:")
    print("1) 🪨 ROCK")
    print("2) 📄 PAPER")
    print("3) 👈 SCISSORS")

    '''
    declare a variable called `choice` to accept user input that should be within the range of #1-3 using an if-else statement
        : continue -> if the user input is invalid, it will continue to the next iteration of loop to prompt user input 
    create a list of possible moves called `moves` to store the values: `ROCK`, `PAPER`, and `SCISSORS`
    '''

    choice = int(input("\nEnter your choice (1/2/3): "))
    if choice < 1 or choice > 3:
        print("\n>> Invalid input. Try again.")
        continue
    print("___________________________________\n")

    '''
    initialize a variable `player` to assign the player's choice which is according to the `choice` from the `moves` list 
        : player = moves[choice - 1] -> include -1 as index counting starts from 0
    initialize a variable `computer` and it will randomly choose from the `moves` list using random function -> do not forget to import random
    '''

    moves = ['🪨 ROCK', '📄 PAPER', '👈 SCISSORS']
    player = moves[choice - 1]
    computer = random.choice(moves)

    print("> 👧 Player picked:   ", player)
    print("> 👾 Computer picked: ", computer)
    print("___________________________________")

    '''
    using if-else statement, create the mechanics of rock, paper, scissors
    if player matches with computer, it's a draw... etc.
    '''

    if player == computer:
        print("\n\n   🎉 ˗ˏˋ It's a tie! ˎˊ˗ 🎉\n")
    elif (player == "🪨 ROCK" and computer == "👈 SCISSORS") or \
        (player == "📄 PAPER" and computer == "🪨 ROCK") or \
        (player == "👈 SCISSORS" and computer == "📄 PAPER"):
        print("\n\n 🎉 ˗ˏˋ The Player won! 👧 ˎˊ˗ 🎉")
        print("      Luck is on your side. \n")
    else:
        print("\n\n 🎉 ˗ˏˋ The Computer won! 👾 ˎˊ˗ 🎉")
        print("      Better luck next time. \n")

    '''
    using a while loop, the program will continue to run, unless it declines for another rematch
    after first round of a game, user will be asked if he would like to play again
    '''

    print("===================================")
    play_again = input("\nDo you want to play again? (Y/N): ")
    
    if play_again.lower() != 'y':
        exit()

''' RPS CODE USING IF-ELSE, NO LIST

import random

isRunning = True

while isRunning:
    print()
    print("Rock, Paper, Scissors!")
    print("\nSelect your move:")
    print("1) ROCK")
    print("2) PAPER")
    print("3) SCISSORS")

    player = int(input("\nEnter your choice: "))
    
    if player == 1:
        player = "ROCK"
    elif player == 2:
        player = "SCISSORS"
    elif player == 3:
        player = "PAPER"
    else:
        print("Invalid input. Try again.\n")
        exit()

    computer = random.randint(1, 3)

    if computer == 1:
        computer = "ROCK"
    elif computer == 2:
        computer = "SCISSORS"
    elif computer == 3:
        computer = "PAPER"

    print("\nPlayer picked: \t ", player)
    print("Computer picked: ", computer)

    if player == computer:
        print("\nIt's a tie!\n")
    elif (player == "ROCK" and computer == "SCISSORS") or \
        (player == "PAPER" and computer == "ROCK") or \
        (player == "SCISSORS" and computer == "PAPER"):
        print("\nThe player won!\n")
    else:
        print("\nThe computer won!\n")
    
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() != 'y':
        print("\nThanks for playing!\n")
        break
'''