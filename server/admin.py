from django.contrib import admin
from .models import Server


class ServerAdmin(admin.ModelAdmin):
    list_display = ['name', 'owner']
    list_filter = ['owner']
    search_fields = ['name', 'owner__username']


admin.site.register(Server, ServerAdmin)
