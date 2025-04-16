from django.views.generic import ListView  
from .models import Member  

class TeamListView(ListView):  # Pas un TemplateView car besoin de données dynamiques  
    model = Member  
    template_name = "core/about.html"  
    context_object_name = "members"  