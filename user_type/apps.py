# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class UserTypeConfig(AppConfig):
    name = 'user_type'

    def ready(self):
        from . import signals
