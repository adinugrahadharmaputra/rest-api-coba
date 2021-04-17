from django.db import models

# Create your models here.
class Destinasi(models.Model):
    name = models.CharField(max_lenght=50)
    description = models.TextField()
    image_url = models.TextField()
    address = models.TextField()
    site = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__ (self):
        return self.name