import sqlite3
import sys

def create_connection():
	connection = sqlite3.connect("/usr/share/jira/database.db")
	return connection

def create_cursor(connection):
	cursor = connection.cursor()
	return cursor

def recreate_table(cursor, tableName):
	# a cursor can perform actions on a database connection
	try:
		cursor.execute('''DROP TABLE '''+tableName)
		print '-Table ' + tableName + ' dropped-'
	except sqlite3.OperationalError:
		print '-Table '+ tableName + ' does not exist-'
	cursor.execute('''CREATE TABLE ''' + tableName + '''(snapshot_date VARCHAR(100), 
	key VARCHAR(12) PRIMARY KEY, summary VARCHAR(5000), status VARCHAR(20), 
	assignee VARCHAR(50), priority VARCHAR(20), created VARCHAR(100), 
	hubble_team VARCHAR(30), last_updated VARCHAR(100))''')
	print '-Table '+ tableName + ' created-'

# Updates the issues in a table.
# An issue should be in the form (date, key, summary, status, assignee, priority, created, hubble_team, last_updated)
def update_table(tableName, issues):
	connection = create_connection()
	cursor = create_cursor(connection)
	recreate_table(cursor, tableName)
	# executemany will perform an SQL action on all items of a list
	cursor.executemany('''INSERT INTO '''+tableName+''' (snapshot_date, key, summary, status, assignee, priority, created, hubble_team, last_updated) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', issues)
	print '-Table '+ tableName + ' updated-'
