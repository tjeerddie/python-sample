from django.db import models


class Questionnaire(models.Model):
    """ Questionnaire Model for storing questionnaire related details """
    __tablename__ = "questionnaire"

    name = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255, blank=False)
    status = models.CharField(max_length=20, blank=False)
    questions = models.ManyToManyField(
        'Question',
        blank=False,
        through='QuestionLink'
    )
