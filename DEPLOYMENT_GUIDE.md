# USDT Mining Telegram Bot - Deployment Guide

This guide covers various deployment methods for the USDT Mining Telegram Bot.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Telegram Bot Token (from @BotFather)
- Admin Telegram User IDs

### 1. Basic Setup

```bash
# Clone/download the project
cd telegram_bot

# Run setup script
python setup.py

# Edit configuration
nano .env  # Linux/Mac
notepad .env  # Windows

# Start the bot
python main.py
```

## 🔧 Configuration

### Environment Variables (.env file)

```env
# Bot Configuration
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
BOT_USERNAME=your_mining_bot
ADMIN_USER_IDS=123456789,987654321
SUPER_ADMIN_ID=123456789

# Database
DATABASE_URL=sqlite:///mining_bot.db
# For PostgreSQL: postgresql://user:pass@localhost/mining_bot

# Wallet Addresses
USDT_WALLET_ADDRESS=TQn9Y2khEsLMWD5uPKiGvhHjBDwQXqvQBq
BTC_WALLET_ADDRESS=1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
ETH_WALLET_ADDRESS=0x742d35Cc6634C0532925a3b8D4C9db96590C6b65

# Application Settings
APP_NAME=USDT Mining Bot
SUPPORT_USERNAME=your_support_username
CHANNEL_USERNAME=your_channel_username

# Security
SECRET_KEY=your-very-secure-secret-key-here
MIN_DEPOSIT=10.00
MAX_DEPOSIT=100000.00
REFERRAL_BONUS_PERCENTAGE=5.0
```

## 🐧 Linux Deployment

### Method 1: Systemd Service (Recommended)

1. **Install and setup**
   ```bash
   python setup.py
   sudo cp mining-bot.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable mining-bot
   sudo systemctl start mining-bot
   ```

2. **Check status**
   ```bash
   sudo systemctl status mining-bot
   sudo journalctl -u mining-bot -f  # View logs
   ```

3. **Manage service**
   ```bash
   sudo systemctl stop mining-bot     # Stop
   sudo systemctl restart mining-bot  # Restart
   sudo systemctl disable mining-bot  # Disable auto-start
   ```

### Method 2: PM2 Process Manager

1. **Install PM2**
   ```bash
   npm install -g pm2
   ```

2. **Start bot**
   ```bash
   pm2 start ecosystem.config.json
   pm2 save
   pm2 startup  # Enable auto-start
   ```

3. **Manage with PM2**
   ```bash
   pm2 status           # Check status
   pm2 logs mining-bot  # View logs
   pm2 restart mining-bot  # Restart
   pm2 stop mining-bot     # Stop
   ```

### Method 3: Screen/Tmux Session

1. **Using Screen**
   ```bash
   screen -S mining-bot
   python main.py
   # Ctrl+A, D to detach
   screen -r mining-bot  # Reattach
   ```

2. **Using Tmux**
   ```bash
   tmux new-session -d -s mining-bot 'python main.py'
   tmux attach-session -t mining-bot
   ```

## 🐳 Docker Deployment

### Method 1: Docker Compose (Recommended)

1. **Start services**
   ```bash
   docker-compose up -d
   ```

2. **View logs**
   ```bash
   docker-compose logs -f mining-bot
   ```

3. **Manage services**
   ```bash
   docker-compose stop     # Stop all services
   docker-compose restart  # Restart all services
   docker-compose down     # Stop and remove containers
   ```

### Method 2: Docker Only

1. **Build image**
   ```bash
   docker build -t mining-bot .
   ```

2. **Run container**
   ```bash
   docker run -d \
     --name mining-bot \
     --restart unless-stopped \
     -v $(pwd)/logs:/app/logs \
     -v $(pwd)/uploads:/app/uploads \
     -v $(pwd)/.env:/app/.env \
     mining-bot
   ```

3. **Manage container**
   ```bash
   docker logs -f mining-bot    # View logs
   docker restart mining-bot    # Restart
   docker stop mining-bot       # Stop
   ```

