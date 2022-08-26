from api.mixins import MyViewSet
from api.permissions import IsAdminOrReadOnly, IsAdminOrSuperUser, IsAdmin
from api.serializers import (CategorySerializer, GenreSerializer,
                             JWTokenSerializer, ProfileSerializer,
                             SignUpSerializer, TitleSerializer, UserSerializer)
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import filters, status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from reviews.models import Category, Genre, Title, Token, User


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    serializer = SignUpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = get_object_or_404(
            User,
            username=serializer.validated_data["username"], )
        confirmation_code = default_token_generator.make_token(user)
        send_mail(
            subject="Sign Up",
            message=f"Your confirmation code: {confirmation_code}",
            from_email=None,
            recipient_list=[user.email], )
        Token.objects.create(user=user, token=confirmation_code)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
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

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return (IsAdminOrReadOnly(),)
        return super().get_permissions()

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
        if request.method == 'GET':
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryViewSet(MyViewSet):

    """Получение списка всех категорий.
    Добавление новых категорий.
    Удаление категорий.
    Поиск по названию категорий.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permissions_classes = (IsAdmin, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )
    lookup_field = "slug"
    pagination_class = LimitOffsetPagination


class GenreViewSet(MyViewSet):

    """Получение списка всех жанров.
    Добавление жанров.
    Удаление жанров.
    """

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permissions_classes = (IsAdminOrReadOnly, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ('name', )
    lookup_field = 'slug'
    pagination_class = LimitOffsetPagination


class TitleViewSet(viewsets.ModelViewSet):

    """Получение списка всех произведений.
    Добавление произведений.
    Получение информации о произведении.
    Частисное обновление информации о произведении.
    Удаление произведения.
    """

    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permissions_classes = (IsAdminOrSuperUser,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('category', 'genre', 'name', 'year',)
    pagination_class = LimitOffsetPagination
