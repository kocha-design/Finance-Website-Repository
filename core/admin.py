from django.contrib import admin
from .models import BrandingSettings


@admin.register(BrandingSettings)
class BrandingSettingsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'primary_color', 'secondary_color', 'accent_color')
    fieldsets = (
        ('Company Identity', {
            'fields': ('company_name', 'logo')
        }),
        ('Brand Colors', {
            'fields': ('primary_color', 'secondary_color', 'accent_color'),
            'description': 'Use hex codes like #1a73e8, #34a853, #fbbc04'
        }),
        ('Footer', {
            'fields': ('footer_text',)
        }),
    )