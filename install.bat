@echo off
setlocal enabledelayedexpansion

set SCRIPT_PATH=%~dp0
set SCRIPT_PATH=%SCRIPT_PATH:~0,-1%
set SCRIPT_NAME=y2mp3.bat
set INSTALL_PATH=%SCRIPT_PATH%
set TARGET_PATH=%SystemRoot%\System32

net session >nul 2>&1
if %errorLevel% neq 0 (
    echo Please run this script as Administrator.
    pause
    exit /b
)

echo @echo off > "%INSTALL_PATH%\%SCRIPT_NAME%"
echo python "%INSTALL_PATH%\main.py" %%* >> "%INSTALL_PATH%\%SCRIPT_NAME%"

copy /Y "%INSTALL_PATH%\%SCRIPT_NAME%" "%TARGET_PATH%\" >nul

if exist "%TARGET_PATH%\%SCRIPT_NAME%" (
    echo Installation successful!
    echo You can now run 'y2mp3' from any command prompt.
) else (
    echo Installation failed. Try running this script as administrator.
)

pause
