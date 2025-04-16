from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm
from django_ratelimit.decorators import ratelimit
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views import View
from django.contrib import messages

@method_decorator(ratelimit(key='ip', rate='5/m', block=True), name='dispatch')
class ContactView(FormView):
    template_name = "contact/form.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact_success")

    def get_initial(self):
        # Pré-remplir le formulaire avec les données de la session
        initial = super().get_initial()
        contact_data = self.request.session.get("contact_data")  # Ne pas supprimer les données ici
        if contact_data:
            initial.update(contact_data)
        return initial

    def form_valid(self, form):
        form.save()  # Sauvegarde automatique grâce au ModelForm
        return super().form_valid(form)
    
class ContactSuccessView(TemplateView):
    template_name = "contact/success.html"

class HomeContactView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        if not name or not email or not message:
            messages.error(request, "Tous les champs sont obligatoires.")
            return redirect("home")

        # Stocker les données dans la session
        request.session["contact_data"] = {
            "name": name,
            "email": email,
            "message": message,
        }

        return redirect("contact_form")