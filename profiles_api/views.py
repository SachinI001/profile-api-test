from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from . import serializers
from . import models
from . import permissions


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    permission_classes = (permissions.UpdateOwnProfile, IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
