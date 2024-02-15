from django.db import models


class Order(models.Model):
    table = models.ForeignKey(
        "Table",
        on_delete=models.DO_NOTHING,
        related_name="orders",
        related_query_name="order",
        null=False,
        blank=False
    )
    waiter = models.ForeignKey(
        "MyUser",
        on_delete=models.DO_NOTHING,
        related_name="waiter_orders"
    )
    to_pay = models.FloatField()
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    ready = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.table
    
    
class Cart(models.Model):
    recipe = models.ForeignKey(
        "Recipe",
        on_delete=models.DO_NOTHING,
        related_name="carts"
    )
    ready = models.BooleanField(default=False)
    quantity = models.PositiveBigIntegerField(default=0)
    total = models.DecimalField(max_digits=30, decimal_places=2)
    

class Payment(models.Model):
    order = models.ForeignKey(
        "Order",
        on_delete=models.DO_NOTHING,
        related_name="payments_order",
        related_query_name="payment_order",
        null=False,
        blank=False
    )
    total_amount = models.DecimalField(max_digits=30, decimal_places=2)
    
    def __str__(self):
        return f"{self.order} --- {self.total_amount}"