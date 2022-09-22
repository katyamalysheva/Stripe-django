from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_stripe = models.CharField(max_length=100, default="")

    def __str__(self) -> str:
        return self.name
