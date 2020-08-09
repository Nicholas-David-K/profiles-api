from rest_framework import viewsets

from profiles.models import UserProfile

from profiles.api.serializers import UserProfileSerializer

from rest_framework.permissions import IsAuthenticated

from profiles.api.permissions import IsProfileOwnerOrReadOnly

from rest_framework.filters import SearchFilter


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated, IsProfileOwnerOrReadOnly]
    filter_backends = [ SearchFilter ]
    search_fields = ['name', 'email'] 


class UserLoginAPIView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
