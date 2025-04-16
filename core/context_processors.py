from .models import SiteConfig
from services.models import Service

def site_config(request):
    config = SiteConfig.objects.first()
    return {'config': config}

def global_services(request):
    return {
        'global_featured_services': Service.objects.filter(is_active=True, is_featured=True),
        'all_active_services': Service.objects.filter(is_active=True)
    }