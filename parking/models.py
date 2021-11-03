from django.db import models

# Create your models here.
class Location(models.Model):
    """This defines the locations

    Args:
        models ([type]): [description]
    """

    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
