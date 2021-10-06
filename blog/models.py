from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Listings(models.Model):
    house_description = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, default="")
    address = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    house_feature = models.CharField(max_length=200)
    house_feature2 = models.CharField(max_length=200)
    house_feature3 = models.CharField(max_length=200)
    house_feature4 = models.CharField(max_length=200)
    house_feature5 = models.CharField(max_length=200)
    house_image =  CloudinaryField('image', null=True, blank=True)
    house_image2 =  CloudinaryField('image', null=True, blank=True)
    house_image3 =  CloudinaryField('image', null=True, blank=True)
    house_image4 =  CloudinaryField('image', null=True, blank=True)
    house_image5 =  CloudinaryField('image', null=True, blank=True)

    def __str__(self):
        return self.house_description