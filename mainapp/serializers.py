from rest_framework.serializers import ModelSerializer
from .models import Message


class MessageModelSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'chat_id']
