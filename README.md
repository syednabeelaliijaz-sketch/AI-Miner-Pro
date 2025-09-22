# USDT Mining Telegram Bot

A comprehensive Telegram bot that replicates all features of the PHP USDT Mining Platform, providing users with a complete mining experience directly through Telegram.

## 🚀 Features

### User Features
- **User Registration & Authentication** - Seamless registration with referral system
- **Dashboard** - Real-time wallet balance, mining status, and statistics
- **Mining System** - 6 mining levels (Starter to Diamond) with different profit rates
- **Wallet Management** - Deposits, withdrawals, and transaction history
- **Referral Program** - Earn 5% bonus for successful referrals
- **KYC Verification** - Document upload and verification system
- **Real-time Notifications** - Instant updates on transactions and mining

### Admin Features
- **Admin Dashboard** - Comprehensive system statistics and analytics
- **User Management** - View, search, and manage user accounts
- **Transaction Management** - Approve/reject deposits and withdrawals
- **Mining Management** - Monitor and control mining operations
- **Broadcasting** - Send announcements to all users
- **System Monitoring** - Real-time system health and performance

### Automation Features
- **Daily Profit Calculation** - Automated profit distribution at 12:01 AM daily
- **Investment Returns** - Automatic return of original investment after mining period
- **Email Notifications** - Automated notifications for important events
- **System Maintenance** - Weekly cleanup and optimization tasks

## 🛠 Technology Stack

- **Python 3.8+** - Core programming language
- **python-telegram-bot 20.7** - Telegram Bot API wrapper
- **SQLAlchemy 2.0** - Database ORM
- **APScheduler 3.10** - Task scheduling
- **SQLite/PostgreSQL** - Database options
- **Pillow** - Image processing for KYC documents
- **bcrypt** - Password hashing and security

## 📁 Project Structure

