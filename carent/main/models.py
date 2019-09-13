from django.db import migrations, models
from datetime import datetime
from datetime import timedelta
from django.contrib.auth.models import User

# Create your models here.
class Car(models.Model):
    car_brand = models.CharField(max_length=200)
    car_model = models.CharField(max_length=200)
    car_color = models.CharField(max_length=200)
    car_availability = models.BooleanField()
    car_production_date = models.DateField()
    car_price_per_day = models.IntegerField()
    car_pic = models.ImageField(default="default.png", blank=True)

    def __str__(self):
        return self.car_brand

class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_user = models.ForeignKey('auth.User', default=1, on_delete=models.SET_DEFAULT)
    rental_car = models.ForeignKey(Car, default=1, on_delete=models.SET_DEFAULT)
    rental_start_date = models.DateField("rental_date", default = datetime.now())
    rental_due_date = models.DateField("rental_date", default = datetime.now() + timedelta(days=1))

    def __str_(self):
        return self.rental_id