import random

while True:
    print()
    print("===== 🪨 Rock, 📄 Paper, 👈 Scissors, 🦎 Lizard, 🖖 Spock! =====")
    print("\nRules of the Game:\n")
    print("> Rock\t\t✅ Scissors - Lizard")
    print("> Paper\t\t✅ Rock - Spock")
    print("> Scissors\t✅ Paper - Lizard")
    print("> Lizard\t✅ Paper - Spock")
    print("> Spock\t\t✅ Rock - Scissors")
    print("\n-----------------------------------")

    print("\nSelect your move:")
    print("1) 🪨 ROCK")
    print("2) 📄 PAPER")
    print("3) 👈 SCISSORS")
    print("4) 🦎 LIZARD")
    print("5) 🖖 SPOCK")

    '''
    declare a variable called `choice` to accept user input that should be within the range of #1-3 using an if-else statement
        : continue -> if the user input is invalid, it will continue to the next iteration of loop to prompt user input 
    create a list of possible moves called `moves` to store the values: `ROCK`, `PAPER`, and `SCISSORS`
    '''

    choice = int(input("\nEnter your choice (1/2/3/4/5): "))
    if choice < 1 or choice > 5:
        print("\n>> Invalid input. Try again.")
        continue
    print("___________________________________\n")

    '''
    initialize a variable `player` to assign the player's choice which is according to the `choice` from the `moves` list 
        : player = moves[choice - 1] -> include -1 as index counting starts from 0
    initialize a variable `computer` and it will randomly choose from the `moves` list using random function -> do not forget to import random
    '''

    moves = ['🪨 ROCK', '📄 PAPER', '👈 SCISSORS', '🦎 LIZARD', '🖖 SPOCK']
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
    elif (player == "🪨 ROCK" and (computer == "👈 SCISSORS" or computer == "🦎 LIZARD")) or \
         (player == "📄 PAPER" and (computer == "🪨 ROCK" or computer == "🖖 SPOCK")) or \
         (player == "👈 SCISSORS" and (computer == "📄 PAPER" or computer == "🦎 LIZARD")) or \
         (player == "🦎 LIZARD" and (computer == "📄 PAPER" or computer == "🖖 SPOCK")) or \
         (player == "🖖 SPOCK" and (computer == "🪨 ROCK" or computer == "👈 SCISSORS")):
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