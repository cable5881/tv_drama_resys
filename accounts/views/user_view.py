from rest_framework import generics
from rest_framework import viewsets

from accounts.models import MyUser
from accounts.serializers.user_serializer import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class UserList(generics.ListAPIView):
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = MyUser.objects.all()
#     serializer_class = UserSerializer
