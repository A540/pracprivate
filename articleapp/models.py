from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='article')
    project = models.ForeignKey(Project, on_delete=models.SET_NULL, null=True, related_name='project')

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='articles/', null=False)
    content = models.TextField(null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True)

