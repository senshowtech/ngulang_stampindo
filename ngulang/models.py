from django.db import models

# Create your models here.


class Food(models.Model):
    name = models.TextField()


class Ingredient(models.Model):
    food = models.ForeignKey(
        Food, on_delete=models.SET_NULL, related_name="ingredients", null=True)
    protein = models.FloatField()
    carb = models.FloatField()
    fat = models.FloatField()


class Author(models.Model):
    first_name = models.CharField(max_length=512)
    last_name = models.CharField(max_length=512)


class Book(models.Model):
    title = models.CharField(max_length=512)
    authors = models.ManyToManyField(Author)
