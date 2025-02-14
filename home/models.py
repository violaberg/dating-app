from django.db import models


class FAQ(models.Model):
    """
    Model representing Frequently Asked Questions (FAQs).

    Attributes:
        question (CharField): The question being asked.
        answer (TextField): The detailed answer to the question.
    """

    class Meta:
        """
        Customizes the display name of the category in the admin panel.
        """
        verbose_name_plural = 'Frequently Asked Questions'

    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
