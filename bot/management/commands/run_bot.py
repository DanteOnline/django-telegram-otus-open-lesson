from django.core.management import BaseCommand
from bot.handlers import bot


class Command(BaseCommand):

    def handle(self, *args, **options):
        print('Run bot ...')
        bot.infinity_polling()
