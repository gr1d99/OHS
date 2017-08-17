from django.core.exceptions import ImproperlyConfigured


class TitleMixin(object):
    title = None

    def get_context_data(self, **kwargs):
        c = super(TitleMixin, self).get_context_data(**kwargs)
        if self.title is None:
            raise ImproperlyConfigured(
                """
                %s: You did not provide a Title for this view.
                """ % self.__class__.__name__
            )
        title = self.title
        c['title'] = self.title

        return c

