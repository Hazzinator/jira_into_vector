from __future__ import print_function
import sys
import os.path

# Opens a new file, overwriting any existing one in the directory. Requires full path
def create_file(file):
	file = open(file, "w+")
	file.close()

# Gets the queries from a text file specified by a parameter.
def get_queries(commandFile):
	if not os.path.exists(commandFile):
		create_file(commandFile)
	file = open(commandFile, "r+")
	commands = file.readlines()
	data = {}
	for line in commands:
		split = line.split(';')
		# removes the trailing newline character
		data[split[0]] = split[1].rstrip()
	return data

# Creates a new query with a query name in the custom text file
def create_query(queryName, query, userCommands):
	with open(userCommands, 'a+') as f:
		f.write(queryName + ';' + query + '\n')

# Takes a dictionary of queries and loads them into storage
def load_in_queries(queries, userCommands):
	create_file(userCommands)
	for key, value in queries.iteritems():
			create_query(key, value, userCommands)

# Reloads the commands file to only contain the ones set out in the base_commands.txt
def load_in_base(baseCommands, userCommands):
	queriesBase = get_queries(baseCommands)
	load_in_queries(queriesBase, userCommands)