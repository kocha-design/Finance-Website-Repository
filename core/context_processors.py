 
from .models import SiteBranding

def branding(request):
    try:
        brand = SiteBranding.objects.filter(is_active=True).first()
    except Exception:
        brand = None
    return {
        'brand': brand,
        'site_name': brand.site_name if brand else 'Obrigado Finance',
        'primary_color': brand.primary_color if brand else '#0A2540',
        'secondary_color': brand.secondary_color if brand else '#F5A623',
        'accent_color': brand.accent_color if brand else '#FFFFFF',
        'logo_url': brand.logo.url if brand and brand.logo else '',
    }