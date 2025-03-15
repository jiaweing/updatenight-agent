@echo off
echo Cleaning up logs and output directories...

:: Remove logs directory
if exist logs\ (
    echo Removing logs directory...
    rmdir /s /q logs
)

:: Remove output directory
if exist output\ (
    echo Removing output directory...
    rmdir /s /q output
)

:: Remove links.md
if exist links.md (
    echo Removing links.md...
    del links.md
)

echo.
echo Cleanup complete!
echo - Removed logs directory
echo - Removed output directory
echo. 