@echo off
cd ../

set /P PPYTHON_PATH=<PPYTHON_PATH

%PPYTHON_PATH% -m __main__
pause
