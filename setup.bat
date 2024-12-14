@echo off
setlocal

echo Starting setup...

:: Check if virtual environment exists
if not exist ".\env" (
    echo Virtual environment not found!
    echo Creating virtual environment...
    python -m venv env
    echo Activating virtual environment...
    call .\env\scripts\activate.bat
    echo Installing Django...
    pip install -r requirements.txt
    echo Running migrations...
    python manage.py migrate
    echo Creating superuser...
    python manage.py createsuperuser
    deactivate
    echo Setup completed successfully!
) else (
    echo Virtual environment already exists.
)

pause
endlocal