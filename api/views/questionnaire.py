from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from api.models import Questionnaire
from api.serializers import QuestionnaireSerializer


@permission_classes((permissions.AllowAny,))
class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
