from django.db import models

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
    house_image = models.ImageField(upload_to='images/')
    house_image2 = models.ImageField(upload_to='images/')
    house_image3 = models.ImageField(upload_to='images/')
    house_image4 = models.ImageField(upload_to='images/')
    house_image5 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.house_description