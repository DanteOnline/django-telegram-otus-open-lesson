from django.contrib import admin
from django.urls import path, include
from mainapp.views import MessageListView


urlpatterns = [
    path('', MessageListView.as_view()),
    path('admin/', admin.site.urls),
]
