import random

word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)
print(word)
guess = input("Guess A letter\n")
guess.lower()

Display = []
for i in word:
    Display.append("_")
print(Display)

count = 0

for i in word:
    if i == guess:
        print("right")
        Display[count] = guess
        count += 1
    else:
        print("wrong")
        count += 1

print(Display)