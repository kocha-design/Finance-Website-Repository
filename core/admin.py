from django.contrib import admin
from django.db import models
from django import forms
from .models import BrandingSettings, Service, CoreValue, TeamMember, Testimonial, FAQ, Partner, BlogPost, Subscriber

# 1. Tengeneza Widget Maalum kwa ajili ya Rangi Pekee
class ColorPickerWidget(forms.TextInput):
    input_type = 'color'

# 2. Tengeneza Fomu (Form) Maalum
class BrandingSettingsForm(forms.ModelForm):
    class Meta:
        model = BrandingSettings
        fields = '__all__'
        widgets = {
            'primary_color': ColorPickerWidget(),
            'secondary_color': ColorPickerWidget(),
            'accent_color': ColorPickerWidget(),
            'dark_color': ColorPickerWidget(),
            'text_color': ColorPickerWidget(),
            'bg_color': ColorPickerWidget(),
        }

# 3. Tumia Fomu hiyo kwenye Admin
class BrandingSettingsAdmin(admin.ModelAdmin):
    form = BrandingSettingsForm
    
    fieldsets = (
        ('Brand Identity', {
            'fields': ('company_name', 'logo', 'footer_text', 'whatsapp_number'),
        }),
        ('🎨 Brand Colors (Chagua Rangi Zako)', {
            'fields': ('primary_color', 'secondary_color', 'accent_color', 'dark_color', 'text_color', 'bg_color'),
            'description': 'Bonyeza kisanduku cha rangi kuibadilisha.'
        }),
        ('Home Page', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_button_text'),
        }),
        ('About Page - Texts', {
            'fields': ('about_title', 'about_subtitle', 'about_mission', 'about_vision'),
        }),
        ('About Page - Media', {
            'fields': ('about_image',),
        }),
        ('About Page - Stats', {
            'fields': ('stat_1_value', 'stat_1_label', 'stat_2_value', 'stat_2_label', 'stat_3_value', 'stat_3_label'),
        }),
        ('Contact Info', {
            'fields': ('contact_address', 'contact_email', 'contact_phone'),
        }),
    )

    class Media:
        js = ('admin/js/color_picker.js',)

# Sajili models zingine
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

@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')

admin.site.register(BrandingSettings, BrandingSettingsAdmin)