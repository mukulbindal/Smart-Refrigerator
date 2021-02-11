from django.contrib import admin

# Register your models here.
from .models import Refrigerator,User


admin.site.register(User)
admin.site.register(Refrigerator)