# required imports
from jira import JIRA
from jira import JIRAError
from time import gmtime, strftime
import datetime
import getpass
import sys
import jira_database as database

# runs a jql command and updates the corresponding database
def run_command(jira, queryName, query):
	# query is in the form of a tuple - change to a class later
	# query[1] is the JQL query
	issues = jql_search(query, jira)
	length = len(issues)			
	if (length != 0):
		# query[0] is the name of the jql query and also the name of the table in the database
		formattedIssues = parse_issues(issues)
		database.update_table(queryName, formattedIssues)

# If the object is none 
def none_creator(field, property):
	if field is None:
		return None
	else:
		return getattr(field, property)

# Converts an ISO-8601 date into a valid SQL date format
def datetime_format(date):
	# x[2:] cut off the first two characters
	# x[:2] cut off everything but the first two characters
	dateStart = date[:10]
	dateEnd = (date[11:])[:8]
	dateNew = dateStart + " " + dateEnd
	return dateNew

# parses a list of issues into a list of tuples that can be inserted straight into a database
def parse_issues(issues):
	# the tuple list to return
	issueList = []
	snapshot = create_snapshot()
	tformat = True
	for issue in issues:
		fields = issue.fields
		key = issue.key
		summary = fields.summary
		assignee = none_creator(fields.assignee, 'displayName')
		priority = none_creator(fields.priority, 'name')
		status = none_creator(fields.status, 'name')
		hubbleTeam = fields.project.name
		# both of these are in ISO 8601 format
		lastUpdated = datetime_format(fields.updated)
		created = datetime_format(fields.created)
		issueList.append((snapshot, key, summary, status, assignee, priority, created, hubbleTeam, lastUpdated))
	return issueList

# creates a string in the form of a date that is used to identify when this code was last run
def create_snapshot():
	return strftime("%Y-%m-%d %H:%M:%S", gmtime())

# Returns a list of issues specified by a JQL query. If the JQL Query is incorrect then it won't return anything
def jql_search(query, jira):
	blockSize = 100
	blockNum = 0
	issues = []
	issuesLen = 0
	try:
		while True:
			startIdx = blockNum*blockSize
			# can return a maximum of 100 at a time, has to be run multiple times to populate a list
			searchedIssues = jira.search_issues(query, startIdx, blockSize)
			searchedLen = len(searchedIssues)
			print 'Searching in progress [' + str(issuesLen) + ']...'	
			if searchedLen == 0:
				break;
			# keep a tally of the number of items returned in total after each run
			issuesLen += searchedLen
			# add the contents of the searched list to the main list
			issues += searchedIssues
			blockNum += 1
		print 'JQL Search completed. Issues found: ' + str(issuesLen)
	except JIRAError as e:
		print(e.text)
	return issues
