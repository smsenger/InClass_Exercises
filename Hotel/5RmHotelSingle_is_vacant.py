#dictionary of hotel rooms paired with empty dict
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
single_is_vacant()







