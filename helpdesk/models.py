from __future__ import unicode_literals

from django.db import models
from django.db.models.manager import Manager
from django.utils import timezone


class ServiceManager(Manager):
    pass


class Service(models.Model):
    name = models.CharField(max_length=155, unique=True)
    is_active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

