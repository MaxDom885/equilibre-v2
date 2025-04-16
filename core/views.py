from django.shortcuts import render
from django.views.generic import TemplateView  
from team.models import Member
from services.models import Service
from partners.models import Partner


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Services
        context['services'] = Service.objects.filter(
            is_active=True
        ).order_by('display_order')
        
        # Partenaires
        partners = Partner.objects.filter(is_active=True).order_by('name')
        context['partners'] = partners
        context['partners_count'] = partners.count()
        
        return context


class AboutView(TemplateView):
    template_name = "core/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = Member.objects.filter(
            is_active=True
        )
        return context


def contact_view(request):
    return render(request, 'contact.html')