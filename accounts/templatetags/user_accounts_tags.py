from django import template
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse


register = template.Library()


@register.inclusion_tag('snippets/user_links.html', takes_context=True, name='user_links')
def create_link(context):
    if 'request' in context:
        request = context['request']
        user_registered = False
        profile_url =   None
        create_profile_url = None
        user_profile = None
        try:
            user = request.user
            user_registered = True
            user_profile = reverse('accounts-app:user-profile-view', kwargs=({'slug': request.user}))
            profile_url = user_profile
        except ObjectDoesNotExist:
            create_profile_url = reverse('accounts-app:create-profile-view')
        return {
            'user_registered': user_registered,
            'profile_url': profile_url,
            'create_profile_url': create_profile_url,
        }


@register.simple_tag(name='admin_site_url')
def admin_site_url():
    site = Site.objects.get(id=settings.SITE_ID)
    site_domain = site.domain
    base_url_string = ''
    admin_url_string = '/admin/'
    # construct url here
    base_url_string += base_url_string.join(['/', site_domain, admin_url_string])
    return base_url_string
