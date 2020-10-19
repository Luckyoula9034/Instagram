from django.db import models
from django.utils import timezone

# Create your models here.

class post(models.Model):
    author = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):   # def __str__(self):  returns a string representaion of the object"
       
        return self.caption