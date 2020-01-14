from rest_framework import serializers
from api.models import QuestionLink
from . import QuestionReprSerializer


class QuestionLinkReprSerializer(serializers.ModelSerializer):
    question = QuestionReprSerializer()

    class Meta:
        model = QuestionLink
        fields = [
            'id', 'question_key', 'question'
        ]

    def to_representation(self, instance):
        """Convert `username` to lowercase."""
        ret = super().to_representation(instance)
        question = ret.pop('question')
        return {**ret, **question, "question_link_id": ret["id"]}
