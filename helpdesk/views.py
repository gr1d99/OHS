from django.views.generic import TemplateView
from helpers.mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'helpdesk/index.html'
    title = 'Index'