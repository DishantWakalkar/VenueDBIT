from django.contrib import admin

# Register your models here.
from .models import Signin, Venue, Booking

admin.site.register(Signin)
admin.site.register(Venue)
admin.site.register(Booking)