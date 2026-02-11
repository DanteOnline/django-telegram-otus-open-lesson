from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from .models import Message
from .serializers import MessageModelSerializer


class MessageViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageModelSerializer
