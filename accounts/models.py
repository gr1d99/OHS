from __future__ import unicode_literals

from mimetypes import MimeTypes
from PIL import Image as Img

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse


VALID_IMAGE_MIMES = ['image/jpeg', 'image/png']


class UserProfile(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        ordering = ('-id', )

    def get_absolute_url(self):
        return reverse('accounts-app:user-profile-view', kwargs=({'slug': self.username, }))

    def get_update_url(self):
        return reverse('accounts-app:update-profile-view', kwargs=({'slug': self.username, }))