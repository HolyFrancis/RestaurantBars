from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, help_text=_("Name of the Category"))
    
    def __str__(self):
        return self.name
    

class Ingredients(models.Model):
    product = models.ForeignKey("Product", on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    quantity = models.FloatField()


class Recipe(models.Model):
    category = models.ForeignKey(
        "Category",
        on_delete=models.DO_NOTHING,
        related_name="recipes",
        related_query_name="recipe",
        null=True,
        blank=True)    
    ingredient = models.ForeignKey(
        "Ingredients",
        on_delete=models.DO_NOTHING,
        related_name="recipes",
        related_query_name="recipe",
        null=True,
        blank=True)
    name = models.CharField(max_length=50)
    price = models.FloatField()
    avaibility = models.BooleanField(default=True)
    image = models.ImageField(help_text=_("Recipe Image"), upload_to=None, height_field=None, width_field=None, max_length=None)
    description = models.CharField(max_length=100, null=True, blank=True)
    