## 🪟 Windows Deployment

### Method 1: Windows Service

1. **Install NSSM (Non-Sucking Service Manager)**
   - Download from https://nssm.cc/download
   - Extract to C:\nssm

2. **Create service**
   ```cmd
   C:\nssm\nssm.exe install MiningBot
   ```
   - Application: C:\Python39\python.exe
   - Arguments: C:\path\to\telegram_bot\main.py
   - Startup directory: C:\path\to\telegram_bot

3. **Start service**
   ```cmd
   net start MiningBot
   ```

### Method 2: Task Scheduler

1. **Open Task Scheduler**
2. **Create Basic Task**
   - Name: USDT Mining Bot
   - Trigger: At startup
   - Action: Start a program
   - Program: python.exe
   - Arguments: main.py
   - Start in: C:\path\to\telegram_bot

### Method 3: Batch File

1. **Use provided batch files**
   ```cmd
   install.bat  # First time setup
   start.bat    # Start the bot
   ```

2. **Create shortcut for easy access**

## ☁️ Cloud Deployment

### Heroku

1. **Create Procfile**
   ```
   worker: python main.py
   ```

2. **Deploy**
   ```bash
   heroku create your-mining-bot
   heroku config:set BOT_TOKEN=your_token
   heroku config:set DATABASE_URL=postgresql://...
   git push heroku main
   heroku ps:scale worker=1
   ```

### DigitalOcean Droplet

1. **Create droplet** (Ubuntu 20.04)
2. **Setup environment**
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip git
   git clone your-repo
   cd telegram_bot
   python3 setup.py
   ```

3. **Use systemd service** (see Linux deployment)

### AWS EC2

1. **Launch EC2 instance** (Amazon Linux 2)
2. **Install dependencies**
   ```bash
   sudo yum update
   sudo yum install python3 python3-pip git
   ```

3. **Deploy using systemd** or **PM2**

### Google Cloud Platform

1. **Create Compute Engine instance**
2. **Use startup script**
   ```bash
   #!/bin/bash
   cd /opt
   git clone your-repo telegram_bot
   cd telegram_bot
   python3 setup.py
   systemctl start mining-bot
   ```

## 🗄️ Database Options

### SQLite (Default)
- File-based database
- No additional setup required
- Good for small to medium deployments

### PostgreSQL (Recommended for production)

1. **Install PostgreSQL**
   ```bash
   # Ubuntu/Debian
   sudo apt install postgresql postgresql-contrib
   
   # CentOS/RHEL
   sudo yum install postgresql-server postgresql-contrib
   ```

2. **Create database**
   ```sql
   sudo -u postgres psql
   CREATE DATABASE mining_bot;
   CREATE USER mining_user WITH PASSWORD 'secure_password';
   GRANT ALL PRIVILEGES ON DATABASE mining_bot TO mining_user;
   ```

3. **Update .env**
   ```env
   DATABASE_URL=postgresql://mining_user:secure_password@localhost/mining_bot
   ```

### MySQL

1. **Install MySQL**
   ```bash
   sudo apt install mysql-server
   ```

2. **Create database**
   ```sql
   mysql -u root -p
   CREATE DATABASE mining_bot;
   CREATE USER 'mining_user'@'localhost' IDENTIFIED BY 'secure_password';
   GRANT ALL PRIVILEGES ON mining_bot.* TO 'mining_user'@'localhost';
   ```

3. **Update .env**
   ```env
   DATABASE_URL=mysql://mining_user:secure_password@localhost/mining_bot
   ```

## 🔒 Security Considerations

### Firewall Configuration

```bash
# Ubuntu/Debian
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443

# CentOS/RHEL
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

### SSL/TLS Setup (if using webhooks)

```bash
# Install Certbot
sudo apt install certbot

# Get certificate
sudo certbot certonly --standalone -d yourdomain.com

# Auto-renewal
sudo crontab -e
0 12 * * * /usr/bin/certbot renew --quiet
```

