@echo off
echo.
echo ========================================
echo   USDT Mining Telegram Bot Setup
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed or not in PATH
    echo.
    echo 📥 Please install Python first:
    echo    1. Go to https://www.python.org/downloads/
    echo    2. Download Python 3.11 for Windows
    echo    3. Run installer and CHECK "Add Python to PATH"
    echo    4. Restart your computer
    echo    5. Run this script again
    echo.
    pause
    exit /b 1
)

echo ✅ Python found
python --version

REM Check if pip is available
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip is not available
    echo Please reinstall Python with pip included
    pause
    exit /b 1
)

echo ✅ pip found

REM Create virtual environment (optional but recommended)
echo.
echo 📦 Creating virtual environment...
python -m venv venv
if %errorlevel% neq 0 (
    echo ⚠️  Could not create virtual environment, continuing without it...
) else (
    echo ✅ Virtual environment created
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment activated
)

REM Install dependencies
echo.
echo 📦 Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Failed to install dependencies
    pause
    exit /b 1
)

echo ✅ Dependencies installed successfully

REM Create necessary directories
echo.
echo 📁 Creating directories...
if not exist "logs" mkdir logs
if not exist "uploads" mkdir uploads
if not exist "uploads\kyc" mkdir "uploads\kyc"
if not exist "uploads\temp" mkdir "uploads\temp"
if not exist "backups" mkdir backups

echo ✅ Directories created

REM Create .env file from template
echo.
echo ⚙️  Setting up configuration...
if not exist ".env" (
    if exist ".env.example" (
        copy ".env.example" ".env" >nul
        echo ✅ Created .env file from template
        echo.
        echo ⚠️  IMPORTANT: You must edit .env file with your bot token!
        echo    1. Get bot token from @BotFather on Telegram
        echo    2. Get your user ID from @userinfobot on Telegram
        echo    3. Edit .env file with your information
        echo.
    ) else (
        echo ❌ .env.example file not found
    )
) else (
    echo ℹ️  .env file already exists
)

REM Run setup script
echo.
echo 🔧 Running setup script...
python setup.py
if %errorlevel% neq 0 (
    echo ❌ Setup script failed
    pause
    exit /b 1
)

echo.
echo ========================================
echo ✅ Installation completed successfully!
echo ========================================
echo.
echo 📝 Next steps:
echo    1. Edit .env file with your bot token and settings
echo    2. Run start.bat to start the bot
echo.
echo 🤖 Bot token setup:
echo    1. Open Telegram and search for @BotFather
echo    2. Send /newbot and follow instructions
echo    3. Copy the token to .env file
echo.
echo 👤 Admin setup:
echo    1. Search for @userinfobot on Telegram
echo    2. Get your user ID
echo    3. Add it to ADMIN_USER_IDS in .env file
echo.
echo 📚 Documentation:
echo    - README.md - Complete documentation
echo    - QUICK_START.md - Quick start guide
echo    - DEPLOYMENT_GUIDE.md - Deployment options
echo.
pause
