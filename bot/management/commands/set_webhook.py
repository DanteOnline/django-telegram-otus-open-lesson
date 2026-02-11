from django.conf import settings
from django.core.management import BaseCommand
from bot.handlers import bot


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        webhook_url = f"{settings.WEBHOOK_URL}/webhook/"
        bot.remove_webhook()
        bot.set_webhook(url=webhook_url)
        print(f"Webhook set to {webhook_url}")