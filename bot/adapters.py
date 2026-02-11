from asgiref.sync import sync_to_async
from mainapp.models import Message


@sync_to_async
def get_messages():
    return list(Message.objects.all())


@sync_to_async
def create_message_in_db(text, chat_id):
    return Message.objects.create(text=text, chat_id=chat_id)
