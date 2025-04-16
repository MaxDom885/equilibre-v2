# contact/urls.py
from django.urls import path
from .views import HomeContactView,ContactView, ContactSuccessView 

urlpatterns = [
    path("", ContactView.as_view(), name="contact_form"),
    path('success/', ContactSuccessView.as_view(), name='contact_success'),
    path("home-contact/", HomeContactView.as_view(), name="home_contact"),
]