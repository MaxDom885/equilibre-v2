from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.translation import gettext_lazy as _



class Partner(models.Model):
    name = models.CharField(_("Nom"), max_length=200)
    slug = models.SlugField(_("Slug"), unique=True)
    logo = models.ImageField(upload_to='partners/')
    url = models.URLField(_("Site web"), blank=True, null=True)  # Nouveau champ
    is_active = models.BooleanField(_("Actif"), default=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Partenaire")
        verbose_name_plural = _("Partenaires")
        ordering = ['name']