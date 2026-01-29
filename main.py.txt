from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

from config import BOT_TOKEN
from database import create_tables, set_setting, get_setting

create_tables()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Olá! 👋\n"
        "Vamos configurar seu controle financeiro.\n\n"
        "💰 Qual é o VALOR MENSAL TOTAL de gastos da família?"
    )
    context.user_data["step"] = "ASK_TOTAL"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    step = context.user_data.get("step")

    if step == "ASK_TOTAL":
        try:
            total = float(update.message.text.replace(",", "."))
            set_setting("monthly_total", total)
            context.user_data["step"] = None

            await update.message.reply_text(
                f"✅ Valor mensal definido: R$ {total:.2f}\n\n"
                "Em breve vamos criar os envelopes."
            )
        except:
            await update.message.reply_text(
                "❌ Valor inválido. Envie apenas números.\n"
                "Exemplo: 5000"
            )
    else:
        await update.message.reply_text(
            "Use /start para iniciar a configuração."
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
