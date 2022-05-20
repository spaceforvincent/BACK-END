from django.db import models
from django.conf import settings


class Review(models.Model):
    title = models.CharField(max_length=100)
    # movie_title = models.CharField(max_length=50)
    # rank = models.IntegerField()
    # content = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
            return self.title


class Comment(models.Model):
    content = models.TextField()
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.title
