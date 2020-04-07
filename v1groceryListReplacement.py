
#to fill grocery list:
#prompt until they enter empty string

groceries1 = []

while len(groceries1) < 3:
    item = input('What do you need from the store? ')
    if item == '':                     #if enter empty string break out of loop // alt: if len(item) == 0
        break        
    else:
        groceries1.append(item) 



groceries2 = []
while len(groceries2) < 3:
    item = input('What do you need from the store? ')
    if item == '':                       #if enter empty string break out of loop
        break
    else:
        groceries2.append(item)

#combine the two lists




groceries1.extend(groceries2)


#alternate method of combinining two lists:
# groceries3 = groceries1 + groceries2
# print(groceries3)


#print combined list w/index number next to item

indexes = range(len(groceries1))
for i in indexes:
    print(f'{i}: {groceries1[i]}')

    #could also use: print(f'{i}: {list[i]}') if incremening in a while loop



#THEN, subset of items to replace, by index number
#if start and end same, replace 1 item
#if different, replace with a list
#prompt until they enter empty string
#This will work on any size list. 

new_index1 = int(input('Use index number to select first item to replace, using printed list above as reference. After entry, press ENTER. '))
new_index2 = int(input('Use index number to select last item to replace, using printed list above as reference. New item(s) will replace existing item(s) including this second index number. After entry, press ENTER. '))

#This starts the count of inputs at 0, then continues until the difference between the second and first index has been reached.
#Assigns value to old_item by referencing the current index number in question
#new item prompt includes reference to old item that will be replaced

count = 0
difference = new_index2 - new_index1
possible_items = range(len(groceries1))
# possible_indices = range(new_index1, new_index2, 1) 


while count <= difference:
    try:
        old_item = groceries1[new_index1 + count]                                                             
        new_item = input(f'Name new item to replace {old_item}: ')               #prompt user for new item
        groceries1[new_index1 + count] = new_item                                #new_index1 + count gets to the current index number // sets value of new_item to the current index number
        count += 1                                                               #iterates through range given in index number selection until the count = difference between to given indice
    except:
        print('Entered index without an assigned corresponding item on list. boobeebaaboop!')          s


#print updated combined list
print(groceries1)