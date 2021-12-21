row1 = ["☠", "☠", "☠",]
row2 = ["☠", "☠", "☠",]
row3 = ["☠", "☠", "☠",]

map =[row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")
print(map)

position = input("Where would you like to hide the treasure?\n")
position.split()

horizontal = int(position[0]) -1
virtical = int(position[1]) -1


map[virtical][horizontal]= "x"

print(f"{row1}\n{row2}\n{row3}\n")
