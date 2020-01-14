from django.db import models
from .enums import QuestionTypes


class Question(models.Model):
    """ Question Model for storing question related details """

    question = models.CharField(max_length=255, blank=False)
    type = models.CharField(max_length=100, blank=False, choices=QuestionTypes)
    questionnaires = models.ManyToManyField(
        'Questionnaire',
        through='QuestionLink'
    )
