from .models import BrandingSettings

def branding(request):
    settings_obj = BrandingSettings.objects.first()
    if not settings_obj:
        settings_obj = BrandingSettings.objects.create()
    return {'branding': settings_obj}