#This function prompts user for an input to select a function to run. Upon input of a valid number, runs corresponding function. If number not valid, runs function again.
#Functions called in the first function preceed this program's function call.



#dictionary of hotel rooms paired with name
#some rooms pre-populated to check function in isolation
hotel = {
    '101' : {'occupant_name': 'Darlene Alderson',
    'occupant_phone': 1234567891,
    'has_prepaid' : 'True',           
},
    '102': {},
    '103': {},
    '104': {
    'occupant_name': 'Darlene Alderson',
    'occupant_phone': 1234567891,
    'has_prepaid' : 'True',           
},
    '105': {},
}




#Functions called in last function:

empty_room = {}
#function that lists vacancy status of all rooms
def is_vacant():
    for room_number in hotel.keys():
        if hotel[room_number] == empty_room:
            print(f'Room {room_number} is vacant.')
        else:
            print(f'Hotel room {room_number} is occupied.')
# is_vacant()


#function that checks in hotel guests, asking for name, phone number, and prepay status
empty_room = {}

def check_in():      
    is_vacant()

    select_room = input('Please type a room number from available options and press ENTER. ' '\n').strip()
    while True:
        try:  
            if hotel[select_room] == empty_room:           #if the room is empty, enter customer name
                occupant_name = input('Please enter customer name, then press ENTER. ' '\n')   #ensures that name is alpha and spaces
                if all(x.isalpha() or x.isspace() for x in occupant_name):
                    hotel[select_room]['occupant_name'] = [occupant_name]
                else: 
                    occupant_name = input('Please type name again, using only letters and spaces. ' '\n') #prompts for correct response
                    hotel[select_room]['occupant_name'] = [occupant_name]   #need code for further bad user input...            
            else:
                return check_in()                                       #runs function from beginning if occupied room selected
            break                                          
        except:
            print('Please select a valid room number. ' '\n')     #if not a valid room number, prints this message
            return check_in()                                     #runs function from beginning

    occupant_phone = input('Please enter ten-digit customer phone number without dashes, then press ENTER. ') #need to learn how to include dashes as string
    if occupant_phone.isdigit() == True  and len(occupant_phone) == 10:  
        hotel[select_room]['occupant_phone'] = [occupant_phone]
    else:
        occupant_phone = int(input('Please enter a valid ten-digit number without dashes. '))
        hotel[select_room]['occupant_phone'] = [occupant_phone]    #need code for further bad user input

    has_prepaid = input('Please enter True if customer has prepaid or False if not, then press ENTER. ')
    if has_prepaid == 'True' or has_prepaid == 'False':
        hotel[select_room]['has_prepaid'] = [has_prepaid]
        print('Information has been saved.')
        print(hotel)
    else:
        has_prepaid = input('Please enter True or False to indicate payment status. ')
        hotel[select_room]['has_prepaid'] = [has_prepaid]
        print('Information has been saved.')
        print(hotel)                                    #need code for further bad user input
# check_in()



#funciton that checks guests out of hotel, asking for room, checking for occupancy, then printing updated hotel data
empty_room = {}
def check_out():
    while True:
        try: 
            # vacate_room = input('Please enter room to be vacated and press ENTER. ')
            vacate_room = input('Please enter room to be vacated and press ENTER. ')
            if hotel[vacate_room] == empty_room:
                print(f'Room {vacate_room} is currently vacant. Please enter another room number. ')
                return check_out()
            else: 
                del hotel[vacate_room]['occupant_name']           #unassign key value pairs from room
                del hotel[vacate_room]['occupant_phone']
                del hotel[vacate_room]['has_prepaid']
                print(f'Room {vacate_room} is now vacant.' '\n')
            break    
        except:
            print('Invalid room number.')
            
    print('VACANCY STATUS:')    
    is_vacant()
# check_out()



empty_room = {}
#function that checks if a particular room is vacant
def single_is_vacant():
    while True:
        try:
            hotel_room = input('Please enter room number to search and press ENTER. ')
            if hotel[hotel_room] == empty_room:
                print(f'Room {hotel_room} is vacant.')
            else:
                print(f'Hotel room {hotel_room} is occupied.')
            break
        except:
            print('Invalid room number. ')
# single_is_vacant()



def hotel_functions():
    #input: ask what they want to do
    user_instruction = input('''Please select a function from those below. Type the corresponding number and press ENTER. 
    1. Check all vacancies
    2. Check room occupancy status
    3. Customer check-in
    4. Customer check-out     
    ''')

    if user_instruction == '1':                                #if user input == check all vacancies, run function 
        return is_vacant()    
                                                         
    elif user_instruction == '2':                              #if user input == check specific room, run function
        single_is_vacant()
    
    elif user_instruction == '3':
        check_in()                                             #if user input == check in, run check_in()
    
    elif user_instruction == '4':                              #if user input == check out, run check_out()
        check_out()
    
    else:
        print('Please select from available options')
        hotel_functions()
    print('Have a nice day!')

hotel_functions()
    