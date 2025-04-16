from django.urls import path
from .views import home_view
from .views import (
    ServiceListView,
    ServiceDetailView,
)

# Supprimez ou commentez l'URL de service_list
urlpatterns = [
    path('<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
    # path('', service_list, name='service_list')  # À supprimer
]