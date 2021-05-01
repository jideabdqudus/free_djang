from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('viewset', views.HelloViewSet, basename='viewset')
router.register('profile-viewset', views.UserProfileViewSet)

urlpatterns = [
    path('hello', views.HelloApiView.as_view()),
    path('login', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
