This tool comes in two parts:

1. A docker container that runs a script to return the results of a JQL query and store them on the host computer 
in the form of .csv files. This will be accomplished using a shared docker volume.
2. A script that will automatically move .csv files onto the Accelerator, and then runs a script that will import 
them into the database.

REST API
Stateless, rather than having to share the state of the webpage with every client who wants to connect to it.
Read up on it

Ghetto Solution
To get step two working, a simple script will have to be made that will allow the user to enter their username and
password, and then copy the entire shared Docker directory to the Accelerator. Then, a script will have to be ran
on the accelerator that creates a new schema for the files to exist under. It will then import all of the .csv files
into the database using the vwword command. A script should be made that loops through all the names (.csv) and runs
the script on them with the correct schema.

