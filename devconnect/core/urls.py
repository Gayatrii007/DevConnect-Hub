from django.urls import path
from .views import register, ProfileListCreateView, ProfileRetrieveUpdateDeleteView, PostListCreateView, PostRetrieveUpdateDeleteView
from core.views import health_check, register   # make sure these exist!
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
      # Health check
    path("health/", health_check),

    # Auth
    path("auth/register/", register),
    path("auth/login/", TokenObtainPairView.as_view()),
    path("auth/token/refresh/", TokenRefreshView.as_view()),

    path('profiles/', ProfileListCreateView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileRetrieveUpdateDeleteView.as_view(), name='profile-detail'),

    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
]
