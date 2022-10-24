from django.db import models
from django.core.validators import *

SIZE_CHOICES = {
    ("Tiny", "Tiny"),
    ("Small", "Small"),
    ("Medium", "Medium"),
    ("Large", "Large"),
}
# Create your models here.
class Breed(models.Model):
    name = models.CharField(max_length=50, blank=False)
    size = models.CharField(max_length=6, choices=SIZE_CHOICES, default="")
    friendliness = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingAmount = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseNeeds = models.IntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=1000, blank=False)
    age = models.IntegerField(default=1, blank=False)
    breed = models.ForeignKey(Breed, null=True, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=False)
    gender = models.CharField(max_length=50, blank=False) 
    favoriteFood = models.CharField(max_length=100, blank=False)
    favoriteToy = models.CharField( max_length=100, blank=False)

    def __str__(self):
        return self.name
    
