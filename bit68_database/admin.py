from django.contrib import admin
from . import models
from django.db.models.query import QuerySet


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
