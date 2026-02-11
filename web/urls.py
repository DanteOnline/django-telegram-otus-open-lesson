from django.contrib import admin
from django.urls import path, include
from mainapp.views import MessageListView
from mainapp.routers import router

urlpatterns = [
    path('', MessageListView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls))
]
