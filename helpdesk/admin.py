from django.contrib import admin
from .models import Service


class AdminService(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'timestamp',)
    list_filter = ('name', 'timestamp')
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


admin.site.register(Service, AdminService)