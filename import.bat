@echo off
set SESSION=scp://root:goldenhalo1@10.13.1.171/
set REMOTE_PATH=/import/
 
echo open %SESSION% >> script.tmp
 
rem Generate "put" command for each line in list file
for /F %%i in (list.txt) do echo put "%%i" "%REMOTE_PATH%" >> script.tmp
 
echo exit >> script.tmp
 
"C:\Program Files (x86)\WinSCP\winscp.com" /script=script.tmp
set RESULT=%ERRORLEVEL%
 
del script.tmp
 
rem Propagating WinSCP exit code
call exit /b %RESULT%
pause