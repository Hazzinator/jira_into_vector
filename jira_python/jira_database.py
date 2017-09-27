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
	except sqlite3.OperationalError as e:
		print e
		print '-Table '+ tableName + ' could not be dropped-'

# All issues have the same fields, so the only customisable aspect is the name of the table
# Protect against injection?
def create_table(tableName):
	try:
		cursor.execute('''CREATE TABLE ''' + tableName + '''(snapshot_date DATETIME, 
		key VARCHAR(12) PRIMARY KEY, summary VARCHAR(5000), status VARCHAR(20), 
		assignee VARCHAR(50), priority VARCHAR(20), created DATETIME, 
		hubble_team VARCHAR(100), last_updated DATETIME)''')
		print '-Table ' + tableName + ' created-'
	except sqlite3.OperationalError as e:
		print '-Table ' + tableName + ' could not be created'

def recreate_table(tableName):
	drop_table(tableName)
	create_table(tableName)

# Returns a list of all tables in the database at the moment
def get_table_names():
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
	return cursor.fetchall()

# Updates the issues in a table.
# An issue should be in the form (date, key, summary, status, assignee, priority, created, hubble_team, last_updated)
def update_table(tableName, issues):
	recreate_table(tableName)
	# executemany will perform an SQL action on all items of a list
	cursor.executemany('''INSERT INTO '''+tableName+'''(snapshot_date, key, summary, status, assignee, priority, created, hubble_team, last_updated) 
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', issues)
	print '-Table '+ tableName + ' updated-'

