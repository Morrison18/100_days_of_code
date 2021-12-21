import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

# r stores the length of names
r = random.randint(0, len(names))
# print (r)

pay_bill = names[r]
print(pay_bill)

# Instead of all the above code
who_will_pay = random.choice(names)
print(who_will_pay)
