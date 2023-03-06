# row1 = ["a","b","c"]
# row2 = ["d","e","f"]
# row3 = ["g","h","i"]

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]

map = [row1,row2,row3]
#print(f"{row1}\n{row2}\n{row3}")

#1print(map[0][0])

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")