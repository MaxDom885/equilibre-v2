from captcha.fields import CaptchaField  # Correction ici
from .models import ContactRequest
from django import forms


class ContactForm(forms.ModelForm):
    captcha = CaptchaField()  # Utilisation de CaptchaField

    def clean_website(self):
        website = self.cleaned_data.get("website")
        if website:
            raise forms.ValidationError("Bot détecté. Formulaire refusé.")
        return website

    class Meta:
        model = ContactRequest
        fields = ["name", "email", "message", "captcha"]
        widgets = {
            "message": forms.Textarea(attrs={"rows": 5}),
        }