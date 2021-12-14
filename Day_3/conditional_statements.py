

print("Welcome to the Rollercoaster!")
height = int(input("What height is the person ?\n"))

ticket_adult = 18
ticket_teens = 10
ticket_Kids = 5
sell_ticket = False

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What age are you?\n"))
    if age >= 18:
        print(f"The Ticket for Kids is ${ticket_adult}")
    elif age >= 13 & age <18:
        print(f"The ticket for teens is ${ticket_teens}")
    else:
        print(f"The Ticket for adults is ${ticket_Kids}")
else:
    print("Your to short go home")
