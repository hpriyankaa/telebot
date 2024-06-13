from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = '7203979984:AAFDLD5N7R-K0F352tDjfLyBcLHddVqVNz8'
BOT_USERNAME: Final = 'caketalesbot'


# commands

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi welcome to caketales! Happy to help you!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("what do you want to look into?")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("place your order")


# responses

def handle_respone(text: str) -> str:
    processed: str = text.lower()
    if 'hello' in processed:
        return 'Welcome to caketales, what do you want please?'
    if 'order' in processed:
        return 'please place the order at the website.'
    if 'cancel' in processed:
        return 'order  once placed cannot be cancelled'

    return ' this is an auto generated response, contact the customer care'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in  {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_respone(new_text)
        else:
            return
    else:
        response: str = handle_respone(text)
    print("Bot: ", response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update: {update} caused error {context.error}')


if __name__ == '__main__':
    print("startingg")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)
    print("polling")
    app.run_polling(poll_interval=3)


