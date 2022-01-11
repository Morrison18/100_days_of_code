import random

word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)
print(word)
guess = input("Guess A letter\n")
guess.lower()

for i in word:
    if i == guess:
        print("right")
    else:
        print("wrong")