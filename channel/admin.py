from django.contrib import admin
from .models import Channel


class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
    list_filter = []
    search_fields = []


admin.site.register(Channel, ChannelAdmin)
