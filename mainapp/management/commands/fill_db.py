from django.core.management import BaseCommand
from mainapp.models import Message
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Delete all users ...')
        User.objects.all().delete()
        print('Create admin ...')
        User.objects.create_superuser(
            'admin',
            'admin@admin.com',
            'admin',
        )
        print('Create messages ...')
        message_list = [
            'One test message',
            'Two test message',
        ]
        messages = [
            Message(text=message) for message in message_list
        ]
        Message.objects.bulk_create(messages)
        print('Done')
