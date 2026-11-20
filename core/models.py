from django.db import models

class BrandingSettings(models.Model):
    company_name = models.CharField(max_length=200, default="Obrigado Finance")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, default="#0f172a") # Dark blue premium
    secondary_color = models.CharField(max_length=7, default="#10b981") # Emerald green
    accent_color = models.CharField(max_length=7, default="#f59e0b") # Gold/Yellow
    footer_text = models.TextField(default="© 2026 Obrigado Finance. All rights reserved.")

    # Home Page Controls
    hero_title = models.CharField(max_length=200, default="Welcome to Obrigado Finance")
    hero_subtitle = models.TextField(default="Your trusted partner for financial growth and stability.")
    hero_button_text = models.CharField(max_length=50, default="Get Started")
    
    # About Page Controls
    about_title = models.CharField(max_length=200, default="About Obrigado Finance")
    about_subtitle = models.TextField(default="Building financial bridges for a prosperous tomorrow.")
    about_mission = models.TextField(default="To empower individuals and businesses with innovative financial solutions...")
    about_vision = models.TextField(default="To be the global benchmark for financial excellence...")

    # Contact Page Controls
    contact_address = models.TextField(default="123 Financial District Avenue\nGlobal City, GC 10001")
    contact_email = models.CharField(max_length=100, default="info@obrigadofinance.com")
    contact_phone = models.CharField(max_length=50, default="+1 (800) 123-4567")

    class Meta:
        verbose_name_plural = "Branding & Site Settings"

    def __str__(self):
        return self.company_name

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="📈", help_text="Use an emoji like 📈, 🏦, 💳")

    def __str__(self):
        return self.title