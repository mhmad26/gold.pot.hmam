from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = "8706248467:AAH7a-i5GLRWei1Ur813THwSguxV_wigl_I"

async def start(update, context):
    await update.message.reply_text("Hello Muhammad! The gold bot is running successfully 📊")

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is ready! Send /start from your mobile now...")
    app.run_polling()