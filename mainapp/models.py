from django.db import models


class Message(models.Model):
    text = models.TextField()
    chat_id = models.PositiveBigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.text
