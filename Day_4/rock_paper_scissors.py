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
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = input("What do you pick Rock, Scissors or Paper\n")
player.lower()
CPU = [rock, paper, scissors]
pick = random.randint(0, 2)
CPU = CPU[pick]


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
elif player == rock and CPU == paper:
    print("💩 CPU Wins !!💀!! Hard Luck 💩")

elif player == paper and CPU == paper:
    print("Its a Draw")
    os.execl(sys.executable, sys.executable, *sys.argv)
elif player == paper and CPU == rock:
    print("🏆 You Win !!!! Well done 🏆")
elif player == paper and CPU == scissors:
    print("💩 CPU Wins !!💀!! Hard Luck 💩")

elif player == scissors and CPU == scissors:
    print("Its a Draw")
    os.execl(sys.executable, sys.executable, *sys.argv)
elif player == scissors and CPU == paper:
    print("🏆 You Win !!!! Well done 🏆")
elif player == scissors and CPU == rock:
    print("💩 CPU Wins !!💀!! Hard Luck 💩")
else:
    os.execl(sys.executable, sys.executable, *sys.argv)