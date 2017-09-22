from __future__ import print_function
import sys
import os.path

path = '/usr/share/jira/commands.txt'


def create_file():
	file = open(path, "w+")
	file.close()

def get_queries(path=path):
	if not os.path.exists(path):
		create_file()
	file = open(path, "r+")
	commands = file.readlines()
	data = {}
	for line in commands:
		split = line.split(';')
		# removes the trailing newline character
		data[split[0]] = split[1].rstrip()
	return data

def create_query(queryName, query):
	with open(path, 'a+') as f:
		f.write(queryName + ';' + query + '\n')

# Takes a dictionary of queries and loads them into storage
def load_in_queries(queries):
	create_file()
	for key, value in queries.iteritems():
			create_query(key, value)

# Reloads the commands file to only contain the ones set out in the base_commands.txt
def load_in_base():
	queriesBase = get_queries('/home/jira_python/base_commands.txt')
	load_in_queries(queriesBase)