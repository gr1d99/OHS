# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserType, SpecialUser

admin.site.register(UserType)
admin.site.register(SpecialUser)