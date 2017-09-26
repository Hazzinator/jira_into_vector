# required imports
from jira import JIRA
from jira import JIRAError
import getpass
import sys

# Attempts a connection to the specified jira server with the username and password. If
def login():
	print 'What is your Atlassian login? e.g. harry.bassettbutt@gohubble.com: '
	username = raw_input()
	# password is entered securely
	password = getpass.getpass(prompt='What is your password? : ')
	# sets up the server to connect to
	jira_options = {'server': 'https://insightsoftware.atlassian.net'}
	jira = None
	try:
		# uses the basic authentication to login to the jira server and return a jira object
		jira = JIRA(options=jira_options, basic_auth=('harry.bassettbutt@gohubble.com', 'golden halo power'))
	except JIRAError as e:
		print 'Login error - did you enter the right credentials?'
		pass
		# exception not handled as only a print out is needed		
	return jira
	
