from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-Binary'),
        ('other', 'Other'),
        ('prefer_not_say', 'Prefer not to say'),
    ]

    RELATIONSHIP_GOALS = [
        ('casual', 'Casual Dating'),
        ('serious', 'Serious Relationship'),
        ('friendship', 'Friendship'),
        ('unsure', 'Not Sure Yet'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True, help_text="Tell others about yourself.")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='prefer_not_say')
    age = models.PositiveIntegerField(blank=True, null=True, help_text="Enter your age.")
    location = models.CharField(max_length=255, blank=True, null=True)
    interests = models.TextField(blank=True, null=True, help_text="List your hobbies and interests.")
    relationship_goal = models.CharField(max_length=20, choices=RELATIONSHIP_GOALS, default='unsure')
    profile_image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')
    gender_preference = models.CharField(max_length=50, blank=True, null=True)
    spark_type = models.CharField(max_length=50, blank=True, null=True)
    age_preference = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
