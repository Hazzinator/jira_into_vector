@ECHO OFF
PowerShell.exe -Command "docker run -v /c/Docker/jira:/usr/share/jira/ -it jira_python python /home/jira_python"
PAUSE