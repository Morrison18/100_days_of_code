student_heights = input("Input a list of student heights \n").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

total_height = 0
for h in student_heights:
  total_height += h
print(total_height)

num_students = 0
for s in student_heights:
  num_students += 1
print(num_students)

avg_height = round(total_height / num_students)

print(f"The average height of the students is {avg_height}")

# Avg_height = sum(student_heights) / len(student_heights)
# print(f"The average height of the students is {Avg_height}")
# input = 156 178 165 171 187