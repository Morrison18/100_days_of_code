age = int(input("What is your current age?"))

days_in_year = 365
weeks_in_year = 52
months_in_year = 12

days_left = 90 * days_in_year - age * 365
weeks_left = 90 * weeks_in_year - age * weeks_in_year
months_left = 90 * months_in_year - age * months_in_year
years_left = 90 - age

print(f"You have {days_left} days, {weeks_left} weeks, {months_left} months and {years_left} years left to live.")