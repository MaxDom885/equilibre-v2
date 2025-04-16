# core/urls.py
from django.urls import path, include
from .views import HomeView, AboutView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path("notre-agence/", AboutView.as_view(), name="about"),  # Un seul point d'entrée
    path("services/", include("services.urls")),
    path("contact/", include("contact.urls")),
    path("partenaires/", include("partners.urls")),
]