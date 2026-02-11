import telebot
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .handlers import bot


@csrf_exempt
def telegram_webhook(request):
    if request.method == "POST":
        json_str = request.body.decode("UTF-8")
        update = telebot.types.Update.de_json(json_str)

        bot.process_new_updates([update])

        return HttpResponse("OK", status=200)

    return JsonResponse({"detail": "Method not allowed"}, status=405)