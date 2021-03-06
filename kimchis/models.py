from django.db import models
from cloudinary.models import CloudinaryField


class MainIngredient(models.Model):
    title = models.CharField(blank=False, max_length=255)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(blank=False, max_length=50)

    def __str__(self):
        return self.title


class Kimchi(models.Model):
    title = models.CharField(blank=False, max_length=255)
    desc = models.TextField(blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, blank=False)
    manufactured_date = models.DateField(blank=False)
    expiry_date = models.DateField(blank=False)
    main_ingredient = models.ForeignKey(
        MainIngredient, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    cover = CloudinaryField()

    def __str__(self):
        return self.title
