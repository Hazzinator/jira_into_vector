This tool comes in two parts:

1. A docker container that runs a script to return the results of a JQL query and store them inside a folder in the 
container. This folder will have to be set up as a volume so the data is persistent and can be accessed from the 
host machine. The results will be put into database file. Using the export command, the program can export one table
at a time or all the tables into .csv files.
2. A script that will automatically move .csv files onto the Accelerator, provided you have the username, password
and ip address of the Accelerator.

From there, another script will have to be executed that will import those csv files into vector. The script and its
corresponding README can be found on the following repository:
https://github.com/Hazzinator/create_table_in_vector
