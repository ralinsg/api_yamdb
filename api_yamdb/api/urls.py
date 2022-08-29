from django.urls import path, include
from .views import signup, jwt_token, UserViewSet
from rest_framework import routers


v1_router = routers.DefaultRouter()
v1_router.register(r'users', UserViewSet)

signup_patterns = [
    path('signup/', signup, name='signup'),
    path('token/', jwt_token, name='jwt_token'),
]

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/', include(signup_patterns))
]
