from django.db import models  

class SiteConfig(models.Model):  
    logo = models.ImageField(upload_to="config/")  
    call_phone = models.CharField(max_length=20)  
    whatsapp_phone = models.CharField(max_length= 20)
    email= models.EmailField()
    address= models.CharField(max_length=200)
    horaires= models.CharField(max_length=200)
    social_facebook= models.CharField(max_length=200, blank= True, null= True)
    social_linkedin= models.CharField(max_length= 200, blank= True, null= True)
    social_instagram= models.CharField(max_length= 200, blank= True, null= True)
    social_youtube= models.CharField(max_length= 200, blank= True, null= True)
    social_twitter= models.CharField(max_length= 200, blank= True, null= True)

    class Meta:  
        verbose_name = "Configuration du site"  