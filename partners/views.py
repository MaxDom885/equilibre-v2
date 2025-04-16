from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import Partner

class PartnerCarouselView(TemplateView):
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['partners'] = Partner.objects.filter(is_active=True).order_by('name')
        return context