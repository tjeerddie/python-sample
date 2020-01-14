from rest_framework import serializers
from api.models import Question


class QuestionReprSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question', 'type']
