from django.views.generic import CreateView, DetailView, TemplateView
from .forms import HelpRequestForm
from .models import HelpRequest, Service
from helpers.mixins import TitleMixin


class IndexView(TitleMixin, TemplateView):
    template_name = 'index.html'
    title = 'Index'

    def get_context_data(self, **kwargs):
        c = super(IndexView, self).get_context_data(**kwargs)
        c['services'] = Service.objects.all()
        return c


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'service/service_detail.html'

    def get_context_data(self, **kwargs):
        c = super(ServiceDetailView, self).get_context_data(**kwargs)
        form = HelpRequestForm()
        c['form'] = form
        return c

class CreateHelpRequestView(CreateView):
    model = HelpRequest
    form_class = HelpRequestForm
