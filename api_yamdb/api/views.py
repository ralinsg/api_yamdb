from django.shortcuts import get_object_or_404
from reviews.models import User, Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, action
from .serializers import SignUpSerializer, JWTokenSerializer, UserSerializer
from .serializers import ProfileSerializer
from rest_framework.permissions import AllowAny
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from .permissions import IsAdminOrSuperUser
from rest_framework.permissions import IsAuthenticated
from django.conf import settings


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user, created = User.objects.get_or_create(serializer.data)
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject="Sign Up",
        message=f"Your confirmation code: {confirmation_code}",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user.email], )
    Token.objects.create(user=user, token=confirmation_code)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([AllowAny])
def jwt_token(request):
    serializer = JWTokenSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data["username"]
        user = get_object_or_404(User, username=username,)
        confirmation_code = serializer.validated_data["confirmation_code"]
        token = Token.objects.get(user=user)
        if confirmation_code == token.token:
            jwt_token = AccessToken.for_user(user)
            return Response(
                {"token": str(jwt_token)}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Your code is not valid"},
            status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminOrSuperUser, )
    lookup_field = "username"

    @action(
        methods=["GET", "PATCH"],
        url_path="me",
        url_name="me",
        serializer_class=ProfileSerializer,
        permission_classes=(IsAuthenticated, ),
        detail=False, )
    def profile(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = self.get_serializer(user, many=False)
        if request.method == "GET":
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
