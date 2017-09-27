import sys
import os
import query_parser
import jira
import jira_login
import jira_query
import jira_database
import subprocess

def start():
	# list of options []
	inloop = True
	while (inloop):
		print '\nType help for a list of commands.'
		sys.stdout.write(': ')
		data = raw_input()
		# Parse out arguments
		inloop = check_input(data)

def exit():
	sys.exit(0)

def print_queries():
	queries = query_parser.get_queries()
	for key, value in queries.iteritems():
		print key

def printj_queries():
	queries = query_parser.get_queries()
	for key, value in queries.iteritems():
		print key
		print value
		print

def display_help():
	print '\nexit : exits the program'
	print 'print : displays the queries that can be ran'
	print 'printj : displays the queries along with their JQL commands'
	print 'run "name" : runs the query where name is the name of the query to run'
	print 'delete "name" : deletes the query with the specified name'
	print 'reload : loads a default set of queries into the query storage'
	print 'list : lists the names of all the tables currently in the database file'
	print 'drop "table": drops a table in the database'
	print 'export : exports the db file into multiple csv files'
	print 'bash : execute a shell on the container'

# Runs the command to query the JQL server to retrieve the issues
def run_query(queryName):
	queries = query_parser.get_queries()
	try:
		query = queries[queryName]
		jira_query.run_command(jira, queryName, query)
	except KeyError:
		print 'A query by that name does not exist, please type in print_q to see the list of queries.'

# Runs the command to store a new text file
def run_create(queryName):
	print 'Creating a query with name -' + queryName + '-'
	print 'Please enter the JQL statement to bind to it below:'
	query = raw_input()
	print 'The query you entered is:'
	print query
	print '\nIs this correct? (y/n)'
	answer = raw_input()
	if answer == 'Y' or answer == 'y':
		query_parser.create_query(queryName, query)

def run_reload():
	print 'Are you sure you want to reload default queries? (y/n)'
	answer = raw_input()
	if answer == 'y' or answer == 'Y':
		print '-Reloading default queries-'
		query_parser.load_in_base()
		print '-Default list loaded-'

# Deletes a stored query 
# Rather than finding the query in the file and removing it, the file is recreated and all the queries are written back in again
# but without the deleted one 
def run_delete(queryName):
	queries = query_parser.get_queries()
	# Attempt to remove the query with that name from the internal dictionary
	if queries.pop(queryName, None) is None:
		print 'A query by that name does not exist, please type in print to see the list of available queries.'
	else:
		query_parser.load_in_queries(queries)
		print queryName + ' has been deleted'

# Exports the .db file into .csv files. Calls a library script
def run_export():
	print 'Exporting database to csv files in volume: /usr/share/jira'
	output = subprocess.call(["/lib/convert-db-to-csv/convert-db-to-csv.sh", "/usr/share/jira/database.db", "/usr/share/jira"])
	print "Export exited with code: " + str(output)

def run_list():
	print 'Fetching list of all tables:'
	tables = jira_database.get_table_names()
	for table in tables:
		print table.__str__().strip("'()[],")[2:]

# Removes a table in the database file
def run_drop(tableName):
	jira_database.drop_table(tableName)

# Exports the .db file into .csv files
def run_bash():
	output = subprocess.call('/bin/sh', shell=True)

# Checks that the second argument is not just '' and then runs a method
def second_arg_check(split, methodToRun):
	if len(split) > 1:
		secondArg = split[1]
		if secondArg != '':
			methodToRun(secondArg)
	else:
		print 'Format is wrong for command ' + split[0]

# Splits up the arguments of the input and checks them
def check_input(data):
	split = data.split(" ")
	firstArg = split[0]
	if firstArg == 'exit':
		return False
	elif firstArg == 'help':
		display_help()
	elif firstArg == 'print':
		print_queries()
	elif firstArg == 'reload':
		run_reload()
	elif firstArg == 'printj':
		printj_queries()
	elif firstArg == 'export':
		run_export()
	elif firstArg == 'bash':
		run_bash()
	elif firstArg == 'drop':
		second_arg_check(split, run_drop)
	elif firstArg == 'list':
		run_list()
	elif firstArg == 'run':
		second_arg_check(split, run_query)
	elif firstArg == 'create':
		second_arg_check(split, run_create)
	elif firstArg == 'delete':
		second_arg_check(split, run_delete)
	return True

jira = jira_login.login()
start()
