from .bot import bot
from .adapters import get_messages, create_message_in_db


@bot.message_handler(commands=['messages'])
async def messages_handler(message):
    messages = await get_messages()
    for item_message in messages:
        await bot.send_message(message.chat.id, f'{item_message.text} {item_message.chat_id}')


@bot.message_handler(func=lambda message: True)
async def create_message(message):
    text = message.text
    chat_id = message.from_user.id
    await create_message_in_db(text, chat_id)
    await bot.send_message(message.chat.id, 'Сообщение сохранено')