### File Permissions

```bash
chmod 600 .env              # Secure config file
chmod 755 *.sh              # Executable scripts
chmod -R 755 logs/          # Log directory
chmod -R 755 uploads/       # Upload directory
```

## 📊 Monitoring and Logging

### Log Management

1. **Logrotate configuration**
   ```bash
   sudo nano /etc/logrotate.d/mining-bot
   ```
   
   ```
   /path/to/telegram_bot/logs/*.log {
       daily
       missingok
       rotate 30
       compress
       delaycompress
       notifempty
       copytruncate
   }
   ```

### System Monitoring

1. **Install monitoring tools**
   ```bash
   sudo apt install htop iotop nethogs
   ```

2. **Monitor bot process**
   ```bash
   htop -p $(pgrep -f main.py)
   ```

### Health Checks

1. **Create health check script**
   ```bash
   #!/bin/bash
   if pgrep -f "main.py" > /dev/null; then
       echo "Bot is running"
       exit 0
   else
       echo "Bot is not running"
       exit 1
   fi
   ```

2. **Add to crontab**
   ```bash
   */5 * * * * /path/to/health_check.sh
   ```

## 🔄 Backup and Recovery

### Automated Backups

1. **Use provided backup script**
   ```bash
   chmod +x backup.sh
   ./backup.sh
   ```

2. **Schedule daily backups**
   ```bash
   crontab -e
   0 2 * * * /path/to/telegram_bot/backup.sh
   ```

### Database Backups

1. **SQLite**
   ```bash
   cp mining_bot.db backups/mining_bot_$(date +%Y%m%d).db
   ```

2. **PostgreSQL**
   ```bash
   pg_dump mining_bot > backups/mining_bot_$(date +%Y%m%d).sql
   ```

### Recovery Process

1. **Stop the bot**
2. **Restore database**
3. **Restore configuration**
4. **Start the bot**
5. **Verify functionality**

## 🚨 Troubleshooting

### Common Issues

1. **Bot not responding**
   - Check bot token
   - Verify internet connection
   - Check logs for errors

2. **Database connection errors**
   - Verify database credentials
   - Check database service status
   - Test connection manually

3. **Permission errors**
   - Check file permissions
   - Verify user ownership
   - Check directory access

4. **Memory issues**
   - Monitor memory usage
   - Increase swap space
   - Optimize database queries

### Debug Mode

1. **Enable debug logging**
   ```env
   LOG_LEVEL=DEBUG
   ```

2. **Run in foreground**
   ```bash
   python main.py
   ```

3. **Check specific logs**
   ```bash
   tail -f logs/bot.log
   grep ERROR logs/bot.log
   ```

## 📈 Performance Optimization

### Database Optimization

1. **Add indexes**
2. **Optimize queries**
3. **Use connection pooling**
4. **Regular maintenance**

### System Optimization

1. **Increase file limits**
   ```bash
   echo "* soft nofile 65536" >> /etc/security/limits.conf
   echo "* hard nofile 65536" >> /etc/security/limits.conf
   ```

2. **Optimize Python**
   ```bash
   export PYTHONOPTIMIZE=1
   ```

3. **Use production WSGI server** (if using webhooks)

## 🔄 Updates and Maintenance

### Update Process

1. **Backup current installation**
2. **Stop the bot**
3. **Pull latest changes**
4. **Update dependencies**
5. **Run database migrations**
6. **Start the bot**
7. **Verify functionality**

### Maintenance Schedule

- **Daily**: Check logs, monitor performance
- **Weekly**: Review backups, check disk space
- **Monthly**: Update dependencies, security patches
- **Quarterly**: Full system review, optimization

## 📞 Support

For deployment issues:
1. Check logs first
2. Review this guide
3. Check GitHub issues
4. Contact support with detailed error information

---

**Remember**: Always test deployments in a staging environment first!
