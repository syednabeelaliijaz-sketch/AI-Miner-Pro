#!/usr/bin/env python3
"""
Replit-specific main script for USDT Mining Telegram Bot
This handles Replit's environment properly
"""
import sys
import os
import subprocess

def install_dependencies():
    """Install dependencies on Replit"""
    print("📦 Installing dependencies...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def setup_environment():
    """Setup environment for Replit"""
    print("🔧 Setting up environment...")
    
    # Create necessary directories
    directories = ['logs', 'uploads', 'uploads/kyc', 'uploads/temp', 'backups']
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    
    # Check if .env exists, if not create from example
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            print("⚠️  .env file not found. Please set up your environment variables in Replit Secrets!")
            print("Required secrets:")
            print("- BOT_TOKEN")
            print("- BOT_USERNAME") 
            print("- ADMIN_USER_IDS")
            print("- SUPER_ADMIN_ID")
        else:
            print("❌ .env.example not found")
            return False
    
    return True

def main():
    """Main function for Replit"""
    print("🚀 Starting USDT Mining Telegram Bot on Replit...")
    
    # Setup environment
    if not setup_environment():
        print("❌ Environment setup failed")
        return
    
    # Install dependencies
    if not install_dependencies():
        print("❌ Dependency installation failed")
        return
    
    # Import and run the main bot
    try:
        print("🤖 Starting bot...")
        from main import main as bot_main
        bot_main()
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Make sure all files are uploaded correctly")
    except Exception as e:
        print(f"❌ Error starting bot: {e}")

if __name__ == '__main__':
    main()
