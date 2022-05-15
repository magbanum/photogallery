from django.db import models
from cloudinary.models import CloudinaryField

class Photo(models.Model):
    image = CloudinaryField('image')
    alt = models.CharField(max_length=200)
    uploaded = models.DateTimeField(auto_now_add=True)