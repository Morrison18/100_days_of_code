print("Welcome to python pizza")
print("Prices\n"
      "Small Pizza: $15\n"
      "Medium Pizza: $20\n"
      "Large Pizza: $ 25\n")
size = input("What size pizza do you want? S, M, L \n")
add_pepperoni= input("Would you like to add Pepperoni? Y, N\n")
extra_cheese = input("Do you want extra cheese? Y, N\n")

if size == "S" or size =="s":
    size == "small"
    pizza = 15
elif size == "M" or size == "m":
    size == "medium"
    pizza = 20
elif size == "L" or size == "l":
    size == "large"
    pizza = 25

    if add_pepperoni == "y" or add_pepperoni == "Y" or add_pepperoni == "yes" or add_pepperoni == "Yes" and size == "small":
        pizza += 2
    elif add_pepperoni == "y" or add_pepperoni == "Y" or add_pepperoni == "yes" or add_pepperoni == "Yes" and size == "medium" or size == "large":
        pizza += 3
    if extra_cheese == "y" or extra_cheese == "yes" or extra_cheese == "Y" or extra_cheese == "Yes":
        pizza += 1
else:
    print("Ops something went wrong!! \n PLEASE RELOAD THE PROGRAM")

print(f"Your final bill is ${pizza}")
