from django.contrib import admin

from .models import  Register, BusDetail, Seat

admin.site.register(Register)
admin.site.register(Seat)
admin.site.register(BusDetail)