```
telegram_bot/
├── config/
│   └── settings.py          # Configuration settings
├── database/
│   ├── models.py           # Database models
│   ├── database.py         # Database connection
│   └── init_data.py        # Initial data setup
├── handlers/
│   ├── user_handlers.py    # User command handlers
│   └── admin_handlers.py   # Admin command handlers
├── services/
│   ├── user_service.py     # User operations
│   ├── mining_service.py   # Mining operations
│   └── transaction_service.py # Transaction operations
├── utils/
│   ├── keyboards.py        # Inline keyboards
│   ├── formatters.py       # Message formatting
│   └── security.py         # Security utilities
├── automation/
│   └── profit_scheduler.py # Automated tasks
├── logs/                   # Log files
├── uploads/               # User uploads
├── main.py               # Main bot application
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🔧 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Telegram Bot Token (from @BotFather)

### Quick Setup

1. **Clone or download the project**
   ```bash
   cd telegram_bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure the bot**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file with your configuration:
   ```env
   BOT_TOKEN=your_bot_token_here
   BOT_USERNAME=your_bot_username
   ADMIN_USER_IDS=123456789,987654321
   SUPER_ADMIN_ID=123456789
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `BOT_TOKEN` | Telegram bot token from @BotFather | Yes |
| `BOT_USERNAME` | Bot username (without @) | Yes |
| `ADMIN_USER_IDS` | Comma-separated admin user IDs | Yes |
| `SUPER_ADMIN_ID` | Super admin user ID | Yes |
| `DATABASE_URL` | Database connection URL | No |
| `USDT_WALLET_ADDRESS` | USDT wallet for deposits | No |
| `BTC_WALLET_ADDRESS` | Bitcoin wallet for deposits | No |
| `ETH_WALLET_ADDRESS` | Ethereum wallet for deposits | No |

### Mining Levels Configuration

The bot comes with 6 pre-configured mining levels:

| Level | Min Deposit | Max Deposit | Daily Profit | Duration |
|-------|-------------|-------------|--------------|----------|
| 🥉 Starter | $10 | $99.99 | 1.5% | 30 days |
| 🥉 Bronze | $100 | $499.99 | 2.0% | 60 days |
| 🥈 Silver | $500 | $999.99 | 2.5% | 90 days |
| 🥇 Gold | $1,000 | $4,999.99 | 3.0% | 120 days |
| 💎 Platinum | $5,000 | $9,999.99 | 3.5% | 180 days |
| 💎 Diamond | $10,000+ | Unlimited | 4.0% | 365 days |

## 🤖 Bot Commands

### User Commands
- `/start` - Start the bot and show main menu
- `/cancel` - Cancel current operation

### Admin Commands
- `/admin` - Access admin panel (admin only)

### Inline Keyboards
All interactions are done through inline keyboards for better user experience:
- 📊 Dashboard
- ⛏️ Mining
- 💰 Wallet
- 👥 Referrals
- 👤 Profile
- 📋 Transactions
- ⚙️ Settings

## 🔒 Security Features

- **Rate Limiting** - Prevents spam and abuse
- **Input Validation** - All user inputs are validated and sanitized
- **Admin Authentication** - Multi-level admin access control
- **Transaction Security** - Secure transaction processing with rollback
- **File Upload Security** - Safe file handling for KYC documents
- **SQL Injection Prevention** - Using SQLAlchemy ORM with prepared statements

## 📊 Database Schema

The bot uses a comprehensive database schema with 15+ tables:

### Core Tables
- `users` - User accounts and authentication
- `user_wallets` - Wallet balances and transactions
- `mining_levels` - Mining plan configurations
- `user_mining` - Active mining accounts
- `mining_profits` - Daily profit records
- `transactions` - All financial transactions
- `withdrawal_requests` - Withdrawal request management
- `kyc_documents` - KYC verification files
- `referrals` - Referral tracking and rewards

## 🔄 Automation

### Daily Profit Calculation
- Runs automatically at 12:01 AM daily
- Calculates profits based on mining level and investment amount
- Updates user wallets and creates transaction records
- Handles mining completion and investment returns
- Sends admin notifications with results

### System Maintenance
- Weekly cleanup tasks
- Database optimization
- Log file management
- System health monitoring

## 📱 User Experience

### Registration Flow
1. User starts the bot with `/start`
2. Optional referral code detection from deep links
3. One-click registration with Telegram profile data
4. Automatic wallet creation
5. Welcome message with next steps

### Mining Flow
1. Browse available mining plans
2. Select mining level based on balance
3. Enter investment amount
4. Confirm activation
5. Start earning daily profits automatically

### Deposit Flow
1. Select payment method (USDT, BTC, ETH)
2. Enter deposit amount
3. Get wallet address and instructions
4. Send payment and submit transaction hash
5. Admin approval and wallet credit

### Withdrawal Flow
1. Enter withdrawal amount and wallet address
2. Submit withdrawal request
3. Admin review and approval
4. Manual payment processing
5. Transaction completion with hash

## 🔧 Admin Panel

### Dashboard
- Real-time system statistics
- User counts and activity
- Financial overview
- Mining statistics
- Pending operations

### User Management
- View all users
- Search specific users
- Verify KYC documents
- Manage user accounts
- View user details

### Transaction Management
- Review pending deposits
- Approve/reject transactions
- Manage withdrawal requests
- View transaction history
- Generate reports

### Broadcasting
- Send announcements to all users
- Target specific user groups
- Track delivery statistics
- Schedule messages (future feature)

## 🚀 Deployment

### Local Development
```bash
python main.py
```

### Production Deployment

1. **Using systemd (Linux)**
   ```bash
   sudo cp mining-bot.service /etc/systemd/system/
   sudo systemctl enable mining-bot
   sudo systemctl start mining-bot
   ```

2. **Using Docker**
   ```bash
   docker build -t mining-bot .
   docker run -d --name mining-bot mining-bot
   ```

3. **Using PM2**
   ```bash
   pm2 start main.py --name mining-bot --interpreter python3
   ```

## 📝 Logging

The bot includes comprehensive logging:
- All user interactions
- Transaction processing
- Error handling
- Admin actions
- System events
- Profit calculations

Logs are stored in `logs/bot.log` and rotated automatically.

## 🔍 Monitoring

### Health Checks
- Database connectivity
- Scheduler status
- Bot responsiveness
- Memory usage
- Error rates

### Alerts
- Failed profit calculations
- Database errors
- High error rates
- System downtime

## 🛡️ Error Handling

- Graceful error recovery
- User-friendly error messages
- Admin error notifications
- Automatic retry mechanisms
- Fallback procedures

## 📈 Performance

### Optimization Features
- Database connection pooling
- Query optimization with indexes
- Async/await for non-blocking operations
- Rate limiting to prevent abuse
- Efficient message formatting

### Scalability
- Supports thousands of concurrent users
- Horizontal scaling ready
- Database optimization
- Memory efficient operations

## 🔄 Updates and Maintenance

### Regular Updates
- Security patches
- Feature enhancements
- Bug fixes
- Performance improvements

### Backup Strategy
- Daily database backups
- Configuration backups
- Log file archiving
- Disaster recovery plan

## 📞 Support

### User Support
- In-bot support commands
- FAQ and help sections
- Contact information
- Troubleshooting guides

### Admin Support
- Comprehensive admin documentation
- Error handling guides
- Maintenance procedures
- Update instructions

## 🔮 Future Features

- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Mobile app integration
- [ ] API for third-party integrations
- [ ] Advanced referral system
- [ ] Staking features
- [ ] NFT integration
- [ ] DeFi features

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## ⚠️ Disclaimer

This bot is for educational and demonstration purposes. Always comply with local regulations regarding cryptocurrency and financial services.

---

**Built with ❤️ using Python and the python-telegram-bot library.**
