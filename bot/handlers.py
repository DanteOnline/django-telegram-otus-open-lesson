from .bot import bot
from mainapp.models import Message


@bot.message_handler(commands=['messages'])
def messages_handler(message):
    messages = Message.objects.all()
    for item_message in messages:
        bot.send_message(message.chat.id, f'{item_message.text} {item_message.chat_id}')


# @bot.message_handler(func=lambda message: True)
# def create_message(message):
#     text = message.text
#     chat_id = message.from_user.id
#     Message.objects.create(text=text, chat_id=chat_id)
#     bot.send_message(message.chat.id, 'Сообщение сохранено')
