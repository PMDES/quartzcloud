from django.contrib import admin
from .models import DM


# Register the DM model with the admin interface
@admin.register(DM)
class DMAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_1', 'user_2')
    list_filter = ('user_1', 'user_2')
    search_fields = ('user_1__username', 'user_2__username')
