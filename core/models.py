from django.db import models

class SiteBranding(models.Model):
    site_name = models.CharField(max_length=100, default='Obrigado Finance')
    logo = models.ImageField(upload_to='branding/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, default='#0A2540')
    secondary_color = models.CharField(max_length=7, default='#F5A623')
    accent_color = models.CharField(max_length=7, default='#FFFFFF')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.site_name