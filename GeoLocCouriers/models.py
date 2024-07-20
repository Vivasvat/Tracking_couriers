from django.db import models

class Couriers(models.Model):
    name = models.CharField(
        max_length = 50,
        blank = True,
        null = True,
    )

    Phone = models.CharField(
        max_length = 16,
        blank = True,
        null = True,
    )

    Experience = models.SmallIntegerField(
        default=0,
    )

    Rating = models.SmallIntegerField(
        default=0,
    )

    Avatar = models.ImageField(
        upload_to="media/", 
        default="media/defolt_avatar.png", 
        blank=True, 
        null=True, 
        verbose_name='Аватар'
        )
    
    GeoLocCouriers = models.
    
    def __str__(self):
        return self.name
# Create your models here.
