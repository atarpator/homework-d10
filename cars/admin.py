from django.contrib import admin
from .models import Car

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("maker", "car_model", "year", "transmission", "color",)}