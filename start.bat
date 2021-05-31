@echo off
:loop
echo Starting launcher.py... - If you run into any issues create a issue!
python launcher.py
timeout /t 5 > nul
cls
echo Restarting..
goto loop