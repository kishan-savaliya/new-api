from rest_framework import serializers
from .models import User,Post,Like

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

    """create and return new 'post' instance, given the validated data.

    Args:
        serializers (_type_): _description_
    """

    liked_by = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()

    class Meta: 

        model = Post
        fields  = ["id","title","user","like_count","liked_by"]

    def get_liked_by(self, obj):
        likes = Like.objects.filter(post=obj)

        return LikeSerializers(likes,many=True).data

    def get_like_count(self,obj):
        likes = Like.objects.filter(post=obj).count()

        return likes

class LikeSerializers(serializers.ModelSerializer):

    """create and return new 'like' instance, given the validated data.

    Args:
        serializers (_type_): _description_
    """

    user = UserSerializers()

    class Meta:

        model = Like
        fields = ['like','post','user']
         
