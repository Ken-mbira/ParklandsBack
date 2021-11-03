from django.db import models

# Create your models here.
from account.models import Account

class Location(models.Model):
    """This defines the locations

    Args:
        models ([type]): [description]
    """

    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name


from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group

class DriverProfile(models.Model):
    """This defines the drivers prefferences

    Args:
        models ([type]): [description]
    """
    location = models.ForeignKey(Location, related_name='driver_location',on_delete=models.SET_NULL,null=True)
    owner = models.ForeignKey(Account, related_name="driver_profile",on_delete=models.CASCADE)

class Parking(models.Model):
    """This defines a set parking space

    Args:
        models ([type]): [description]
    """
    owner = models.ForeignKey(Account, related_name="parking",on_delete=models.CASCADE)
    location = models.ForeignKey(Location, related_name="parkings",on_delete=models.PROTECT)
    min_price = models.DecimalField(verbose_name="Minimun price to be charged",max_digits=4,decimal_places=2)
    name = models.CharField(max_length=50,unique=True)
    image = models.ImageField(upload_to="images/")
    rate = models.DecimalField(max_digits=4,decimal_places=2,verbose_name="Rate per hour")
    rows = models.IntegerField()
    columns = models.IntegerField()

    def __str__(self):
        return self.name


class Reservation(models.Model):
    """This defines the structure of a reservation

    Args:
        models ([type]): [description]
    """
    user = models.ForeignKey(Account, related_name="reservations",on_delete=models.PROTECT)
    parking = models.ForeignKey(Parking, related_name="reservations",on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.TimeField()
    end_time = models.TimeField()
    car_plate = models.CharField(max_length=3)
    car_plate_number = models.CharField(max_length=5)
    car_brand = models.CharField(max_length=100)
    driver = models.ForeignKey(Account,related_name="driving",on_delete=models.PROTECT)
    completed = models.BooleanField(default=False)
