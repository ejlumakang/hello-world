# print("\n===== 🤑 Who Wants to Be a Millionaire 🤑 =====\n")

# q1 = '1. Which of the following instruments do you have to blow into to play? 🌬'
# a = 'Trumpet'
# b = 'Drum'
# c = 'Guitar'
# d = 'Triangle'
# print(q1)

# print('\tA) 🎺 Trumpet')
# print('\tB) 🥁 Drum')
# print('\tC) 🎸 Guitar')
# print('\tD) 📐 Triangle\n')

# answer1 = input("\tEnter your answer: ")
# if answer1.lower() != 'a':
#     print("\n",answer1, "is incorrect.\n")
# else:
#     print("\n🎺",a, "is correct! 🎉\n")


print("\n==========❓ Quiz Game ❓==========")
score = 0
start = 1

questions = [
    ('What is the capital of Japan? 🎎', 'Tokyo'),
    ('Who painted the Mona Lisa? 🎨', 'Leonardo da Vinci'),
    ('Which planet is known as the Red Planet? 🪐', 'Mars'),
    ('Who wrote the play "Romeo and Juliet"? 🤴👸', 'William Shakespeare'),
    ('What is the largest ocean on Earth? 🌍', 'Pacific Ocean')
]

for question, correctAnswer in questions:
    answer = input(f"\n{start}. {question} \n\n   > ").strip().lower()
    if answer == correctAnswer.lower():
        print("\n  ✅ Correct!")
        score += 1
        start += 1          
    else:
        print("\n  ❌ Incorrect!")
        start += 1 

print(f"\n\n🎉 You scored {score} out of 5. 🎉\n")
