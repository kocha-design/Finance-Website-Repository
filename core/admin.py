from django.contrib import admin
from .models import BrandingSettings, Service, CoreValue, TeamMember, Testimonial, FAQ

@admin.register(BrandingSettings)
class BrandingSettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Brand Identity', {'fields': ('company_name', 'logo', 'primary_color', 'secondary_color', 'accent_color', 'footer_text')}),
        ('Home Page', {'fields': ('hero_title', 'hero_subtitle', 'hero_button_text')}),
        ('About Page - Texts', {'fields': ('about_title', 'about_subtitle', 'about_mission', 'about_vision')}),
        ('About Page - Media', {'fields': ('about_image',)}),
        ('About Page - Stats', {'fields': ('stat_1_value', 'stat_1_label', 'stat_2_value', 'stat_2_label', 'stat_3_value', 'stat_3_label')}),
        ('Contact Info', {'fields': ('contact_address', 'contact_email', 'contact_phone')}),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')

@admin.register(CoreValue)
class CoreValueAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'company', 'rating')
    
@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)