print("Welcome to the love Calculator!")
name1 = input("What is your name?\n")
name2 = input("What is their name?\n")

## TRUE LOVE ##

combined_string = name1 + name2
combined_string.lower()

t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

true = t + r + u + e

l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

love = l + o + v + e


love_score = str(f"{true}{love}")
score = int(love_score)

if score < 10 or score > 90:
    print(f"Your score is {score}% you go together like coke and mentos")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}% you are alright together")
else:
    print(f"Your score is {score}%")