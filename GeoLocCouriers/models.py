from django.db import models

class Couriers(models.Model):
    courier_id = models.IntegerField(
        null=True, blank=True
    )

    surname = models.CharField(
        max_length = 50,
        null=True, blank=True
    )

    name = models.CharField(
        max_length = 50,
        null=True, blank=True
    )

    middlename = models.CharField(
        max_length = 50,
        null=True, blank=True
    )

    phone = models.CharField(
        max_length = 16,
        null=True, blank=True
    )

    photo_url = models.ImageField(
        upload_to="media/",
        blank=True, null=True,
    )
    
    latitude = models.CharField(
        max_length = 16,
        blank = True, null = True,
    )
    longitude = models.CharField(
        max_length = 16,
        blank = True, null = True,
    )

    def __str__(self):
        return self.name
    

class ListOrderId(models.Model):
    order_id = models.CharField(
        max_length = 16,
        default='',
    )

    def __str__(self):
        return self.order_id
# Create your models here.
