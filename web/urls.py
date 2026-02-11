from django.contrib import admin
from django.urls import path, include
from mainapp.views import MessageListView
from bot.views import telegram_webhook


urlpatterns = [
    path('', MessageListView.as_view()),
    path('admin/', admin.site.urls),
    path("webhook/", telegram_webhook),
]
