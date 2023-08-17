from django.db import models


class Register(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.CharField(max_length=800, null=True, blank=True)
    password = models.CharField(max_length=20)


class BusDetail(models.Model):
    bus_name = models.CharField(max_length=200)
    source = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    source_time = models.TimeField(blank=True, null=True)
    dest_time = models.TimeField(blank=True, null=True)

class Seat(models.Model):
    SEAT_CHOICE = (('Available', 'Available'),
            ('Not_Available', 'Not_Available'))
    bus = models.ForeignKey(BusDetail, on_delete=models.CASCADE)
    seat = models.IntegerField()
    price = models.IntegerField()
    booked = models.CharField(max_length=20, default='Available', choices=SEAT_CHOICE)
    timing=models.DateTimeField(blank=True, null=True)
    booked_by_user = models.CharField(max_length=200, blank=True)

