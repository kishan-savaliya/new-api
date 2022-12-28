from django.contrib import admin
from .models import User,Post,Like

@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    """register user instances fields.

    Args:
        admin (_type_): _description_
    """
    list_display = ['id','name','gender','post']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    """register post instances fields.

    Args:
        admin (_type_): _description_
    """

    list_display = ['id','title','user','like']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    """register like instances fields.

    Args:
        admin (_type_): _description_
    """

    list_display = ['like','post']