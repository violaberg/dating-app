from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class QuestionCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Question Categories"

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.ForeignKey(QuestionCategory, on_delete=models.CASCADE)
    question_text = models.TextField()
    question_type = models.CharField(
        max_length=50,
        choices=[
            ("single", "Single Choice"),
            ("multiple", "Multiple Choice"),
            ("text", "Text"),
        ],
        default="single",
    )

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=200)

    def __str__(self):
        return self.answer_text


class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(
    Answer,
    on_delete=models.CASCADE,
    blank=True,
    null=True
)

    text_response = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'question')

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text}"
