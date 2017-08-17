from django.core.urlresolvers import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView
from .forms import CreateUserProfileForm
from .models import UserProfile
from . import mixins


class CreateUserProfileView(LoginRequiredMixin, CreateView):
    form_class = CreateUserProfileForm
    template_name = 'accounts/create_profile_form.html'

    def get_success_url(self):
        messages.success(self.request, 'Profile successfully created.')
        return reverse('accounts-app:user-profile-view', kwargs=({'slug': self.request.user.username, }))

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateUserProfileView, self).form_valid(form)


class UserProfileView(LoginRequiredMixin, mixins.CheckIfProfileExist, DetailView):
    model = UserProfile
    template_name = 'accounts/profile_detail.html'
    slug_field = 'username'

    def get_context_data(self, **kwargs):
        c = super(UserProfileView, self).get_context_data(**kwargs)
        user = UserProfile.objects.get(username=self.request.user)
        c['profile'] = user
        return c


class UpdateUserProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    form_class = CreateUserProfileForm

    def get_success_url(self):
        messages.success(self.request, 'Profile successfully updated.')
        return reverse('accounts-app:user-profile-view', kwargs=({'slug': self.request.user.username, }))


class StaffUsersView(TemplateView):
    template_name = 'staff/staff_template.html'
