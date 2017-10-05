from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^service/(?P<slug>[a-zA-Z0-9_-]+)$', views.ServiceDetailView.as_view(), name='service_detail'),
]