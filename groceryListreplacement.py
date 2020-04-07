
#to fill grocery list:
#prompt until they enter empty string

groceries1 = []

while len(groceries1) < 3:
    item = input('What do you need from the store? ')
    if item == '':                                        #if enter empty string break out of loop // alt: if len(item) == 0
        break        
    else:
        groceries1.append(item) 



groceries2 = []
while len(groceries2) < 3:
    item = input('What do you need from the store? ')
    if item == '':                                         #if enter empty string break out of loop
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



#This starts the count of inputs at 0, then continues until the difference between the second and first index has been reached.
#Assigns value to old_item by referencing the current index number in question
#prompts for correct index if number too large
#new item prompt includes reference to old item that will be replaced

def replacement():
    new_index1 = int(input('Use index number to select first item to replace, using printed list above as reference. '))
    new_index2 = int(input('Use index number to select last item to replace, using printed list above as reference. New item(s) will replace existing item(s) including this second index number. '))
    if new_index1 > len(groceries1):
        print('First index number too high. ')
        print('Re-enter first index number. ')
        return replacement()
    elif new_index2 > len(groceries1): 
        print('Second index number too high. ')  
        print('Please re-enter second index number.')
        return replacement()
    else:        
        difference = new_index2 - new_index1
        count = 0
        while count <= difference:
            old_item = groceries1[new_index1 + count]                                                
            new_item = input(f'Name new item to replace {old_item}: ')
            groceries1[new_index1 + count] = new_item                        #new_index1 + count gets to the current index number // sets value of new_item to the current index number
            count += 1  

#call the function. This initiates the process. Other function calls prompt for index numbers again, then continue evaluation if numbers correct.
replacement()

#print updated combined list
print(groceries1)