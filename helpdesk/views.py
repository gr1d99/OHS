from django.views.generic import TemplateView
from .models import Service
from helpers.mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'helpdesk/index.html'
    title = 'Index'

    def get_context_data(self, **kwargs):
        c = super(IndexView, self).get_context_data(**kwargs)
        c['services'] = Service.objects.all()
        return c