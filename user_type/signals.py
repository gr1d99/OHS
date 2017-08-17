import logging

from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import post_save
from django.template.defaultfilters import slugify
from .models import SpecialUser


def create_usergroup(name):
    group = None
    try:
        group = Group.objects.get(name=name)

    except Group.DoesNotExist:
        group = Group.objects.create(
            name=name
        )

    return group


def create_permission(name):
    permission = None
    content_type = ContentType.objects.get_for_model(SpecialUser)
    codename = slugify(name)
    try:
        permission = Permission.objects.get(codename=codename)

    except Permission.DoesNotExist:
        permission = Permission.objects.create(
            codename=codename,
            name=name,
            content_type=content_type
        )

    return permission


def assign_permssion(group, permission, user):
    status = False
    try:
        group.permissions.add(permission)
        group.user_set.add(user)
        status = True

    except Exception as e:
        logging.warning(e)

    return status


def handle_usertype(sender, instance, created, **kwargs):
    create_group = instance.create_group
    permission = instance.permission_name
    user = instance.user
    if create_group and permission:
        group = create_usergroup(instance.usertype.name)
        permission = create_permission(permission)
        assign_permssion(group, permission, user)


post_save.connect(handle_usertype, SpecialUser)