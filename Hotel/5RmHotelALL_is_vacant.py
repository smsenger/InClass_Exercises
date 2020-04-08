

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


#function that lists vacancy status of all rooms
def is_vacant():
    for room_number in hotel.keys():
        if hotel[room_number] == {}:
            print(f'Room {room_number} is vacant.')
        else:
            print(f'Hotel room {room_number} is occupied.')
    #print(hotel)

is_vacant(hotel)






#ORIGINAL EXERCISE:
#hotel has 5 rooms
#names of rooms: 101, 102, 103, 104, 105
#store occupant name for each of the rooms
#use one dictionary to hold this information
#make sure you can 
    #put someone in an unoccupied room
    #make a room available by setting the occupant name to ''
    #check if a room number is valid
    #check if a room is occupied or not
#code to run in REPL:
# hotel['101'] = 'Rob'
# hotel['102'] = 'Rick'
# hotel['103'] = 'Rock'
# hotel['104'] = 'Rod'
# hotel['105'] = 'Rhett'
# hotel['105'] = ''
# hotel['101']
# hotel['101'] = []
# if hotel['104'] != '':
#     print('This room is unoccupied.')
# else:
#     print('This room is occupied.')