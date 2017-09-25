import sqlite3
import sys
import csv

connection = sqlite3.connect("/usr/share/jira/database.db", isolation_level=None)
cursor = connection.cursor()

# Drops a table with the specificed table name (if it exists)
def drop_table(tableName):
	try:
		cursor.execute('''DROP TABLE '''+tableName)
		print '-Table ' + tableName + ' dropped-'
	except sqlite3.OperationalError:
		print '-Table '+ tableName + ' does not exist-'

# All issues have the same fields, so the only customisable aspect is the name of the table
# Protect against injection?
def create_table(tableName):
	try:
		cursor.execute('''CREATE TABLE ''' + tableName + '''(snapshot_date VARCHAR(100), 
		key VARCHAR(12) PRIMARY KEY, summary VARCHAR(5000), status VARCHAR(20), 
		assignee VARCHAR(50), priority VARCHAR(20), created VARCHAR(100), 
		hubble_team VARCHAR(100), last_updated VARCHAR(100))''')
		print '-Table ' + tableName + ' created-'
	except sqlite3.OperationalError:
		print '-Table ' + tableName + ' already exists'


#def create_table(tableName):
#	with open(tableName+".csv", 'wb') as file:
#		wr = csv.writer(file, quoting=csv.QUOTE_ALL)
#		wr.writerow(mylist)

def recreate_table(tableName):
	drop_table(tableName)
	create_table(tableName)

# Updates the issues in a table.
# An issue should be in the form (date, key, summary, status, assignee, priority, created, hubble_team, last_updated)
def update_table(tableName, issues):
	recreate_table(tableName)
	# executemany will perform an SQL action on all items of a list
	print issues
	cursor.executemany('''INSERT INTO '''+tableName+'''(snapshot_date, key, summary, status, assignee, priority, created, hubble_team, last_updated) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', issues)
	print '-Table '+ tableName + ' updated-'

