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




empty_room = {}
#function that lists vacancy status of all rooms
def is_vacant():
    for room_number in hotel.keys():
        if hotel[room_number] == empty_room:
            print(f'Room {room_number} is vacant.')
        else:
            print(f'Hotel room {room_number} is occupied.')

is_vacant()




#function that checks guests out of hotel, asking for room, checking for occupancy, then printing updated hotel data
empty_room = {}
def check_out():
    while True:
        try: 
            # vacate_room = input('Please enter room to be vacated and press ENTER. ')
            vacate_room = input('Please enter room to be vacated and press ENTER. ')
            if hotel[vacate_room] == empty_room:
                print(f'Room {vacate_room} is currently vacant. Please enter another room number. ')
                print()
                return check_out()
            else: 
                del hotel[vacate_room]['occupant_name']           #unassign key value pairs from room
                del hotel[vacate_room]['occupant_phone']
                del hotel[vacate_room]['has_prepaid']
                print(f'Room {vacate_room} is now vacant.')
                print()
            break    
        except:
            print('Invalid room number.')
            
    print('VACANCY STATUS:')    
    is_vacant() #searches to find vacant/occupied rooms and prints results -- verifies changes

check_out()


