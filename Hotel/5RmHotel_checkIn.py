#dictionary of hotel rooms paired with name
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

def check_in():
    for room_number in hotel.keys():  #searches to find vacant/occupied rooms and prints results
        if hotel[room_number] == {}:
            print(f'Room {room_number} is vacant.')
            
        else:
            print(f'Hotel room {room_number} is occupied.')
    select_room = input('Please type a room number from available options and press ENTER. ')
    if hotel[select_room] == {}:
        occupant_name = input('Please enter customer name, then press ENTER. ')
        occupant_phone = int(input('Please enter ten-digit customer phone number, then press ENTER. '))
        has_prepaid = input('Please enter True if customer has prepaid or False if not, then press ENTER. ')
        hotel[select_room]['occupant_name'] = [occupant_name]
        hotel[select_room]['occupant_phone'] = [occupant_phone]
        hotel[select_room]['has_prepaid'] = [has_prepaid]
        print('Information has been saved.')
        print(hotel)
    else:
        print('Please select another room.' '\n')
        return check_in()



    

check_in()
