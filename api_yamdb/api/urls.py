from django.urls import path, include
from .views import signup, jwt_token, UserViewSet
from rest_framework import routers


v1_router = routers.DefaultRouter()
v1_router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', jwt_token, name='jwt_token'),
    path('v1/', include(v1_router.urls)),
]
