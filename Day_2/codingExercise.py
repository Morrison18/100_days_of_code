height = float(input("What height are you in metres?\n"))
weight = float(input("What is your weight in Kg\n"))

BMI = round(weight / (height ** 2))

print("Your BMI is: " + str(BMI))
#F-String
print(f"Your BMI is: {BMI}")