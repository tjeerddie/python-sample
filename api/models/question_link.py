from django.db import models


class QuestionLink(models.Model):
    """ question link Model for storing question link related details """

    question_key = models.CharField(max_length=45, blank=False)
    question = models.ForeignKey(
        'Question',
        blank=False,
        on_delete=models.CASCADE
    )
    questionnaire = models.ForeignKey(
        'Questionnaire',
        blank=False,
        related_name='question_links',
        on_delete=models.CASCADE
    )

    class Meta:
        unique_together = [
            ['question', 'questionnaire'], ['questionnaire', 'question_key']
        ]
