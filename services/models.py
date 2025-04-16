from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    short_description = models.CharField(max_length=300, blank=True)
    full_description = models.TextField()
    image = models.ImageField(upload_to='services/')
    is_active = models.BooleanField(default=True)
    full_description_image = models.ImageField(upload_to='services/', blank=True)
    is_featured = models.BooleanField(
        default=False,
        help_text="Cocher pour afficher ce service en page d'accueil"
    )
    icon = models.CharField(
        max_length=50, 
        blank=True,
        help_text="Utilisez les classes Font Awesome. Ex: code → fa-code"
    )
    header_image = models.ImageField(upload_to='services/headers/', default='services/headers/default_header.jpg')
    strengths_image = models.ImageField(upload_to='services/strengths/', blank=True)
    strengths_text = models.TextField(
        "Atouts clés",
        max_length=500,
        blank=True,
        default="Notre expertise dans ce domaine inclut :\n- Solution personnalisée\n- Technologie de pointe\n- Support premium"
    )
    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Ordre d'affichage (plus petit chiffre en premier)"
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['display_order', 'name']