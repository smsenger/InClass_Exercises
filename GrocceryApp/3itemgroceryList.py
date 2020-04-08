#convert infinite grocery item prompter, only accept 3 items

groceries1 = []

while len(groceries1) < 3:
    item = input('What do you need from the store? ')
    groceries1.append(item)


groceries2 = []
while len(groceries2) < 3:
    item = input('What do you need from the store? ')
    groceries2.append(item)

#combine the two lists

groceries1.extend(groceries2)
print(groceries1)

#alternate method of combinining two lists:
# groceries3 = groceries1 + groceries2
# print(groceries3)