from django import template
from helpdesk.models import Service


register = template.Library()


@register.simple_tag
def get_services():
    return Service.objects.actice()