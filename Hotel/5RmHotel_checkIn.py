#dictionary of hotel rooms paired with name
hotel = {
    '101': {
    'occupant_name' : 'Elliot Alderson',
    'occupant_phone' : '555-555-5555',
    'has_prepaid' : 'False',
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


#function that checks in hotel guests, asking for name, phone number, and prepay status
empty_room = {}
def check_in():      #in combined version, call is_vacant instead of using this code
empty_room = {}
#function that lists vacancy status of all rooms
def is_vacant():
    for room_number in hotel.keys():
        if hotel[room_number] == empty_room:
            print(f'Room {room_number} is vacant.')
        else:
            print(f'Hotel room {room_number} is occupied.')
# is_vacant()



    # for room_number in hotel.keys():  #searches to find vacant/occupied rooms and prints results for entire hotel
    #     if hotel[room_number] == empty_room:
    #         print(f'Room {room_number} is vacant.')   
    #     else:
    #         print(f'Hotel room {room_number} is occupied.')
    is_vacant()
    select_room = input('Please type a room number from available options and press ENTER. ' '\n').strip()
    while True:
        try:  
            if hotel[select_room] == empty_room:           #if the room is empty, enter customer name
                occupant_name = input('Please enter customer name, then press ENTER. ' '\n').strip()   #ensures that name is alpha and spaces
                if all(x.isalpha() or x.isspace() for x in occupant_name):
                    hotel[select_room]['occupant_name'] = [occupant_name]
                else: 
                    occupant_name = input('Please type name again, using only letters and spaces. ' '\n').strip() #prompts for correct response
                    hotel[select_room]['occupant_name'] = [occupant_name]   #need code for further bad user input...            
            else:
                return check_in()                                       #runs function from beginning if occupied room selected
            break                                          
        except:
            print('Please select a valid room number. ' '\n')     #if not a valid room number, prints this message
            return check_in()                                     #runs function from beginning

    occupant_phone = input('Please enter ten-digit customer phone number without dashes, then press ENTER. ').strip() #need to learn how to include dashes as string
    if occupant_phone.isdigit() == True  and len(occupant_phone) == 10:  
        hotel[select_room]['occupant_phone'] = [occupant_phone]
    else:
        occupant_phone = int(input('Please enter a valid ten-digit number without dashes. ')).strip()
        hotel[select_room]['occupant_phone'] = [occupant_phone]    #need code for further bad user input

    has_prepaid = input('Please enter True if customer has prepaid or False if not, then press ENTER. ').strip()
    if has_prepaid == 'True' or has_prepaid == 'False':
        hotel[select_room]['has_prepaid'] = [has_prepaid]
        print('Information has been saved.')
        print(hotel)
    else:
        has_prepaid = input('Please enter True or False to indicate payment status. ').strip()
        hotel[select_room]['has_prepaid'] = [has_prepaid]
        print('Information has been saved.')
        print(hotel)                                    #need code for further bad user input


check_in()




