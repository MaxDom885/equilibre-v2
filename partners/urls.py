from django.urls import path
from .views import PartnerCarouselView

urlpatterns = [
    path('', PartnerCarouselView.as_view(), name='home'),
]