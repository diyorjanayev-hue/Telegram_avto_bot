import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")
CHANNEL_USERNAME = os.getenv("CHANNEL_USERNAME")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Matn yuboring, kanalga tashlayman.")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    post_template = f"""
📢 YANGI E'LON

{text}

🔰 Batafsil: @Avto|Bozor|Uz
"""
    await context.bot.send_message(chat_id=CHANNEL_USERNAME, text=post_template)
    await update.message.reply_text("✅ Kanalga joylandi!")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()I'm
