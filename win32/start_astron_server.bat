@echo off
cd ../

cd astron
astrond --loglevel info config/astrond.yml
pause