# '''
# Instrutions:


# The starter code provides you with the main menu for a command-line
# based grocery list application.

# The user should be able to add, update, and remove items.

# Small exercise ------------------------------------------------
# Using this starter code, you're going to combine the pieces of code
# you've written so far to create the functionality for each action (either 
# adding, updating, or removing an item).

# Each time the user adds, updates, or deletes an item, they should see the main menu again.

# Medium exercise ------------------------------------------------
# For each sub-menu, show the user another menu with choices for that section of the application.
# For example, when Removing Items, show the user this menu:

# 1. Print items
# 2. Delete an item
# 3. Delete multiple items
# 4. Return to main menu

# If they enter "2", prompt them for the index of the item to delete.
# If they enter "3", prompt them for a start index and an end index for the slice to delete.

# After deleting, show them the "delete" menu again.
# To return to the main menu, the user needs to enter "4" at the prompt.

# Large exercise ------------------------------------------------
# Add a second array that stores whether or not each grocery list item has been obtained.
# Every time you add or remove an item, you need to add to or remove from this second list.

# Add an additional main menu option for changing the status of any grocery list item.

# Update the "Print Items" output so that it shows whether or not an item has been obtained.
# '''


groceries = []


main_menu = '''

1. Print List
2. Add Items
3. Edit Items
4. Remove Items
5. Change item status
6. Quit

'''
add_menu = '''

1. Print List
2. Add Item
3. Add Multiple Item
4. Main Menu
'''

update_menu = '''
1. Print
2. Update Item
3. Update Multiple
4. Main Menu
'''
delete_menu = '''
1. Print Items
2. Delete an Item
3. Delete Multiple Items
4. Return to Main Menu
'''

item_status_menu = '''
1. Add to List of Acquired Items
2. Main Menu
'''

#PUT CODE FOR EACH MENU IN A FUNCTION, THEN CALL FUNCTION LATER AS PART OF PROGRAM FLOW


while True:
    menu_choice = int(input('Please select an option using integer. Then press ENTER. '))
    indexes = range(len(groceries))
    if menu_choice == 1:
        print(groceries)
        print(main_menu)
    if menu_choice == 2:
        print(add_menu)
        add_choice = int(input('Please select an add option using an integer. Then press ENTER. '))
        if add_choice == 1:
            print(groceries)
        if add_choice == 2:
            item = input('What do you need from the store? Type item and press ENTER. ')
            if item == '':                                        #if enter empty string break out of loop // alt: if len(item) == 0
                break        
            else:
                groceries.append(item)
                for i in indexes:
                    print(f'{i}: {groceries[i]}')
        if add_choice == 3:
            while len(groceries) <= 100:
                item = input('What do you need from the store? Type items and press ENTER after each. ')
                if item == '':                                        #if enter empty string break out of loop // alt: if len(item) == 0
                    break        
                else:
                    groceries.append(item)
                    for i in indexes:
                        print(f'{i}: {groceries[i]}')
        if add_choice == 4:
            print(main_menu)
    if menu_choice == 3:
        print(update_menu)
        new_index1 = int(input('Use index number to select first item to replace, using printed list above for reference. '))
        if update_choice == 2:
            if new_index1 > len(groceries):
                print('Index number too high. ')
                print('Re-enter index number. ')
                new_index1 = int(input('Use index number to select first item to replace, using list above for reference. '))
            else:        
                difference = new_index2 - new_index1
                count = 0
                while count <= difference:
                    old_item = groceries[new_index1 + count]                                                
                    new_item = input(f'Name new item to replace {old_item}: ')
                    groceries[new_index1 + count] = new_item                        #new_index1 + count gets to the current index number // sets value of new_item to the current index number
                    count += 1  
                    for i in indexes:
                        print(f'{i}: {groceries[i]}')
        if update_choice == 3:
            new_index1 = int(input('Use index number to select first item to replace, using printed list above for reference. '))
            new_index2 = int(input('Use index number to select last item to replace, using printed list above for reference. New item(s) will replace existing item(s) including this second index number. '))
            if new_index1 > len(groceries):
                print('First index number too high. ')
                print('Re-enter first index number. ')
                new_index1 = int(input('Use index number to select first item to replace, using printed list above for reference. '))           
            elif new_index2 > len(groceries): 
                print('Second index number too high. ')  
                print('Please re-enter second index number.')
                new_index2 = int(input('Use index number to select last item to replace, using printed list above for reference. New item(s) will replace existing item(s) including this second index number. '))
            else:        
                difference = new_index2 - new_index1
                count = 0
                while count <= difference:
                    old_item = groceries[new_index1 + count]                                                
                    new_item = input(f'Name new item to replace {old_item}: ')
                    groceries[new_index1 + count] = new_item                        #new_index1 + count gets to the current index number // sets value of new_item to the current index number
                    count += 1  
                    for i in indexes:
                        print(f'{i}: {groceries[i]}')
        if update_choice == 4:
            print(main_menu)    
    if menu_choice == 4:
        print(delete_menu)
        delete_choice = int(input('Please select a delete option using integer. Then press ENTER. '))
        if delete_choice == 1:
            print(groceries)
        if delete_choice == 2:
            for i in indexes:
                print(f'{i}: {groceries[i]}')
            remove = int(input('Please type index number of menu item to delete, using list above for reference. '))
            if remove > len(groceries):
                print('Index number too high. ')
                print('Re-enter index number. ')
                remove = int(input('Please type index number of menu item to delete, using list above for reference.'))
            else:
                del groceries[remove]
        if delete_choice == 3:
            for i in indexes:
                print(f'{i}: {groceries[i]}')
            remove = int(input('Please type index number of menu item to delete, using list above for reference.'))
            remove2 = int(input('Use index number to select last item to delete, using list above for reference. '))
            if remove > len(groceries):
                print('First index number too high. ')
                print('Re-enter first index number. ')
                remove = int(input('Please type index number of menu item to delete, using list above for reference.'))
            elif remove2 > len(groceries): 
                print('Second index number too high. ')  
                print('Please re-enter second index number.')
                remove2 = int(input('Use index number to select last item to delete, using list above for reference. '))
            else:  
                del groceries [remove : remove2]
                print(groceries)
        if delete_choice == 4:
            print(main_menu)
    if menu_choice == 5:
        print(item_status_menu)
        status_list = []
        for i in indexes:
            print(f'{i}: {groceries[i]}')
        status_menu = int(input('Use index number to select item and change status, using the above list for reference. '))
        if status_menu == 1:
            item_status = input('Please type the name of the item that has been acquired, then press ENTER. ')
            if item == '':                                        #if enter empty string break out of loop // alt: if len(item) == 0
                break        
            else:
                status_list.append(item_status)
                del groceries[item_status]
                for i in indexes:
                    print(f'{i}: {status_list[i]}')
                for i in indexes:
                    print(f'{i}: {status_list[i]}')       
        if status_menu == 2:
            print(main_menu)
    if menu_choice == 6:
        print('Thank you for using the Grocery List App! Mmmbuh-bye.'')
        break
item_status_menu = '''
