from os import getenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)
from dotenv import load_dotenv
from rest import get_messages, create_message


load_dotenv()


async def messages_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    messages = await get_messages()
    for message in messages:
        await update.message.reply_text(f'{message['text']} {message['chat_id']}')


async def text_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_id = update.effective_user.id
    text = update.message.text
    response = await create_message(text, user_id)

    if response.status_code == 201:
        answer = 'Сообщение было сохранено'
    else:
        answer = f'Ошибка {response.status_code} при сохранении'
    await update.message.reply_text(answer)


bot_token = getenv('BOT_TOKEN')

app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("messages", messages_handler))
# app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_handler))

app.run_polling()
