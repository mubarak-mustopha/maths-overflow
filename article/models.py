from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    photo = models.ImageField(null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-updated", "-created"]

    def get_absolute_url(self):
        return "/article/post/%i/" % self.id

    def __str__(self):
        return self.text[:50]


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()

    photo = models.ImageField(null=True, blank=True)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return "/article/post/%i/" % self.post.id

    def __str__(self):
        return self.text[:50]
