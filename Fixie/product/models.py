from django.db import models

class products(models.Model):
    name = models.CharField(max_length= 35)
    description = models.TextField(null=True, max_length= 255, blank= True)
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, upload_to='images/')
    
    def _str_(self):
        return self.name
# Create your models here.
