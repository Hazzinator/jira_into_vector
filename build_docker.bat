@ECHO OFF
REM Remove the REM after this line clean any instances of jira_python from your machine
REM PowerShell.exe -Command "docker stop jira_python; docker rm jira_python; docker rmi jira_python"
PowerShell.exe -Command "docker build . -t jira_python"
PAUSE
