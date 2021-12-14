height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in Kg: "))

bmi = round(weight / ((height /100) ** 2), 1)
print(bmi)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, You are underweight")

elif bmi > 18.4 and bmi <= 25:
    print(f"Your BMI is {bmi}, You are normal weight")

elif bmi > 25 and bmi <= 30:
    print(f"Your BMI is {bmi}, You are over weight")

elif bmi > 30 and bmi <= 35:
    print(f"Your BMI is {bmi}, You are obese")

else:
    print(f"Your BMI is {bmi} you need to see a doctor you are clinically obese")
