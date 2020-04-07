#function that takes two arguments: a number and a string. Prints the string as many times as number dictates.

def repeat(how_many_times, the_string):
    result = ''

    while how_many_times > 0:
        #print(the_string)
        result += the_string
        how_many_times -= 1

    return result


greeting = repeat(5, 'morning!')
another_greeting = repeat(3, greeting)
print(greeting)
print(another_greeting)


