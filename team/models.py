# team/models.py  
from django.db import models  

class Member(models.Model):  
    name = models.CharField(max_length=100)  
    role = models.CharField(max_length=100)   
    photo = models.ImageField(upload_to="team/")  
    linkedin_url = models.URLField(blank=True) 
    facebook_url = models.URLField(blank=True) 
    twitter_url = models.URLField(blank=True) 
    is_active = models.BooleanField(default=True)  # Pour filtrer les anciens membres  

    def __str__(self):  
        return self.name  

    class Meta:  
        ordering = ["name"]  # Tri alphabétique  