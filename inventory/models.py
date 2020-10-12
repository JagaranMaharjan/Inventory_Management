from django.db import models


# Create your models here.
# in this model file, define the data structure of database

class Device(models.Model):  # name of the table
    type = models.CharField(max_length=100, blank=False)  # name of column
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item Sold'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default="SOLD")  # AVAILABLE, SOLD, RESTOCKING
    issues = models.CharField(max_length=100, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type:{0} Price:{1}'.format(self.type, self.price)


class Laptop(Device):
    pass


class Desktop(Device):
    pass


class Mobile(Device):
    pass

# migration reads the model file and generates the file that are necessary to write the postgresql in the backend
# python manage.py makemigrations
# python manage.py migrate
