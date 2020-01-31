@echo off
echo [!] Killing Bustr executables, please wait...
taskkill /f /im bustr.exe
taskkill /f /im py.exe
taskkill /f /im python.exe
taskkill /f /im cmd.exe
echo [!] Done, press any key to close window
pause >nul