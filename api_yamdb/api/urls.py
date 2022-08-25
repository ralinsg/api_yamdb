from django.urls import include, path
from rest_framework import routers

from .views import (CategoryViewSet, GenreViewSet, TitleViewSet, UserViewSet,
                    jwt_token, signup)

v1_router = routers.DefaultRouter()
v1_router.register(r'users', UserViewSet)
v1_router.register(r'categories', CategoryViewSet)
v1_router.register(r'genres', GenreViewSet)
v1_router.register(r'titles', TitleViewSet)
v1_router.register(
    r'titles/(?P<titles_id>\d+)/',
    TitleViewSet,
    basename='titles'
)

urlpatterns = [
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', jwt_token, name='jwt_token'),
    path('v1/', include(v1_router.urls)),
]
