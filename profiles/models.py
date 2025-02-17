from django.db import models
from django.contrib.auth.models import User
from questionnaire.models import Choice


class Profile(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('non-binary', 'Non-Binary'),
        ('other', 'Other'),
        ('prefer_not_say', 'Prefer not to say'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True, help_text="Tell others about yourself.")
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default='prefer_not_say')
    age = models.PositiveIntegerField(blank=True, null=True, help_text="Enter your age.")
    location = models.CharField(max_length=255, blank=True, null=True)
    interests = models.TextField(blank=True, null=True, help_text="List your hobbies and interests.")
    profile_image = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpg')

    # Questionnaire-related fields
    gender_preferences = models.ManyToManyField(
        Choice,
        related_name='profiles_gender_preference',
        blank=True
    )
    spark_type = models.ForeignKey(
        Choice,
        on_delete=models.SET_NULL,
        related_name='profiles_spark_type',
        null=True, blank=True
    )
    age_preferences = models.ManyToManyField(
        Choice,
        related_name='profiles_age_preference',
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"


class Report(models.Model):
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports_made")
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reports_received")
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reporter.username} reported {self.reported_user.username}"

