from django.contrib import admin
from .models import HelpRequest, Service


class AdminService(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'timestamp',)
    list_filter = ('name', 'timestamp')
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


class AdminHelpRequest(admin.ModelAdmin):
    list_display = ('for_service', 'timestamp', 'is_handled')
    list_filter = ('timestamp', )


admin.site.register(Service, AdminService)
admin.site.register(HelpRequest, AdminHelpRequest)
