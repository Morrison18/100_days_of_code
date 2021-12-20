import os
import sys

print('''        
            ************************************* 
                 Welcome to Treasure Island.
            Your Mission is to find the treasure.
            *************************************\n''')

print('''
        To get through the door you must answer a riddle        
                type Hint if you need help!!!
        ------------------------------------------------\n
            ''')

print("Answer the riddle to get past the first door\n")
door1 = input("What has to be broken before you use it?\n")
door1.lower()
# door1.find("egg") == -1
# door1.find("egg") != -1
print(door1)
pass1, pass2, pass3, pass4, pass5 = False, False, False, False, False


if door1.find("egg") != -1:
    pass1 = True
elif door1.find("hint") != -1:
    door1 = input("you can scramble me\n")
    if door1.find("egg") != -1:
        pass1 = True
else:
    # restarts game
    print("Game Over Try Again!")
    os.execl(sys.executable, sys.executable, *sys.argv)

print("Answer the riddle to get past the Second door\n")
if pass1 == True:
    door2 = input("What month of the year has 28 days?\n")
    door2.lower()
    if door2.find("every") != -1 or door2.find("all") != -1:
        pass2 = True
    elif door2.find("hint") != -1:
        door2 = input("What month\'S of the year has 28 days?\n")
        if door2.find("every") != -1 or door2.find("all") != -1:
            pass2 = True
else:
    # restarts game
    print("Game Over Try Again!")
    os.execl(sys.executable, sys.executable, *sys.argv)

print("Answer the riddle to get past the Third door\n")
if pass2 == True:
    door3 = input("What is always in front of you but can’t be seen?\n")
    door3.lower()
    if door3.find("future") != -1:
        pass3 = True
    elif door3.find("hint") != -1:
        door3 = input("The Past is behind you\n")
        if door3.find("future") != -1:
            pass3 = True
else:
    # restarts game
    print("Game Over Try Again!")
    os.execl(sys.executable, sys.executable, *sys.argv)

print("Answer the riddle to get past the Forth door\n")
if pass3 == True:
    door4 = input("I shave every day, but my beard stays the same. What am I?\n")
    door4.lower()
    if door4.find("barber") != -1 or door4.find("hairdresser") != -1:
        pass4 = True
    elif door4.find("hint") != -1:
        door4 = input("Its my job\n")
        if door4.find("barber") != -1 or door4.find("hairdresser") != -1:
            pass4 = True
else:
    # restarts game
    print("Game Over Try Again!")
    os.execl(sys.executable, sys.executable, *sys.argv)

print("This is the final door answer the riddle and you'll get the treasure\n")
if pass4 == True:
    door5 = input("Sometimes it's silver but also gold.\nPrinted on paper it's a treasure to hold. What is it?\n")
    door5.lower()
    if door5.find("money") != -1:
        pass5 = True
    elif door5.find("hint") != -1:
        door5 = input("no hints available take a guess\n")
        if door5.find("money") != -1:
            pass5 = True
else:
    # restarts game
    print("Game Over Try Again!")
    os.execl(sys.executable, sys.executable, *sys.argv)

if pass5 == True:
    print("You Won Congratulations \n the password is winner")
    password = input("Enter the password\n")
    password.lower()
    if password == "winner":
        print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
******************************************************************************* 
              ''')