from django.db.models.manager import Manager, QuerySet


class ServiceQuerySet(QuerySet):
    def active(self):
        """Filter out Services that are active"""
        return self.filter(is_active=True)


class ServiceManager(Manager):
    def get_query_set(self):
        return ServiceQuerySet(self.model)

    def __getattr__(self, attr, *args):
        # see https://code.djangoproject.com/ticket/15062 for details
        if attr.startswith("_"):
            raise AttributeError

        return getattr(self.get_query_set(), attr, *args)