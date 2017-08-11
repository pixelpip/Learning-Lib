
import sqlite3
import time
import datetime
import random
import sys

#dictionary 
from pw_dict_source_v01 import pword_dict

connection = sqlite3.connect('pwdb.db')
cursor = connection.cursor()

def create_table():
	cursor.execute("CREATE TABLE IF NOT EXISTS pwdb(company TEXT, username TEXT, login TEXT, password TEXT)")

def dynamic_data_entry():
	for keys in pword_dict.keys():
		company = keys
		username = pword_dict[keys]['username']
		login = pword_dict[keys]['login']
		password = pword_dict[keys]['password']
		print ('company = ', company)
		cursor.execute("INSERT INTO pwdb (company, username, login, password) VALUES (?, ?, ?, ?)", 
			(company, username, login, password))
	connection.commit()

create_table()
dynamic_data_entry()

cursor.close()
connection.close()



















