FROM ubuntu:latest

# Install packages
RUN apt-get update
RUN apt-get install -y python
RUN apt-get install -y python-pip
RUN apt-get install -y git
RUN apt-get install -y sqlite3 libsqlite3-dev

# Update packages on subsequent runs
RUN apt-get upgrade -y

# Update to latest pip version
RUN pip install --upgrade pip

# Install jira api
RUN pip install jira schedule

# Install our python code
RUN mkdir -p /home/jira_python

# Install the database to csv code
RUN git clone https://github.com/Hazzinator/convert-db-to-csv.git /lib/convert-db-to-csv

# Copy the jira_python code into the correct directory
COPY jira_python /home/jira_python

# Giving execute permissions to our code
RUN chmod +x /home/jira_python
