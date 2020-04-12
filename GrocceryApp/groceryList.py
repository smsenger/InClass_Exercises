#prompt user for a single grocery item
# append to grocery list

# groceries = []
# new_item = input('Please add a grocery item to the list: ')
# groceries.append(new_item)
# print(groceries)



#in an infinite while loop, prompt user for an item
#append the item to the list
#print the list after you add the item
#will prompt then print repeatedly because no end condition set

groceries = []
while True:
    new_item = input('Please add a grocery item to the list: ')
    groceries.append(new_item)
    print(groceries)



