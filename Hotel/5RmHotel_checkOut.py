#dictionary of hotel rooms paired with name
hotel = {
    '101': {
    'occupant_name': 'Darlene Alderson',
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


# #guest check-in for room 101
# hotel_101 = {
#     'occupant_name' : 'Elliot Alderson',
#     'occupant_phone' : '555-555-5555',
#     'has_prepaid' : 'False',
# } 

# #sets dictionary above equal to the key 101 in hotel dictionary
# hotel['101'] = hotel_101

# #guest check-in for room 104
# hotel_104 = {
#     'occupant_name': 'Darlene Alderson',
#     'occupant_phone': 1234567891,
#     'has_prepaid' : 'True',           
# }

# #sets dictionary above equal to the key 101 in hotel dictionary
# hotel['104'] = hotel_104



def check_out():
    vacate_room = input('Please enter room to be vacated and press ENTER. ')
    if hotel[vacate_room] == {}:
            print(f'Room {vacate_room} is currently vacant. Please enter another room number. ' '\n')
    else:
        del hotel[vacate_room]['occupant_name']                            #unassign key value pairs from room
        del hotel[vacate_room]['occupant_phone']
        del hotel[vacate_room]['has_prepaid']
        print(f'Room {vacate_room} is now vacant.' '\n')
    for room_number in hotel.keys():  #searches to find vacant/occupied rooms and prints results
        if hotel[room_number] == {}:
            print(f'Room {room_number} is vacant.')
        else:
            print(f'Hotel room {room_number} is occupied.')
check_out()



        # hotel.remove('vacate_room')('occupant_phone')
        # hotel.remove('vacate_room')('has_prepaid')
        # hotel.remove('vacate_room')('occupant_name')
