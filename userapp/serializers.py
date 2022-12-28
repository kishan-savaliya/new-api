from rest_framework import serializers
from .models import User,Post,Like
# from rest_framework.response import Response
# from django.views.decorators.csrf import csrf_exempt

class UserSerializers(serializers.ModelSerializer):

    """create and return new 'user' instance, given the validated data.

    Args:
        serializers (_type_): _description_
    """

    post = serializers.SlugRelatedField(many=True, read_only= True, slug_field="title")

    class Meta:

        model = User
        fields = ['id','name','gender','post']

class PostSerializers(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField("like_count")
    class Meta:
        model = Post
        fields  = ("__all__")

    def like_count(self,obj):
        total_like = self.context.get("like_count")
        return total_like

# class PostSerializers(serializers.ModelSerializer):

#     """create and return new 'post' instance, given the validated data.

#     Args:
#         serializers (_type_): _description_
#     """
    
#     # like = serializers.SlugRelatedField(many=True, read_only= True, slug_field="like")

#     class Meta:

#         model = Post
#         fields = ['id','title','user','likes_count']

class LikeSerializers(serializers.ModelSerializer):

    """create and return new 'like' instance, given the validated data.

    Args:
        serializers (_type_): _description_
    """

    class Meta:

        model = Like
        fields = ['like','post']

# @csrf_exempt
# def post_like_count(request, pk):
#     try:
#         post = Post.objects.get(pk=pk)
#     except Post.DoesNotExist:
#         return Response(status=404)

#     if request.method == 'GET':
#         like_count = Like.objects.filter(post=post).count()
#         serializer = PostSerializers(post, data={'like_count': like_count})
#         serializer.is_valid()
#         return Response(serializer.data)





