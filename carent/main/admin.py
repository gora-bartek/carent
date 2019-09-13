from django.contrib import admin
from .models import Car
from .models import Rental

class CarAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Car description", {"fields": ["car_brand", "car_model", "car_production_date", "car_color"]}),
        ("Car rental", {"fields": ["car_price_per_day", "car_availability"]}),
        ("Car photo", {"fields": ["car_pic"]})
    ]

admin.site.register(Car, CarAdmin)
admin.site.register(Rental)