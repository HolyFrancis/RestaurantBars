from django.db import models

from django.utils.translation import gettext as _

class Place(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    short_description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    

class Table(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    capacity = models.IntegerField()
    place = models.OneToOneField(
        "Place",
        on_delete=models.DO_NOTHING,
        null=True,
        blank=True,
        related_name="tables",
        related_query_name="table",
        verbose_name=_("Place")
    )
    image = models.ImageField(help_text=_("Table Image"), upload_to=None, height_field=None, width_field=None, max_length=None)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name