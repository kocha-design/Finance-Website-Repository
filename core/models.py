from django.db import models

class BrandingSettings(models.Model):
    company_name = models.CharField(max_length=200, default="Obrigado Finance")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    primary_color = models.CharField(max_length=7, default="#0f172a")
    secondary_color = models.CharField(max_length=7, default="#10b981")
    accent_color = models.CharField(max_length=7, default="#f59e0b")
    footer_text = models.TextField(default="© 2026 Obrigado Finance. All rights reserved.")

    # Home Page
    hero_title = models.CharField(max_length=200, default="Welcome to Obrigado Finance")
    hero_subtitle = models.TextField(default="Your trusted partner for financial growth and stability.")
    hero_button_text = models.CharField(max_length=50, default="Get Started")
    
    # About Page - Main Texts
    about_title = models.CharField(max_length=200, default="About Obrigado Finance")
    about_subtitle = models.TextField(default="Building financial bridges for a prosperous tomorrow.")
    about_mission = models.TextField(default="To empower individuals and businesses with innovative financial solutions...")
    about_vision = models.TextField(default="To be the global benchmark for financial excellence...")
    
    # About Page - Media & Stats
    about_image = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Upload an image for the About page")
    stat_1_value = models.CharField(max_length=50, default="10+")
    stat_1_label = models.CharField(max_length=50, default="Years of Experience")
    stat_2_value = models.CharField(max_length=50, default="500M+")
    stat_2_label = models.CharField(max_length=50, default="Assets Managed")
    stat_3_value = models.CharField(max_length=50, default="50k+")
    stat_3_label = models.CharField(max_length=50, default="Happy Clients")

    # Contact Page
    contact_address = models.TextField(default="123 Financial District Avenue\nGlobal City, GC 10001")
    contact_email = models.CharField(max_length=100, default="info@obrigadofinance.com")
    contact_phone = models.CharField(max_length=50, default="+1 (800) 123-4567")
    # Ongeza hii ndani ya class BrandingSettings
    whatsapp_number = models.CharField(max_length=20, default="255700000000", help_text="Without + sign. E.g., 255700000000")

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

class CoreValue(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50, default="🛡️", help_text="Use an emoji like 🛡️, 🤝, 🌟")

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='team/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    company = models.CharField(max_length=100, blank=True, null=True)
    quote = models.TextField()
    rating = models.IntegerField(default=5, help_text="Rating from 1 to 5")

    def __str__(self):
        return self.client_name
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")

    class Meta:
        ordering = ['order']
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
    
    # Ongeza hizi chini ya models zilizopo:

class Partner(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='partners/', blank=True, null=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    excerpt = models.TextField(help_text="Short summary shown on the list page")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email