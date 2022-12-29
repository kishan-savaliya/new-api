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

    class Meta: 

        model = Post
        fields  = ["id","title","user","likes_count"]

class LikeSerializers(serializers.ModelSerializer):

    """create and return new 'like' instance, given the validated data.

    Args:
        serializers (_type_): _description_
    """
    users = serializers.CharField(source = 'user.name')

    class Meta:

        model = Like
        fields = ['like','post','user','users']
