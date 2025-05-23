def wordCounter(sentence):
    words = sentence.lower().split()
    return len(words)

def main():
    print("\n=== 🔠 Word Counter! 🔠 ===\n")
    sentence = input("Enter a sentence: ")
    wordCount = wordCounter(sentence)
    print("Number of words:", wordCount, "\n")

main()
'''
empty_list = []

print("\n=== 🔠 Word Counter! 🔠 ===\n")
words = input("Enter a sentence: ").lower().split()

for word in words:
    empty_list.append(word)

print("Number of words:", len(empty_list), "\n")
'''


