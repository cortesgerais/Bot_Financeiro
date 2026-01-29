from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from config import BOT_TOKEN

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot Financeiro ativo!\n\n"
        "Envie um gasto assim:\n"
        "42,90 mercado\n"
        "ou use /help"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Comandos disponíveis:\n"
        "/start - iniciar bot\n"
        "/help - ajuda\n\n"
        "Envie mensagens como:\n"
        "50 mercado\n"
        "200 academia 2x"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text
    await update.message.reply_text(f"Mensagem recebida: {texto}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
