print("Welcome to the tip calculator")

total_bill = float(input("what was the total bill?\n"))
#print(type(total_bill))

tip_percentage = float(input("what percentage tip would you like to give?\n"))
#print(type(tip_percentage))

num_people = input("How many people are splitting the bill?\n")
#print(type(num_people))

tip = ( tip_percentage / 100) * total_bill
what_to_pay = round((tip + total_bill) / int(num_people), 2)

print(f"each person should pay €{what_to_pay} each, with €{round(tip, 2)} tip included and split two ways")