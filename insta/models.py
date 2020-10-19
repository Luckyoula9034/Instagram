from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    author =models.Foreignkey('auth.user',on_delete=models.CASCADE)
    image = models.imageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.outerTimeField(default=timezone.now)