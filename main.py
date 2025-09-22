"""
Main Telegram bot application for USDT Mining Platform
"""
import logging
import asyncio
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, 
    MessageHandler, ConversationHandler, filters
)
from config.settings import settings
from database.init_data import initialize_database
from handlers.user_handlers import UserHandlers, WAITING_FOR_MINING_AMOUNT
from handlers.admin_handlers import (
    AdminHandlers, WAITING_FOR_BROADCAST_MESSAGE, 
    WAITING_FOR_REJECTION_REASON
)
from automation.profit_scheduler import profit_scheduler
from utils.security import rate_limiter
import sys
import os

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=getattr(logging, settings.LOG_LEVEL),
    handlers=[
        logging.FileHandler(settings.LOG_FILE),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

class MiningBot:
    """Main bot application class"""
    
    def __init__(self):
        self.application = None
        self.is_running = False
    
    def setup_handlers(self):
        """Setup all bot handlers"""
        try:
            # User conversation handler for mining activation
            mining_conv_handler = ConversationHandler(
                entry_points=[CallbackQueryHandler(
                    UserHandlers.activate_mining_callback, 
                    pattern=r'^activate_mining_\d+$'
                )],
                states={
                    WAITING_FOR_MINING_AMOUNT: [
                        MessageHandler(filters.TEXT & ~filters.COMMAND, UserHandlers.mining_amount_handler)
                    ]
                },
                fallbacks=[CommandHandler('cancel', UserHandlers.cancel_command)]
            )
            
            # Admin conversation handler for broadcast
            broadcast_conv_handler = ConversationHandler(
                entry_points=[CallbackQueryHandler(
                    AdminHandlers.broadcast_all_callback,
                    pattern=r'^broadcast_all$'
                )],
                states={
                    WAITING_FOR_BROADCAST_MESSAGE: [
                        MessageHandler(filters.TEXT & ~filters.COMMAND, AdminHandlers.broadcast_message_handler)
                    ]
                },
                fallbacks=[CommandHandler('cancel', UserHandlers.cancel_command)]
            )
            
            # Admin conversation handler for transaction rejection
            rejection_conv_handler = ConversationHandler(
                entry_points=[CallbackQueryHandler(
                    AdminHandlers.reject_transaction_callback,
                    pattern=r'^reject_transaction_\d+$'
                )],
                states={
                    WAITING_FOR_REJECTION_REASON: [
                        MessageHandler(filters.TEXT & ~filters.COMMAND, AdminHandlers.rejection_reason_handler)
                    ]
                },
                fallbacks=[CommandHandler('cancel', UserHandlers.cancel_command)]
            )
            
            # Add conversation handlers first
            self.application.add_handler(mining_conv_handler)
            self.application.add_handler(broadcast_conv_handler)
            self.application.add_handler(rejection_conv_handler)
            
            # Command handlers
            self.application.add_handler(CommandHandler('start', UserHandlers.start_command))
            self.application.add_handler(CommandHandler('admin', AdminHandlers.admin_command))
            
            # User callback handlers
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.register_callback, pattern=r'^register$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.dashboard_callback, pattern=r'^dashboard$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.mining_callback, pattern=r'^mining$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.mining_plans_callback, pattern=r'^mining_plans$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.mining_level_callback, pattern=r'^mining_level_\d+$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.wallet_callback, pattern=r'^wallet$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.deposit_callback, pattern=r'^deposit$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.transactions_callback, pattern=r'^transactions$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.referrals_callback, pattern=r'^referrals$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.referral_link_callback, pattern=r'^referral_link$'
            ))
            
            # Admin callback handlers
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.admin_dashboard_callback, pattern=r'^admin_dashboard$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.admin_users_callback, pattern=r'^admin_users$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.admin_all_users_callback, pattern=r'^admin_all_users$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.admin_transactions_callback, pattern=r'^admin_transactions$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.admin_pending_deposits_callback, pattern=r'^admin_pending_deposits$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.approve_transaction_callback, pattern=r'^approve_transaction_\d+$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.admin_broadcast_callback, pattern=r'^admin_broadcast$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.admin_mining_callback, pattern=r'^admin_mining$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.admin_process_profits_callback, pattern=r'^admin_process_profits$'
            ))
            
            # Navigation handlers
            self.application.add_handler(CallbackQueryHandler(
                UserHandlers.dashboard_callback, pattern=r'^main_menu$'
            ))
            self.application.add_handler(CallbackQueryHandler(
                AdminHandlers.back_to_admin_callback, pattern=r'^admin$'
            ))
            
            # Generic callback handler for unhandled callbacks
            self.application.add_handler(CallbackQueryHandler(self.handle_unknown_callback))
            
            # Error handler
            self.application.add_error_handler(self.error_handler)
            
            logger.info("Bot handlers setup completed")
            
        except Exception as e:
            logger.error(f"Error setting up handlers: {e}")
            raise
    
    async def handle_unknown_callback(self, update: Update, context):
        """Handle unknown callback queries"""
        try:
            query = update.callback_query
            await query.answer("❌ Unknown command. Please try again.")
            logger.warning(f"Unknown callback: {query.data}")
        except Exception as e:
            logger.error(f"Error handling unknown callback: {e}")
    
    async def error_handler(self, update: Update, context):
        """Handle errors"""
        try:
            logger.error(f"Update {update} caused error {context.error}")
            
            # Try to send error message to user
            if update and update.effective_chat:
                try:
                    await context.bot.send_message(
                        chat_id=update.effective_chat.id,
                        text="❌ An unexpected error occurred. Please try again later."
                    )
                except Exception:
                    pass  # Ignore if we can't send error message
                    
        except Exception as e:
            logger.error(f"Error in error handler: {e}")
    
    async def post_init(self, application):
        """Post initialization tasks"""
        try:
            # Initialize database
            initialize_database()
            
            # Start profit scheduler
            profit_scheduler.bot = application.bot
            profit_scheduler.start()
            
            # Send startup notification to super admin
            if settings.SUPER_ADMIN_ID:
                try:
                    startup_message = f"""
🤖 <b>{settings.APP_NAME} Started</b>

✅ Bot is now online and ready to serve users!

🔧 <b>System Status:</b>
• Database: ✅ Connected
• Scheduler: ✅ Running
• Handlers: ✅ Loaded

⏰ <b>Startup Time:</b> {asyncio.get_event_loop().time()}

The mining bot is fully operational.
                    """
                    
                    await application.bot.send_message(
                        chat_id=settings.SUPER_ADMIN_ID,
                        text=startup_message,
                        parse_mode='HTML'
                    )
                except Exception as e:
                    logger.error(f"Error sending startup notification: {e}")
            
            logger.info("Bot post-initialization completed")
            
        except Exception as e:
            logger.error(f"Error in post initialization: {e}")
            raise
    
    async def post_shutdown(self, application):
        """Post shutdown tasks"""
        try:
            # Stop profit scheduler
            profit_scheduler.stop()
            
            # Send shutdown notification to super admin
            if settings.SUPER_ADMIN_ID:
                try:
                    shutdown_message = f"""
🤖 <b>{settings.APP_NAME} Shutdown</b>

⚠️ Bot is going offline for maintenance.

🔧 <b>System Status:</b>
• Database: 🔄 Disconnecting
• Scheduler: ⏹️ Stopped
• Handlers: 🔄 Unloading

⏰ <b>Shutdown Time:</b> {asyncio.get_event_loop().time()}

The bot will be back online shortly.
                    """
                    
                    await application.bot.send_message(
                        chat_id=settings.SUPER_ADMIN_ID,
                        text=shutdown_message,
                        parse_mode='HTML'
                    )
                except Exception as e:
                    logger.error(f"Error sending shutdown notification: {e}")
            
            logger.info("Bot post-shutdown completed")
            
        except Exception as e:
            logger.error(f"Error in post shutdown: {e}")
    
    def run(self):
        """Run the bot"""
        try:
            # Validate configuration
            if not settings.BOT_TOKEN:
                raise ValueError("BOT_TOKEN is required")
            
            # Create application
            self.application = Application.builder().token(settings.BOT_TOKEN).build()
            
            # Setup handlers
            self.setup_handlers()
            
            # Set post init and shutdown hooks
            self.application.post_init = self.post_init
            self.application.post_shutdown = self.post_shutdown
            
            logger.info(f"Starting {settings.APP_NAME}...")
            logger.info(f"Bot username: @{settings.BOT_USERNAME}")
            
            # Run the bot
            self.application.run_polling(
                allowed_updates=Update.ALL_TYPES,
                drop_pending_updates=True
            )
            
        except Exception as e:
            logger.error(f"Error running bot: {e}")
            raise
        finally:
            self.is_running = False

def main():
    """Main entry point"""
    try:
        # Create logs directory if it doesn't exist
        os.makedirs(os.path.dirname(settings.LOG_FILE), exist_ok=True)
        
        # Create uploads directory if it doesn't exist
        os.makedirs(settings.UPLOAD_PATH, exist_ok=True)
        
        # Create and run bot
        bot = MiningBot()
        bot.run()
        
    except KeyboardInterrupt:
        logger.info("Bot stopped by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
