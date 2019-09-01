from django.contrib import admin
from .models import Car

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Car description", {"fields": ["car_brand", "car_model", "car_production_date", "car_color"]}),
        ("Car rental", {"fields": ["car_price_per_day", "car_availability"]})
    ]


admin.site.register(Car, CarAdmin)