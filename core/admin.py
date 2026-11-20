from django.contrib import admin
from .models import BrandingSettings, Service

@admin.register(BrandingSettings)
class BrandingSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Brand Identity', {'fields': ('company_name', 'logo', 'primary_color', 'secondary_color', 'accent_color', 'footer_text')}),
        ('Home Page Content', {'fields': ('hero_title', 'hero_subtitle', 'hero_button_text')}),
        ('About Page Content', {'fields': ('about_title', 'about_subtitle', 'about_mission', 'about_vision')}),
        ('Contact Info', {'fields': ('contact_address', 'contact_email', 'contact_phone')}),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')