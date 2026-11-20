from django.db import models

class BrandingSettings(models.Model):
    company_name = models.CharField(max_length=200, default="Obrigado Finance")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, default="#1a73e8")
    secondary_color = models.CharField(max_length=7, default="#34a853")
    accent_color = models.CharField(max_length=7, default="#fbbc04")
    footer_text = models.TextField(default="© 2026 Obrigado Finance. All rights reserved.")

    class Meta:
        verbose_name_plural = "Branding Settings"

    def __str__(self):
        return self.company_name