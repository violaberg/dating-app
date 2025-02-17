from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    descption = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    