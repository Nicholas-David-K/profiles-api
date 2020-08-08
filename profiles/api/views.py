from rest_framework import viewsets
from profiles.models import UserProfile
from profiles.api.serializers import UserProfileSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer