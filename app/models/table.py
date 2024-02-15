from django.db import models

from django.utils.translation import gettext as _

class Place(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    
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
    
    def __str__(self):
        return self.name