from django.contrib.auth.models import User
from django.db import models


# Create your models here.
# class UserProfile(User):
#     name = models.CharField(max_length=30, null=True, blank=True, verbose_name="姓名")
#     avatar = models.CharField(max_length=100, null=True, blank=True, verbose_name="头像")
#     role = models.CharField(max_length=10, default="员工", verbose_name="角色")
#
#     class Meta:
#         verbose_name = "用户"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.username
