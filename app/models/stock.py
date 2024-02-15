from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    adress = models.CharField(max_length=100, null=True, blank=True)
    
    
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    
    
class ProductProvider(models.Model):
    provider = models.ForeignKey(
        "Provider",
        on_delete=models.DO_NOTHING,
        related_name="product_providers",
        related_query_name="product_provider",
        null=True,
        blank=True
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.DO_NOTHING,
        related_name="products_provider",
        related_query_name="product_provider",
        null=True,
        blank=True
    )
    expiration_date = models.DateField()
    is_active = models.BooleanField(default=True)
    quantity = models.FloatField(null=True, blank=True)