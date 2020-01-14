from rest_framework import viewsets, status, permissions
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from django.http import Http404
from api.models import Questionnaire
from api.serializers import QuestionLinkSerializer
from api.serializers.representational import QuestionLinkReprSerializer


@permission_classes((permissions.AllowAny,))
class QuestionLinkViewSet(viewsets.ViewSet):
    def get_object(self, pk):
        try:
            return Questionnaire.objects.get(pk=pk)
        except Questionnaire.DoesNotExist:
            raise Http404

    def list(self, request, questionnaire_pk):
        """List of all questions in a questionnaire"""
        questionnaire = self.get_object(questionnaire_pk)
        question_links = questionnaire.question_links.all()
        serializer = QuestionLinkReprSerializer(question_links, many=True)
        return Response(serializer.data)

    def create(self, request, questionnaire_pk):
        serializer = QuestionLinkSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        questionnaire = self.get_object(questionnaire_pk)
        question = {
            'question': serializer.validated_data['question'],
            'type': serializer.validated_data['type']
        }

        question_link = serializer.save(questionnaire=questionnaire)
        repr_serializer = QuestionLinkReprSerializer(question_link)
        return Response(repr_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, questionnaire_pk, pk):
        questionnaire = self.get_object(questionnaire_pk)
        try:
            question_link = questionnaire.question_links.get(question=pk)
        except Exception:
            raise Http404

        serializer = QuestionLinkReprSerializer(question_link)
        return Response(serializer.data)

    def update(self, request, questionnaire_pk, pk):
        questionnaire = self.get_object(questionnaire_pk)
        try:
            question_link = questionnaire.question_links.get(question=pk)
        except Exception:
            raise Http404

        serializer = QuestionLinkSerializer(question_link, data=request.data)
        if not serializer.is_valid():
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        question_link = serializer.save()
        repr_serializer = QuestionLinkReprSerializer(question_link)
        return Response(repr_serializer.data)

    def destroy(self, request, questionnaire_pk, pk):
        questionnaire = self.get_object(questionnaire_pk)
        question = questionnaire.questions.get(id=pk)
        if not question:
            return Response(status=status.HTTP_404_NOT_FOUND)

        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
