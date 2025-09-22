"""
Setup script for USDT Mining Telegram Bot
"""
import os
import sys
import subprocess
import shutil
from pathlib import Path

def create_directories():
    """Create necessary directories"""
    directories = [
        'logs',
        'uploads',
        'uploads/kyc',
        'uploads/temp',
        'backups',
        'config'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"✅ Created directory: {directory}")

def install_dependencies():
    """Install Python dependencies"""
    try:
        print("📦 Installing Python dependencies...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False
    return True

def create_env_file():
    """Create .env file from template"""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            shutil.copy('.env.example', '.env')
            print("✅ Created .env file from template")
            print("⚠️  Please edit .env file with your configuration")
        else:
            print("❌ .env.example file not found")
            return False
    else:
        print("ℹ️  .env file already exists")
    return True

def create_systemd_service():
    """Create systemd service file for Linux"""
    if sys.platform.startswith('linux'):
        service_content = f"""[Unit]
Description=USDT Mining Telegram Bot
After=network.target

[Service]
Type=simple
User=ubuntu
WorkingDirectory={os.getcwd()}
Environment=PATH={os.getcwd()}/venv/bin
ExecStart={sys.executable} main.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
"""
        
        with open('mining-bot.service', 'w') as f:
            f.write(service_content)
        
        print("✅ Created systemd service file: mining-bot.service")
        print("📝 To install service:")
        print("   sudo cp mining-bot.service /etc/systemd/system/")
        print("   sudo systemctl enable mining-bot")
        print("   sudo systemctl start mining-bot")

def create_docker_files():
    """Create Docker configuration files"""
    dockerfile_content = """FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs uploads uploads/kyc uploads/temp backups

EXPOSE 8000

CMD ["python", "main.py"]
"""
    
    docker_compose_content = """version: '3.8'

services:
  mining-bot:
    build: .
    container_name: mining-bot
    restart: unless-stopped
    volumes:
      - ./logs:/app/logs
      - ./uploads:/app/uploads
      - ./backups:/app/backups
      - ./.env:/app/.env
    environment:
      - PYTHONUNBUFFERED=1
    depends_on:
      - db

  db:
    image: postgres:13
    container_name: mining-bot-db
    restart: unless-stopped
    environment:
      POSTGRES_DB: mining_bot
      POSTGRES_USER: mining_user
      POSTGRES_PASSWORD: mining_password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

volumes:
  postgres_data:
"""
    
    with open('Dockerfile', 'w') as f:
        f.write(dockerfile_content)
    
    with open('docker-compose.yml', 'w') as f:
        f.write(docker_compose_content)
    
    print("✅ Created Docker files: Dockerfile, docker-compose.yml")

def create_pm2_config():
    """Create PM2 configuration file"""
    pm2_config = {
        "apps": [{
            "name": "mining-bot",
            "script": "main.py",
            "interpreter": "python3",
            "cwd": os.getcwd(),
            "instances": 1,
            "autorestart": True,
            "watch": False,
            "max_memory_restart": "1G",
            "env": {
                "NODE_ENV": "production"
            },
            "error_file": "./logs/pm2-error.log",
            "out_file": "./logs/pm2-out.log",
            "log_file": "./logs/pm2-combined.log",
            "time": True
        }]
    }
    
    import json
    with open('ecosystem.config.json', 'w') as f:
        json.dump(pm2_config, f, indent=2)
    
    print("✅ Created PM2 config: ecosystem.config.json")
    print("📝 To start with PM2: pm2 start ecosystem.config.json")

def create_backup_script():
    """Create backup script"""
    backup_script = """#!/bin/bash

# USDT Mining Bot Backup Script
# Run this script daily to backup important data

DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="backups"
BOT_DIR="$(pwd)"

echo "🔄 Starting backup process..."

# Create backup directory
mkdir -p "$BACKUP_DIR"

# Backup database (SQLite)
if [ -f "mining_bot.db" ]; then
    cp mining_bot.db "$BACKUP_DIR/mining_bot_$DATE.db"
    echo "✅ Database backed up"
fi

# Backup configuration
if [ -f ".env" ]; then
    cp .env "$BACKUP_DIR/env_$DATE.backup"
    echo "✅ Configuration backed up"
fi

# Backup logs (last 7 days)
if [ -d "logs" ]; then
    tar -czf "$BACKUP_DIR/logs_$DATE.tar.gz" logs/
    echo "✅ Logs backed up"
fi

# Backup uploads
if [ -d "uploads" ]; then
    tar -czf "$BACKUP_DIR/uploads_$DATE.tar.gz" uploads/
    echo "✅ Uploads backed up"
fi

# Clean old backups (keep last 30 days)
find "$BACKUP_DIR" -name "*.db" -mtime +30 -delete
find "$BACKUP_DIR" -name "*.backup" -mtime +30 -delete
find "$BACKUP_DIR" -name "*.tar.gz" -mtime +30 -delete

echo "✅ Backup completed: $BACKUP_DIR"
echo "📊 Backup size: $(du -sh $BACKUP_DIR | cut -f1)"
"""
    
    with open('backup.sh', 'w') as f:
        f.write(backup_script)
    
    os.chmod('backup.sh', 0o755)
    print("✅ Created backup script: backup.sh")

def create_start_script():
    """Create start script"""
    start_script = """#!/bin/bash

# USDT Mining Bot Start Script

echo "🚀 Starting USDT Mining Telegram Bot..."

# Check if .env exists
if [ ! -f ".env" ]; then
    echo "❌ .env file not found. Please create it from .env.example"
    exit 1
fi

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install/update dependencies
echo "📦 Installing dependencies..."
pip install -r requirements.txt

# Create necessary directories
mkdir -p logs uploads uploads/kyc uploads/temp backups

# Start the bot
echo "🤖 Starting bot..."
python main.py
"""
    
    with open('start.sh', 'w') as f:
        f.write(start_script)
    
    os.chmod('start.sh', 0o755)
    print("✅ Created start script: start.sh")

def create_windows_batch():
    """Create Windows batch files"""
    start_bat = """@echo off
echo 🚀 Starting USDT Mining Telegram Bot...

REM Check if .env exists
if not exist ".env" (
    echo ❌ .env file not found. Please create it from .env.example
    pause
    exit /b 1
)

REM Check if virtual environment exists
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\\Scripts\\activate.bat

REM Install/update dependencies
echo 📦 Installing dependencies...
pip install -r requirements.txt

REM Create necessary directories
if not exist "logs" mkdir logs
if not exist "uploads" mkdir uploads
if not exist "uploads\\kyc" mkdir uploads\\kyc
if not exist "uploads\\temp" mkdir uploads\\temp
if not exist "backups" mkdir backups

REM Start the bot
echo 🤖 Starting bot...
python main.py

pause
"""
    
    install_bat = """@echo off
echo 📦 Installing USDT Mining Telegram Bot...

REM Create virtual environment
python -m venv venv

REM Activate virtual environment
call venv\\Scripts\\activate.bat

REM Install dependencies
pip install -r requirements.txt

REM Create directories
if not exist "logs" mkdir logs
if not exist "uploads" mkdir uploads
if not exist "uploads\\kyc" mkdir uploads\\kyc
if not exist "uploads\\temp" mkdir uploads\\temp
if not exist "backups" mkdir backups

REM Create .env file
if not exist ".env" (
    copy .env.example .env
    echo ✅ Created .env file from template
    echo ⚠️  Please edit .env file with your configuration
)

echo ✅ Installation completed!
echo 📝 Next steps:
echo    1. Edit .env file with your bot token and configuration
echo    2. Run start.bat to start the bot

pause
"""
    
    with open('start.bat', 'w') as f:
        f.write(start_bat)
    
    with open('install.bat', 'w') as f:
        f.write(install_bat)
    
    print("✅ Created Windows batch files: start.bat, install.bat")

def main():
    """Main setup function"""
    print("🔧 USDT Mining Telegram Bot Setup")
    print("=" * 40)
    
    # Create directories
    create_directories()
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Setup failed during dependency installation")
        return
    
    # Create .env file
    if not create_env_file():
        print("❌ Setup failed during .env creation")
        return
    
    # Create deployment files
    create_systemd_service()
    create_docker_files()
    create_pm2_config()
    create_backup_script()
    create_start_script()
    create_windows_batch()
    
    print("\n" + "=" * 40)
    print("✅ Setup completed successfully!")
    print("\n📝 Next steps:")
    print("1. Edit .env file with your bot token and configuration")
    print("2. Configure wallet addresses in .env")
    print("3. Set admin user IDs in .env")
    print("4. Run the bot:")
    
    if sys.platform.startswith('win'):
        print("   Windows: start.bat")
    else:
        print("   Linux/Mac: ./start.sh")
        print("   Or: python main.py")
    
    print("\n🔧 Deployment options:")
    print("• Systemd: Use mining-bot.service")
    print("• Docker: docker-compose up -d")
    print("• PM2: pm2 start ecosystem.config.json")
    
    print("\n📚 Documentation:")
    print("• README.md - Complete documentation")
    print("• .env.example - Configuration reference")
    
    print("\n🛡️  Security reminders:")
    print("• Keep your .env file secure")
    print("• Use strong passwords")
    print("• Enable firewall if needed")
    print("• Regular backups with backup.sh")

if __name__ == '__main__':
    main()
