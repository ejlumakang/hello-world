import random

print()
print("=================== 🥠 Fortune Cookie 🥠 ===================")
f1 = 'Your greatest strength is the gentle power of silence'
f2 = 'A smile is your passport into the hearts of others'
f3 = 'You will find great success in your creative endeavors'
f4 = 'The best way to predict the future is to create it'
f5 = 'Your kindness will lead you to unexpected riches'


'''
intialize fortune cookie messages per variable `f1`, `f2`, etc.
store all variables in one named `fortunes` and create a list
in this list, the random function will randomly choose and display the fortune
'''

fortunes = [f1, f2, f3, f4, f5]
chosen_fortune = random.choice(fortunes)

#length of border: finds the longest fortune message
max_length = max(len(fortune) for fortune in fortunes)

#top border: calculated based on the longest fortune message
print("+-" + "-" * (max_length + 2) + "-+")

#ensures message is centered within borders
print(f"| {chosen_fortune.center(max_length + 2)} |")

#bottom border: same as top border
print("+-" + "-" * (max_length + 2) + "-+\n")