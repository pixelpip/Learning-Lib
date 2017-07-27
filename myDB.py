# myDB.py   https://www.youtube.com/watch?v=o-vsdfCBpsU&list=PLQVvvaa0QuDezJh0sC5CqXLKZTSKU1YNo
import sqlite3

connection = sqlite3.connect('tutorial.db')
cursor = connection.cursor()


def create_table():
	cursor.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)")

def data_entry():
	cursor.execute("INSERT INTO stuffToPlot VALUES(2313123542, '2017-01-01', 'Python', 30)")
	connection.commit()
	cursor.close()

#create_table()
data_entry()