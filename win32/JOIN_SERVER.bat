@echo off
cd ../
set /P user="Username: " || ^
set /P pass="Password: " || ^
set user=username
set pass=password
set TTR_PLAYCOOKIE=%ttrUsername%
set TTR_GAMESERVER=127.0.0.1

set /P PPYTHON_PATH=<PPYTHON_PATH



echo ===============================
echo Starting Toontown...
echo ppython: %PPYTHON_PATH%
echo Username: %user%:%pass%
echo Client Agent IP: %TTR_GAMESERVER%
echo ===============================

%PPYTHON_PATH% -m toontown.toonbase.ToontownStart
pause
