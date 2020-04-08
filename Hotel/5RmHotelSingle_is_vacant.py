#dictionary of hotel rooms paired with empty dict
hotel = {
    '101': {},
    '102': {},
    '103': {},
    '104': {},
    '105': {},
}


#guest check-in for room 101
hotel_101 = {
    'occupant_name' : 'Elliot Alderson',
    'occupant_phone' : '555-555-5555',
    'has_prepaid' : 'False',
} 

#sets dictionary above equal to the key 101 in hotel dictionary
hotel['101'] = hotel_101

#guest check-in for room 104
hotel_104 = {
    'occupant_name': 'Darlene Alderson',
    'occupant_phone': 1234567891,
    'has_prepaid' : 'True',           
}

#sets dictionary above equal to the key 101 in hotel dictionary
hotel['104'] = hotel_104


#function that checks if a particular room is vacant
def is_vacant():
    hotel_room = input('Please enter room number to search and press ENTER. ')
    if hotel[hotel_room] == {}:
        print(f'Room {hotel_room} is vacant.')
    else:
        print(f'Hotel room {hotel_room} is occupied.')

is_vacant()

