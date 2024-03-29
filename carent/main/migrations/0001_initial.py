# Generated by Django 2.2.4 on 2019-08-30 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_brand', models.CharField(max_length=200)),
                ('car_model', models.CharField(max_length=200)),
                ('car_color', models.CharField(max_length=200)),
                ('car_availability', models.BinaryField()),
                ('car_production_date', models.DateField()),
                ('car_price_per_day', models.IntegerField()),
            ],
        ),
    ]
