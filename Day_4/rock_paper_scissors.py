import os
import random
import sys

rock = '''
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
Paper
    _______
---'   ____)___
          ______`)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)_____
        __________)
        __________)
      (____)
---.__(___)
'''

player = input("What do you pick Rock, Scissors or Paper\n")
player.lower()
CPU = [rock, paper, scissors]
pick = random.randint(0, 2)
CPU = CPU[pick]
play_again = False

if player == "rock":
    player = rock
elif player == "scissors":
    player = scissors
elif player == "paper":
    player = paper
else:
    print("Try Again")
    os.execl(sys.executable, sys.executable, *sys.argv)

print(f"Player:\n{player}\n CPU:\n{CPU}")
if player == rock and CPU == rock:
    print("Its a Draw")
    os.execl(sys.executable, sys.executable, *sys.argv)
elif player == rock and CPU == scissors:
    print("🏆 You Win !!!! Well done 🏆")
    Again = input("Play Again Y = yes N = No")
    Again.lower()
    if Again == "y":
        play_again = True

elif player == rock and CPU == paper:
    print("💩 CPU Wins !!💀!! Hard Luck 💩")
    Again = input("Play Again Y = yes N = No")
    Again.lower()
    if Again == "y":
        play_again = True

elif player == paper and CPU == paper:
    print("Its a Draw")
    os.execl(sys.executable, sys.executable, *sys.argv)
elif player == paper and CPU == rock:
    print("🏆 You Win !!!! Well done 🏆")
    Again = input("Play Again Y = yes N = No")
    Again.lower()
    if Again == "y":
        play_again = True
elif player == paper and CPU == scissors:
    print("💩 CPU Wins !!💀!! Hard Luck 💩")
    Again = input("Play Again Y = yes N = No")
    Again.lower()
    if Again == "y":
        play_again = True

elif player == scissors and CPU == scissors:
    print("Its a Draw")
    os.execl(sys.executable, sys.executable, *sys.argv)
elif player == scissors and CPU == paper:
    print("🏆 You Win !!!! Well done 🏆")
    Again = input("Play Again Y = yes N = No")
    Again.lower()
    if Again == "y":
        play_again = True
elif player == scissors and CPU == rock:
    print("💩 CPU Wins !!💀!! Hard Luck 💩")
    Again = input("Play Again Y = yes N = No")
    Again.lower()
    if Again == "y":
        play_again = True
else:
    os.execl(sys.executable, sys.executable, *sys.argv)

if play_again == True:
    os.execl(sys.executable, sys.executable, *sys.argv)

