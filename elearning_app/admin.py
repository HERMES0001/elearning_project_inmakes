
# Register your models here.
from django.contrib import admin


from .models import Place
from .models import team

admin.site.register(Place)

admin.site.register(team)