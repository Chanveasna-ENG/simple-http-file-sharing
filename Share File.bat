@echo off
setlocal

echo Starting batch file execution...

:: Check if virtual environment exists
if not exist ".\env" (
    echo Virtual environment not found! Running setup...
    call setup.bat
)

:: Activate the virtual environment
echo Activating virtual environment...
call .\env\scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b %errorlevel%
)

:: Run the Django development server
echo Starting Django server...
python manage.py runserver 0.0.0.0:10000
if %errorlevel% neq 0 (
    echo Failed to start Django development server.
    pause
    exit /b %errorlevel%
)

pause
endlocal