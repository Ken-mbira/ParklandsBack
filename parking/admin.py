from django.contrib import admin

# Register your models here.
from parking.models import *

admin.site.register(Location)
admin.site.register(DriverProfile)
admin.site.register(Parking)
admin.site.register(Reservation)
