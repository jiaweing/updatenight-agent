@echo off

clear

echo Cleaning up logs and content directories...

:: Remove logs directory
if exist logs\ (
    echo Removing logs directory...
    rmdir /s /q logs
)

:: Remove content directory
if exist content\ (
    echo Removing content directory...
    rmdir /s /q content
)

:: Remove links.md
if exist links.md (
    echo Removing links.md...
    del links.md
)

echo.
echo Cleanup complete!
echo - Removed logs directory
echo - Removed content directory
echo. 