from accounts.models import UserProfile
from django import http
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist


class CheckIfProfileExist(object):
    def dispatch(self, request, *args, **kwargs):
        try:

            slug = request.user.username
            user = UserProfile.objects.get(username=slug)
            userprofile = user
            return super(CheckIfProfileExist, self).dispatch(request, *args, **kwargs)
        except ObjectDoesNotExist:
            messages.info(request, 'It is a requirement that you provide us with your phone number!!')
            return http.HttpResponseRedirect(reverse('accounts-app:create-profile-view'))
