import datetime
from datetime import date

'''
    This function allows user choose what kind of meal they'd like.
'''

def restaurant():
    print('Hola!!! Welcome to Nio\'s kitchen')
    print('We have an array of dishes both local and international, you could book a seat in advance or order takeout')
    print('So what would you like to order today?')
    print('1. Local dishes')
    print('2. Intercontinental dishes')
    meal = input('Please pick an option: ')
    if meal == 1:
        local()
    elif meal == 2:
        foreign()
    else:
        print('Invalid value!!!!')
        restaurant()

    ''' 
        Function to be executed if the user chooses local meals.
    '''

def local():
    print('1. Bitterleaf soup and fufu  ----- #5000')
    print('2. Amala and ewedu with gbegiri ----- #5000')
    print('3. Beans and bread with peppered ponmo----- #3000')
    print('4. Oha soup with pounded yam ----- #5000')
    print('5. Roasted plantains and BBQ fish -----#4000')
    local_dish = input('Please pick an option: ')
    if local_dish == 1:
        order()
    elif local_dish == 2:
        order()
    elif local_dish == 3:
        order()
    elif local_dish == 4:
        order()
    elif local_dish == 5:
        order()
    else:
        print('Pick a valid option!!')
        local()

    ''' 
        Function to be executed if the user chooses foreign meals.
    '''

def foreign():
    print('1. Fried rice, peppered beef and salad  ----- #8000')
    print('2. Caesar salad with olive oil dressing ----- #11000')
    print('3. Brussel sprouts ----- #5000')
    print('4. Beef Burger ----- #3000')
    print('5. Chinese rice and singapore noodles ----- #15000')
    dish = input('Please pick an option: ')
    if dish == 1:
        order()
    elif dish == 2:
        order()
    elif dish == 3:
        order()
    elif dish == 4:
        order()
    elif dish == 5:
        order()
    else:
        print('Pick a valid option!!')
        foreign()

''' Function called when someone wants to either reserve a seat or order online.'''

def order():
    print('Would you like to reserve a seat?: ')
    print('1. Yes')
    print('2. No')
    seat  = int(input('Please input here: '))
    if seat == 1:
        reserve()
    elif seat == 2:
        takeout()
    else:
        print('Please choose a valid option')

''' Function called when someone wants to reserve a seat.'''

def reserve():
    day = int(input('Pick a date: '))
    month = int(input('What month : '))
    year = int(input('Year: '))
    d = datetime.date(year, month, day)
    print(d)
    time = int(input('Time: '))
    if time in range(0, 25):
        print(f'You booked a seat for {d} at {time} o\'clock. We\'d be expecting you. Do have a lovely day')
    else:
        print('Invalid time format!!!!!')
        reserve()

''' Function called when someone wants to order takeout.'''

def takeout():
    address = input('Please type your address: ')
    print('Please make a transfer to this account number and type in the 4-digit token you received ')
    print('123456789 \n Xyz bank \n Nio\'s store')
    token =int(input('Input your token: '))
    if token in range(1000, 2555):
        print('Verified!')
        print('Please note that delivery takes between 1-3 hours depending on your location')
        print('Thanks for coming, we do hope to see you again!')
    elif token in range(2999, 4000):
        print('Verified!')
        print('Please note that delivery takes between 1-3 hours depending on your location')
        print('Thanks for coming, we do hope to see you again!')
    else:
        print('Invalid token!!!. Try again')
        takeout()

restaurant()