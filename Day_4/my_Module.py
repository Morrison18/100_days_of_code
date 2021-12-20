import random

def dice_roll():
    dice1 = random.randint(1, 6)
    print(dice1)
    dice2 = random.randint(1, 6)
    print(dice2)

    score = dice1 + dice2
    return score
    # print(f"You rolled a {score}")
