from django.shortcuts import render
from rest_framework import viewsets
from .models import User,Post,Like
from .serializers import UserSerializers,PostSerializers,LikeSerializers
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class UserViewSet(viewsets.ModelViewSet):

    """viewset of user instances

    Args:
        viewsets (_type_): _description_
    """

    queryset = User.objects.all()
    serializer_class = UserSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):

    """viewset of post instaces

    Args:
        viewsets (_type_): _description_
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

class LikeViewSet(viewsets.ModelViewSet):

    """viewset of like instaces

    Args:
        viewsets (_type_): _description_
    """

    queryset = Like.objects.all()
    serializer_class = LikeSerializers
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

   


