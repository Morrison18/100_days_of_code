total = 0

for i in range(1, 101):
    # print(i)
    if i % 2 > 0:
        # print(i)
        total += i
print(total)


second_total = 0

for i in range(1, 101, 2):
    second_total += i
print(second_total)