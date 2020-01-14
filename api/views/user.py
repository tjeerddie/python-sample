from rest_framework import viewsets, permissions
from rest_framework.decorators import permission_classes
from api.models import User
from api.serializers import UserSerializer


@permission_classes((permissions.AllowAny,))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
