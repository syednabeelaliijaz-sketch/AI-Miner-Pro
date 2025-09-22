# 🚀 Quick Start Guide - USDT Mining Telegram Bot

## ⚠️ Prerequisites Setup

### 1. Install Python (Required)

**Method 1: Microsoft Store (Easiest)**
1. Open Microsoft Store
2. Search for "Python 3.11"
3. Click "Get" or "Install"
4. Wait for installation to complete

**Method 2: Python.org (Alternative)**
1. Go to https://www.python.org/downloads/
2. Download Python 3.11.x for Windows
3. Run the installer
4. ✅ **IMPORTANT**: Check "Add Python to PATH" during installation
5. Click "Install Now"

### 2. Verify Python Installation

Open Command Prompt or PowerShell and run:
```cmd
python --version
```
You should see: `Python 3.11.x`

If you see an error, restart your computer and try again.

## 🤖 Bot Setup

### 3. Get Telegram Bot Token

1. Open Telegram and search for `@BotFather`
2. Start a chat and send `/newbot`
3. Follow the instructions:
   - Choose a name for your bot (e.g., "USDT Mining Bot")
   - Choose a username (e.g., "usdt_mining_bot")
4. Copy the bot token (looks like: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 4. Get Your Telegram User ID

1. Search for `@userinfobot` on Telegram
2. Start the bot and send any message
3. Copy your User ID (numbers like: `123456789`)

### 5. Configure the Bot

1. Open the `.env.example` file in the telegram_bot folder
2. Copy it and rename to `.env`
3. Edit the `.env` file with your information:

```env
# REQUIRED - Replace with your actual values
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
BOT_USERNAME=your_bot_username
ADMIN_USER_IDS=123456789
SUPER_ADMIN_ID=123456789

# OPTIONAL - Add your wallet addresses
USDT_WALLET_ADDRESS=TQn9Y2khEsLMWD5uPKiGvhHjBDwQXqvQBq
BTC_WALLET_ADDRESS=1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
ETH_WALLET_ADDRESS=0x742d35Cc6634C0532925a3b8D4C9db96590C6b65

# OPTIONAL - Customize settings
APP_NAME=USDT Mining Bot
SUPPORT_USERNAME=your_support_username
CHANNEL_USERNAME=your_channel_username
```

## 🔧 Installation Commands

### 6. Install Dependencies

Open Command Prompt or PowerShell in the telegram_bot folder and run:

```cmd
pip install -r requirements.txt
```

### 7. Run Setup Script

```cmd
python setup.py
```

### 8. Start the Bot

```cmd
python main.py
```

## ✅ Success Indicators

When the bot starts successfully, you should see:
```
INFO - Starting USDT Mining Bot...
INFO - Bot username: @your_bot_username
INFO - Database initialized successfully
INFO - Profit scheduler started successfully
INFO - Bot post-initialization completed
```

## 🧪 Test the Bot

1. Open Telegram
2. Search for your bot username (e.g., @your_bot_username)
3. Send `/start`
4. You should see the welcome message with buttons

## 🛠 Troubleshooting

### Python Not Found
- Restart your computer after installing Python
- Make sure "Add Python to PATH" was checked during installation
- Try `py` instead of `python`

### Module Not Found Errors
```cmd
pip install --upgrade pip
pip install -r requirements.txt
```

### Bot Token Invalid
- Double-check your bot token in `.env`
- Make sure there are no extra spaces
- Get a new token from @BotFather if needed

### Permission Errors
- Run Command Prompt as Administrator
- Check file permissions in the project folder

## 📱 Using the Bot

### User Features:
- 📊 **Dashboard** - View balance and mining status
- ⛏️ **Mining** - Start mining with 6 different levels
- 💰 **Wallet** - Deposit, withdraw, view transactions
- 👥 **Referrals** - Earn 5% bonus from referrals
- 👤 **Profile** - Manage account and KYC

### Admin Features (for admin users):
- 🔧 **Admin Panel** - Access with `/admin`
- 👥 **User Management** - View and manage users
- 💳 **Transactions** - Approve deposits and withdrawals
- 📢 **Broadcasting** - Send announcements
- ⛏️ **Mining Management** - Control mining operations

## 🎯 Next Steps

1. **Test all features** with your admin account
2. **Add wallet addresses** for real payments
3. **Invite users** to test the bot
4. **Monitor logs** in the `logs/` folder
5. **Set up automated backups** using `backup.sh`

## 🆘 Need Help?

- Check the `logs/bot.log` file for error details
- Review the `README.md` for complete documentation
- Check the `DEPLOYMENT_GUIDE.md` for advanced setup

---

**🎉 Congratulations! Your USDT Mining Telegram Bot is ready to serve users!**
