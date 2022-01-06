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
    queryset = models.Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = []

class StudentViewSet(viewsets.ModelViewSet):
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    permission_classes = []


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = models.Subject.objects.all()
    serializer_class = serializers.SubjectSerializer
    permission_classes = []

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = models.Teacher.objects.all()
    serializer_class = serializers.TeacherSerializer
    permission_classes = []


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
