# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

#allow user to see the entire list of obj (feeds) without being authenticated yet.
#from rest_framework.permissions import IsAuthenticatedOrReadOnly

#allow user to see the entire list of obj (feeds) only after being authenticated.
# from rest_framework.permissions import IsAuthenticated

from . import serializers, models, permissions


class DepartmentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.DepartmentSerializer

    #allow user to see the lists of object without being authenticated yet.
    # permission_classes = (
    #     permissions.UpdateOwnStatus,
    #     IsAuthenticatedOrReadOnly
    # )

    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    queryset = models.Department.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class StudentViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.StudentSerializer

    #allow user to see the lists of object without being authenticated yet.
    # permission_classes = (
    #     permissions.UpdateOwnStatus,
    #     IsAuthenticatedOrReadOnly
    # )

    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    queryset = models.Student.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)

class SubjectViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.SubjectSerializer

    #allow user to see the lists of object without being authenticated yet.
    # permission_classes = (
    #     permissions.UpdateOwnStatus,
    #     IsAuthenticatedOrReadOnly
    # )

    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    queryset = models.Subject.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class TeacherViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.TeacherSerializer

    #allow user to see the lists of object without being authenticated yet.
    # permission_classes = (
    #     permissions.UpdateOwnStatus,
    #     IsAuthenticatedOrReadOnly
    # )

    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated
    )

    queryset = models.Teacher.objects.all()

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and upating user profiles"""
    serializer_class = serializers.UserProfileSerializer

    #get all objects from db
    queryset = models.UserProfile.objects.all()

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


#overwrite the default Login classes to display on Browser
#so that we can test via Browser
#normally login module is not visible, now we attached this to View
class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
