from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Service

def home_view(request):
    # Récupère les services marqués comme featured, actifs et triés
    featured_services = Service.objects.filter(
        is_active=True,
        is_featured=True
    )

    context = {
        'services': featured_services, 
    }
    return render(request, 'home.html', context)

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'
    paginate_by = 6

    def get_queryset(self):
        return Service.objects.filter(is_active=True).order_by('display_order', 'name')
    
class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Service.objects.filter(is_active=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_services'] = Service.objects.filter(is_active=True).exclude(id=self.object.id)
        return context