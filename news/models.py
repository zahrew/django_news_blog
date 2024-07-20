from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    #blog_id = models.AutoField(primary_key = True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blogs')
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title


class User_Like_Blog(models.Model):
    #ulb_id = models.AutoField(primary_key = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog')

    def __str__(self):
        return f'{self.user.username} likes {self.blog.title}'
