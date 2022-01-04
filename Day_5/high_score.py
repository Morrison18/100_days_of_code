student_scores = input("Input a list of student scores \n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

high_num = 0
for high in student_scores:
  if high > high_num:
    high_num = high
print(f"The Highest number is {high_num}")

low_num = 1000
for low in student_scores:
  if low < low_num:
    low_num = low
print(f"The Lowest number is {low_num}")



print(f"Highest number {max(student_scores)}")
print(f"Lowest number {min(student_scores)}")

# input = 78 65 89 86 55 91 64 89