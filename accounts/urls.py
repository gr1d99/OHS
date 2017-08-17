from django.conf.urls import url
from . import views

app_name = 'accounts-app'

urlpatterns = [
    url(r'^create-profile/$', views.CreateUserProfileView.as_view(), name="create-profile-view"),
    url(r'^(?P<slug>[a-zA-Z0-9-]+)$', views.UserProfileView.as_view(), name="user-profile-view"),
    url(r'^staff-member/$', views.StaffUsersView.as_view(), name="staff-users"),
    url(r'^update/(?P<slug>[a-zA-Z0-9-]+)$', views.UpdateUserProfileView.as_view(), name="update-profile-view"),
]