from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='articles/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)
