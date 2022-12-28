from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User,Post,Like
from .serializers import UserSerializers,PostSerializers,LikeSerializers

# @api_view(['GET','POST'])
# def allpost(request):
#     id = request.data    
#     post_list = Post.objects.all()
#     like_count = Like.objects.filter(post_id = id).count()
#     post_serializer = PostSerializers(post_list,many=True,context={"like_count":like_count})
#     return Response(request,post_serializer.data)

class UserViewSet(viewsets.ModelViewSet):

    """viewset of user instances

    Args:
        viewsets (_type_): _description_
    """

    queryset = User.objects.all()
    serializer_class = UserSerializers

class PostViewSet(viewsets.ModelViewSet):

    """viewset of post instaces

    Args:
        viewsets (_type_): _description_
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializers

class LikeViewSet(viewsets.ModelViewSet):

    """viewset of like instaces

    Args:
        viewsets (_type_): _description_
    """

    queryset = Like.objects.all()
    serializer_class = LikeSerializers

   


