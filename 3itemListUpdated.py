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


#alternate method of combinining two lists:
# groceries3 = groceries1 + groceries2
# print(groceries3)

#print combined list
#prints index number next to item
print(groceries1)
indexes = range(len(groceries3))
for i in indexes:
    print(f'{i}: {groceries1[i]}')

    #could also use: print(f'{i}: {list[i]}') if incremening in a while loop

#prompt user for index of item to replace
new_index = int(input('Select index of item to replace, using printed list above as reference. '))
#prompt user for new item
new_item = input('Name new item to replace at this index: ')
#replace the item at that index with the new item
groceries1[new_index] = new_item
#print updated combined list
print(groceries1)

