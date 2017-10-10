@echo off
rem Input your own username and password in place of "user" and "pass"
set SESSION=scp://root:pass@10.13.0.0/
set REMOTE_PATH=/import/
 
echo open %SESSION% >> script.tmp
 
rem Generate "put" command for each line in list file
echo put C:\Docker\jira\tables "%REMOTE_PATH%" >> script.tmp
 
echo exit >> script.tmp
 
"C:\Program Files (x86)\WinSCP\winscp.com" /script=script.tmp
set RESULT=%ERRORLEVEL%
 
del script.tmp
 
pause
rem Propagating WinSCP exit code
call exit /b %RESULT%