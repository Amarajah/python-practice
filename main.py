print('Welcome, please create your personalized account')
username = input('Enter your preferred username: ')
password = input('Your preferred password please: ')

print('Hey there, you now have a personal account with us')
print('You may log in now')

username1 = input('Please enter your username: ')
password1 = input('Your password please: ')

if username == username1 and password == password1:
    print('Login successful')
else:
    print('Invalid credentials')
