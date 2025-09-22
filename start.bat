@echo off
echo.
echo ========================================
echo   Starting USDT Mining Telegram Bot
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo Please run install.bat first
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist ".env" (
    echo ❌ .env file not found
    echo.
    echo Please create .env file with your bot configuration:
    echo    1. Copy .env.example to .env
    echo    2. Edit .env with your bot token and settings
    echo    3. Get bot token from @BotFather on Telegram
    echo.
    pause
    exit /b 1
)

REM Activate virtual environment if it exists
if exist "venv\Scripts\activate.bat" (
    echo 🔄 Activating virtual environment...
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment activated
)

REM Check if dependencies are installed
python -c "import telegram" >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Dependencies not installed
    echo Please run install.bat first
    pause
    exit /b 1
)

REM Create directories if they don't exist
if not exist "logs" mkdir logs
if not exist "uploads" mkdir uploads
if not exist "backups" mkdir backups

echo ✅ Pre-flight checks passed
echo.
echo 🚀 Starting bot...
echo.
echo ⚠️  Press Ctrl+C to stop the bot
echo.

REM Start the bot
python main.py

echo.
echo 🛑 Bot stopped
pause
