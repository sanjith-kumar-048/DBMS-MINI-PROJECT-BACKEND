from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'dept', views.DepartmentViewSet)
router.register(r'student', views.StudentViewSet)
router.register(r'subject', views.SubjectViewSet)
router.register(r'teacher', views.TeacherViewSet)
router.register(r'profile', views.UserProfileViewSet)


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.UserLoginApiView.as_view()),
]