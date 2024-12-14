@echo off
setlocal

echo Starting batch file execution...

:: Check if virtual environment exists
if not exist ".\env" (
    echo Virtual environment not found!
    echo Creating virtual environment...
    python -m venv env
    echo Activating virtual environment...
    .\env\scripts\activate.bat
    echo Installing requirements...
    pip install -r requirements.txt
    echo Django installed successfully!
    deactivate
    pause
    exit /b 0
)
:: Activate the virtual environment
echo Activating virtual environment...
call .\env\scripts\activate.bat
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    pause
    exit /b %errorlevel%
)

:: Change directory to file_sharing
echo Changing directory...
cd file_sharing
if %errorlevel% neq 0 (
    echo Failed to change directory to file_sharing.
    echo Current directory: %CD%
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