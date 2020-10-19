from django.db import models

# Create your models here.

class post(models.Model):
    author =models.Foreignkey('auth.user',on_delete=models.CASCADE)
    image = models.imageField(blank=True, null=True)