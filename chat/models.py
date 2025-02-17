from django.db import models

class ChatRoom(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    friendly_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.friendly_name or self.name
    