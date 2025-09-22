# 🚀 Deployment Checklist

## Before Deploying

### ✅ Bot Setup
- [ ] Get bot token from @BotFather
- [ ] Get your Telegram user ID from @userinfobot
- [ ] Test bot locally first (optional but recommended)

### ✅ Files Ready
- [ ] All project files in telegram_bot folder
- [ ] requirements.txt present
- [ ] Procfile created (for Heroku/Railway)
- [ ] runtime.txt created
- [ ] .env.example file present (don't upload .env with real tokens!)

### ✅ Environment Variables to Set
```
BOT_TOKEN=your_bot_token_from_botfather
BOT_USERNAME=your_bot_username_without_@
ADMIN_USER_IDS=your_telegram_user_id
SUPER_ADMIN_ID=your_telegram_user_id
DATABASE_URL=sqlite:///mining_bot.db
APP_NAME=USDT Mining Bot
```

### ✅ Optional Variables (for production)
```
USDT_WALLET_ADDRESS=your_usdt_wallet
BTC_WALLET_ADDRESS=your_btc_wallet
ETH_WALLET_ADDRESS=your_eth_wallet
SUPPORT_USERNAME=your_support_username
CHANNEL_USERNAME=your_channel_username
```

## Deployment Steps

### Railway (Recommended)
1. [ ] Create GitHub repository
2. [ ] Upload telegram_bot folder contents
3. [ ] Sign up at railway.app with GitHub
4. [ ] Deploy from GitHub repo
5. [ ] Add environment variables
6. [ ] Bot should start automatically

### Render
1. [ ] Create GitHub repository
2. [ ] Sign up at render.com
3. [ ] Create Background Worker
4. [ ] Connect GitHub repo
5. [ ] Set build/start commands
6. [ ] Add environment variables

### Heroku
1. [ ] Install Heroku CLI
2. [ ] Create Heroku app
3. [ ] Set environment variables
4. [ ] Deploy via git
5. [ ] Scale worker to 1

## After Deployment

### ✅ Testing
- [ ] Check deployment logs for errors
- [ ] Test bot with /start command
- [ ] Test admin commands with /admin
- [ ] Verify database is working
- [ ] Test mining activation
- [ ] Test wallet features

### ✅ Monitoring
- [ ] Check bot is responding
- [ ] Monitor resource usage
- [ ] Set up log monitoring
- [ ] Test automated profit calculation

## Troubleshooting

### Common Issues
- **Bot not responding**: Check bot token and environment variables
- **Database errors**: Verify DATABASE_URL is set correctly
- **Import errors**: Check all dependencies in requirements.txt
- **Permission errors**: Verify admin user IDs are correct

### Debug Commands
```bash
# Check logs (Railway/Render)
View logs in dashboard

# Check environment variables
echo $BOT_TOKEN

# Test database connection
python -c "from database.database import db_manager; print('DB OK')"
```

## Success Indicators

When deployment is successful, you should see in logs:
```
INFO - Starting USDT Mining Bot...
INFO - Bot username: @your_bot_username
INFO - Database initialized successfully
INFO - Profit scheduler started successfully
INFO - Bot post-initialization completed
```

## Free Tier Limitations

### Railway
- 500 hours/month free
- $5 credit monthly
- Sleeps after 30 min inactivity

### Render
- 750 hours/month free
- Sleeps after 15 min inactivity
- Slower cold starts

### Heroku
- 550-1000 hours/month
- Sleeps after 30 min inactivity
- Requires credit card for verification

### PythonAnywhere
- Always-on tasks available
- Limited CPU seconds
- Good for small bots

## Keeping Bot Alive

For platforms that sleep (Railway, Render, Heroku):

1. **Use UptimeRobot** (free):
   - Create account at uptimerobot.com
   - Add HTTP monitor for your bot's health endpoint
   - Pings every 5 minutes to keep alive

2. **Create Health Endpoint** (already included in bot):
   - Bot responds to health checks
   - Prevents sleeping

## Scaling Up

When you outgrow free tiers:
- Railway: $5/month for more hours
- Render: $7/month for always-on
- DigitalOcean: $5/month VPS
- AWS/GCP: Pay-as-you-use

---

**🎉 Your bot will be live 24/7 and ready to serve users worldwide!**
