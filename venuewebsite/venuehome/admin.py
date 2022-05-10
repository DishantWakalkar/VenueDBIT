from django.contrib import admin

# Register your models here.
from .models import Signin, SeminarHall, Mondini_Hall, BoscoHall, Ground, SeminarBooking

admin.site.register(Signin)
admin.site.register(SeminarHall)
admin.site.register(Mondini_Hall)
admin.site.register(BoscoHall)
admin.site.register(Ground)
admin.site.register(SeminarBooking)