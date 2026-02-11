from django.core.management import BaseCommand
from bot.handlers import bot


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        bot.remove_webhook()
        print(f"Webhook removed")
