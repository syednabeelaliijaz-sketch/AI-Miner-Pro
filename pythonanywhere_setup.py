"""
PythonAnywhere setup script
Run this after uploading files to PythonAnywhere
"""
import os
import subprocess
import sys

def setup_pythonanywhere():
    """Setup bot for PythonAnywhere"""
    print("🔧 Setting up USDT Mining Bot for PythonAnywhere...")
    
    # Install dependencies
    print("📦 Installing dependencies...")
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--user', '-r', 'requirements.txt'])
    
    # Create directories
    os.makedirs('logs', exist_ok=True)
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('backups', exist_ok=True)
    
    # Initialize database
    print("🗄️ Initializing database...")
    from database.init_data import initialize_database
    initialize_database()
    
    print("✅ Setup completed!")
    print("📝 Next steps:")
    print("1. Create .env file with your bot token")
    print("2. Go to PythonAnywhere Tasks tab")
    print("3. Create new task: python3.11 /home/yourusername/telegram_bot/main.py")
    print("4. Set it to run always")

if __name__ == '__main__':
    setup_pythonanywhere()
