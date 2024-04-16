from django.contrib.auth.models import User
from django.db import models

from projectapp.models import Project


# Create your models here.


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        # 유저 한명이 하나의 프로젝트를 한번 구독
        unique_together = ('user', 'project')