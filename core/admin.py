from django.contrib import admin
from .models import SiteBranding

@admin.register(SiteBranding)
class SiteBrandingAdmin(admin.ModelAdmin):
    list_display = ('site_name', 'primary_color', 'is_active')