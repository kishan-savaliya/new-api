from django.db import models

Like_choices = (
    ('like','like'),
)

class User(models.Model):

    """create model for user instances.

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """

    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_name(self):
        return self.name

class Post(models.Model):

    """create model for post instances.

    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """

    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='post')

    def __str__(self):
        return self.title

    def get_user(self):
        return self.user.get_name()

    def likes_count(self):
        return self.likes.all().count()

class Like(models.Model):

    """create model for like instances.
    Args:
        models (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    like = models.CharField(max_length=100, choices=Like_choices)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_user(self):
        return self.user.get_name()

    # def __str__(self):
    #     return self.user

    # def __repr__(self):
    #     return f'{self.user}'