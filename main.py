import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler

TOKEN = "8140620333:AAF-yB_m0NThmf7KSYvWm4pC03HlBAZ-ZEA"

async def start(update, context):
    await update.message.reply_text("Olá, eu sou o Borrachinho_Bot_Laura! 💋")

async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    await application.run_polling()

if __name__ == "__main__":
    asyncio.run(main())