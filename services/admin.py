from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'is_featured', 'display_order')
    list_filter = ('is_active', 'is_featured')
    list_editable = ('is_active', 'is_featured', 'display_order')  # Permet d'éditer directement depuis la liste
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'short_description')  # Ajout de la recherche
    fieldsets = (
        ('Informations de base', {
            'fields': ('name', 'slug', 'is_active', 'is_featured', 'display_order')
        }),
        ('Contenu principal', {
            'fields': ('short_description', 'full_description', 'icon', 'strengths_text'),
            'description': "Contenu textuel du service"
        }),
        ('Gestion des images', {
            'fields': ('image', 'header_image', 'strengths_image', 'full_description_image'),
            'classes': ('collapse',)
        }),
    )
    
    # Optionnel : configuration des actions rapides
    actions = ['make_featured', 'remove_featured']
    
    def make_featured(self, request, queryset):
        queryset.update(is_featured=True)
    make_featured.short_description = "Mettre en avant les services sélectionnés"
    
    def remove_featured(self, request, queryset):
        queryset.update(is_featured=False)
    remove_featured.short_description = "Retirer de la sélection les services"