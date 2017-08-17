# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import UserProfile
# Create your models here.


class UserType(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class SpecialUser(models.Model):
    user = models.OneToOneField(UserProfile, related_name='special_user', null=True, on_delete=models.CASCADE)
    usertype = models.ForeignKey(UserType, related_name='user_types', on_delete=models.CASCADE)
    create_group = models.BooleanField(default=True)
    permission_name = models.CharField(unique=True, max_length=20, null=True)

    def __str__(self):
        return '%s - %s ' % (self.user.username, self.usertype.name)
