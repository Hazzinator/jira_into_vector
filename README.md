This tool comes in two parts:

1. A docker container that runs a script to return the results of a JQL query and store them on the host computer 
in the form of .csv files. This will be accomplished using a shared docker volume.
2. A script that will automatically move .csv files onto the Accelerator, and then runs a script that will import 
them into the database.

For the second script to work, it requires that you store the public SSH key of your workstation on your Accelerator.
A public key can be generated via PuTTY on a Windows machine, and through the ssh command on a Linux machine. 

The public key should be stored in the ~/.ssh/authorized-keys file on the Accelerator.
