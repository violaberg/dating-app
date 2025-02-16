from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    QUESTION_TYPES = (
        ("SINGLE", "Single Choice"),
        ("MULTIPLE", "Multiple Choice"),
    )

    question_text = models.TextField()  # Changed from text to question_text
    question_type = models.CharField(max_length=50)  # Changed max_length to 50
    category_id = models.BigIntegerField()  # Added to match the database
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(
        Question, related_name="choices", on_delete=models.CASCADE
    )
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    spark_type = models.ForeignKey(
        Choice,
        related_name="spark_responses",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    gender_preferences = models.ManyToManyField(
        Choice, related_name="gender_responses", blank=True
    )
    age_preferences = models.ManyToManyField(
        Choice, related_name="age_responses", blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Responses for {self.user.username}"
