from __future__ import unicode_literals

from django.db import models
from django.db.models.manager import Manager
from django.utils import timezone

from .managers import ServiceManager


class Service(models.Model):
    name = models.CharField(max_length=155, unique=True)
    slug = models.SlugField(null=True, blank=True)
    is_active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    objects = ServiceManager()

    def __str__(self):
        return self.name

