# Generated by Django 5.0.7 on 2024-07-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GeoLocCouriers', '0007_remove_couriers_avatar_remove_couriers_experience_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listorderid',
            name='order_id',
            field=models.CharField(default='', max_length=16),
        ),
    ]