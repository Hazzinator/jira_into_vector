@ECHO OFF
if not exist "C:\Docker\jira" mkdir C:\Docker\jira
PowerShell.exe -Command "docker run -v /c/Docker/jira:/usr/share/jira/ -it jira_python python /home/jira_python"
PAUSE