from __future__ import unicode_literals

import StringIO
from mimetypes import MimeTypes
from PIL import Image as Img

from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.urlresolvers import reverse


VALID_IMAGE_MIMES = ['image/jpeg', 'image/png']


class UserProfile(AbstractUser):
    profile_picture = models.FileField(upload_to='profile_pictures', null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        mime = MimeTypes()
        try:
            if not mime.guess_type(self.profile_picture.url)[0] in VALID_IMAGE_MIMES:
                pass
            else:
                image = Img.open(StringIO.StringIO(self.profile_picture.read()))
                image.thumbnail((400, 400), Img.ANTIALIAS)
                output = StringIO.StringIO()
                image.save(output, format='JPEG', quality=99)
                output.seek(0)
                img = self.profile_picture = InMemoryUploadedFile(output, 'FileField',
                                                                  "%s" % self.profile_picture.name, 'image/jpeg',
                                                                  output.len, None)
        except Exception as e:
            pass

        super(UserProfile, self).save(*args, **kwargs)

    class Meta:
        ordering = ('-id', )

    def get_absolute_url(self):
        return reverse('accounts-app:user-profile-view', kwargs=({'slug': self.username, }))

    def get_update_url(self):
        return reverse('accounts-app:update-profile-view', kwargs=({'slug': self.username, }))