from django.db import models

# Create your models here.
class Car(models.Model):
    car_brand = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    car_color = models.CharField(max_length=200)
    car_availability = models.BooleanField()
    car_production_date = models.DateField()
    car_price_per_day = models.IntegerField()

    def __str__(self):
        return self.car_brand