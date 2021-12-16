print("Welcome to the Rollercoaster ride")
height = int(input("Enter your height\n"))

if height>=120:
    print("Your can ride the rollercoaster!")
    age = int(input("What age are you"))
    if age < 12:
        print("Childs Tickets are $5.")
        bill = 5
    elif age <=18:
        print("Teenagers tickets are $7.")
        bill = 7
    else:
        print("Aldut tickets are $12.")
        bill = 12

    photo = input("Would you like to purchase a photo? Y or N\n")
    if photo == "y" or photo == "Y" or photo == "yes":
        print("Photos cost an extra $15.")
        bill += 15
    print(f"IT will be ${bill}.00 to ride the rollercoast")
else:
    print("Sorry you are to short to ride the rollercoaster come back next year.")
