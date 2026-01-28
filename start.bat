@echo off
REM Telegram Mention Bot Startup Script (Windows)

echo Starting Telegram Mention Bot...

REM Check if .env exists
if not exist ".env" (
    echo .env file not found!
    echo Please copy sample.env to .env and configure it
    pause
    exit /b 1
)

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    pause
    exit /b 1
)

REM Check if dependencies are installed
echo Checking dependencies...
python -c "import pyrogram, aiosqlite" >nul 2>&1
if errorlevel 1 (
    echo Missing dependencies. Installing...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo Failed to install dependencies. Please install manually:
        echo pip install -r requirements.txt
        pause
        exit /b 1
    )
    echo Dependencies installed successfully
) else (
    echo Dependencies are installed
)

REM Start the bot with auto-restart wrapper
echo Starting with auto-restart wrapper...
python bot_runner.py
pause
