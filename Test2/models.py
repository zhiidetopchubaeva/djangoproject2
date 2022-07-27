from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Post2(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='posts2', on_delete=models.CASCADE)

    def __str__(self):
        return f"Post {self.user.username} -> {self.title}"


class Comment2(models.Model):
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='comments2', on_delete=models.CASCADE)
    post = models.ForeignKey(Post2, related_name='comments2', on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment {self.user.username} -> {self.post.title} [{self.created_at}]"
