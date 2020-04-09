#function that starts with empty dict, takes user input, uses for loop to match up dict key to value(data from user input)
#needs hardening to prepare for incorrect user inputs
def hotel_data():    
    hotel = {}
    hotel['room_num'] = int(input('Please select a room number for customer and press ENTER. '))
    hotel['cust_name'] = input('Please type the name of customer and press ENTER. ')
    hotel['cust_phone'] = int(input('Please type the ten-digit phone number of customer wihout dashes or spaces and press ENTER. '))
    hotel['cust_prepay'] = input('please type True if customer has prepaid or False if customer has not prepaid. ')
    for key in hotel.keys():                #for each of hotel['keyName'] in this dict, run through all keys
        print(f'{key}: {hotel[key]}')       #print the key itself, colon, and corresponding value for that key

hotel_data()