from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone

from accounts.models import UserProfile
from .managers import ServiceManager


class Service(models.Model):
    name = models.CharField(max_length=155, unique=True)
    slug = models.SlugField(null=True, blank=True, help_text="Leave this field blank")
    description = models.TextField()
    is_active = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)

    objects = ServiceManager()

    def get_absolute_url(self):
        return reverse('helpdesk:service_detail', kwargs={'slug': self.slug, })

    def __str__(self):
        return self.name


class HelpRequest(models.Model):
    for_service = models.ForeignKey(Service, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)
    is_handled = models.BooleanField(default=False)

    def __str__(self):
        return self.for_service.name
