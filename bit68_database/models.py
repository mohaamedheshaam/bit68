from django.db import models

from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, blank=False)
    quantity = models.IntegerField(default=1)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=False)
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT)
    quantity = models.IntegerField(default=1)
