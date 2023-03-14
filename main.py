import pyshorteners
import hashlib
import re as r


def check_name(n):
	run = r'\b[A-Za-z]{1,25}[A-Za-z]{1,25}\b'
	if r.match(run, n):
		return
	else:
		print('Invalid name format!')
		signup()


def check_mail(m):
	pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
	if r.match(pat, m):
		return
	else:
		print('Invalid mail format!')
		signup()


def password_check(a):
	regex = r'\b(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[@$!%*#?&+-]){8,}\b'
	if r.match(regex, a):
		return
	else:
		print('Password must contain at least one lowercase letter,'
			  'one uppercase letter, one special symbol,'
			  'and one numeric value')
		signup()


def signup():
	name = input('Your name please: ')
	check_name(name)
	mail = input('Please enter your email address: ')
	check_mail(mail)
	pwd = input('Please enter your password: ')
	password_check(pwd)
	conf_pwd = input('Confirm password: ')

	if conf_pwd == pwd:
		nam = name.encode()
		enc = conf_pwd.encode()
		hash1 = hashlib.md5(enc).hexdigest()
		hash2 = hashlib.md5(nam).hexdigest()
		with open("credentials.txt", "w") as f:
			f.write(mail + "\n")
			f.write(hash1 + "\n")
			f.write(hash2)
			f.close()
		print('Profile created!')
		login()
	else:
		print('Inconsistent password!!!')
		signup()


def login():
	name = input('Your name please: ')
	mail = input('Please enter your email address: ')
	pwd = input('Please enter your password: ')

	auth_name = name.encode()
	auth = pwd.encode()
	auth_hash = hashlib.md5(auth).hexdigest()
	names = hashlib.md5(auth_name).hexdigest()
	with open("credentials.txt", "r") as f:
		stored_mail, stored_pwd, stored_name = f.read().split("\n")
		f.close()

	if mail == stored_mail and auth_hash == stored_pwd and names == stored_name:
		print('Welcome' + ' ' + name + '! Please enter the URL you wish to shorten below')
		url = input("Enter the url you wish to shorten: ")

		type_tiny = pyshorteners.Shortener()
		short_url = type_tiny.tinyurl.short(url)

		print("Your short url is " + short_url)
		return
	else:
		print('Invalid credentials!!')
		login()

signup()