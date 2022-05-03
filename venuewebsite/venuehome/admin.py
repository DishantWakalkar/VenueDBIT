from django.contrib import admin

# Register your models here.
from .models import Signin
from .models import SeminarHall
from .models import Mondini_Hall
from .models import BoscoHall
from .models import Ground

admin.site.register(Signin)
admin.site.register(SeminarHall)
admin.site.register(Mondini_Hall)
admin.site.register(BoscoHall)
admin.site.register(Ground)
