from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# Create your models here.
class Ingredients(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Ingredient: {self.name}"


class Food(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(
        Ingredients, blank=False, related_name="ingredients"
    )
    recipeUrl = models.TextField(null=True)

    def __str__(self):
        return f"Food: {self.name} | Country: {self.country}"
