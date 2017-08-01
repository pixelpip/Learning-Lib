import sys

rk='email'
moto='email_2'

pword_dict={'anaconda': {'username': 'none', 'login': rk, 'password': 'supersecretpassword'},
		    'bank': {'username': 'none', 'login': rk, 'password': 'secretPassword'}}


def pword(company):
	matched = 'not found'       #set sentry variable 
	for keys in pword_dict.keys():
		if keys.startswith(company):
			matched = 'found'	#set sentry to matched
			print(keys, '\n',  
					  'Username:', pword_dict[keys]['username'], '\n',
					  'login:', pword_dict[keys]['login'], '\n',
					  'password:', pword_dict[keys]['password'], '\n')
	if matched == 'not found':
		print ("not match found")

try:
	pword(sys.argv[1])
except:
	print ("error:--> ::nothing entered::")

