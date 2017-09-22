@ECHO OFF
PowerShell.exe -Command "docker run -v /c/Docker/esdata:/usr/share/jira/ -it jira_python python /home/jira_python"
PAUSE