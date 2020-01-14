from rest_framework import serializers
from api.models import Question, QuestionLink
from api.models.enums import QuestionTypes


class QuestionLinkSerializer(serializers.Serializer):
    question = serializers.CharField(max_length=255, required=True)
    type = serializers.ChoiceField(required=True, choices=QuestionTypes)
    question_key = serializers.CharField(max_length=45, required=True)

    def create(self, validated_data):
        """TODO: Move DB creation to the model"""
        question_key = validated_data.pop('question_key')
        question = self.GetOrCreateQuestion(validated_data)

        question_link = QuestionLink.objects.create(
            questionnaire=validated_data['questionnaire'],
            question=question,
            question_key=question_key,
        )

        return question_link

    def update(self, instance, validated_data):
        if len(instance.question.questionnaires.all()) > 1:
            validated_data['questionnaire'] = instance.questionnaire
            instance.delete()
            return self.create(validated_data)

        instance.question_key = validated_data.get(
            'question_key', instance.question_key
        )

        question = instance.question
        question.question = validated_data.get('question', question.question)
        question.type = validated_data.get('type', question.type)
        question.save()
        instance.save()
        return instance

    def GetOrCreateQuestion(self, question_data):
        questions = Question.objects.all()
        for question in questions:
            if question.equal(question_data):
                return question
        return Question.objects.create(**question_data)
