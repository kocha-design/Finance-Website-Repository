from django.db import models

class BrandingSettings(models.Model):
    company_name = models.CharField(max_length=200, default="Obrigado Finance")
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    # Rangi (Brand Colors)
    primary_color = models.CharField("Rangi Kuu (Primary)", max_length=7, default="#1a73e8", help_text="Rangi ya vitufe vikuu na vichwa vya habari")
    secondary_color = models.CharField("Rangi ya Pili (Secondary)", max_length=7, default="#34a853", help_text="Rangi ya vitufe vingine na mapambo")
    accent_color = models.CharField("Rangi ya Mapambo (Accent)", max_length=7, default="#fbbc04", help_text="Rangi ya kuonyesha vitu muhimu kama bei au tahadhari")
    dark_color = models.CharField("Rangi Nyeusi (Dark)", max_length=7, default="#0f172a", help_text="Rangi ya Footer, Top Bar, na sehemu za giza")
    text_color = models.CharField("Rangi ya Maandishi (Text)", max_length=7, default="#475569", help_text="Rangi ya maandishi ya kawaida")
    bg_color = models.CharField("Rangi ya Nyuma (Background)", max_length=7, default="#f8fafc", help_text="Rangi nyepesi ya nyuma ya kurasa")
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
    
class HeroSlide(models.Model):
    title = models.CharField(max_length=200, help_text="Andika kichwa cha habari kwa picha hii")
    subtitle = models.TextField(help_text="Andika maelezo mafupi")
    image = models.ImageField(upload_to='hero_slides/', help_text="Pakia picha nzuri ya jengo au timu")
    order = models.IntegerField(default=0, help_text="Namba ndogo inaonekana kwanza")

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Hero Slides (Picha za Mwanzo)"

    def __str__(self):
        return self.title