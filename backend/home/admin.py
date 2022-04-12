from django.contrib import admin
from .models import Hometest, Name, Testing

admin.site.register(Name)
admin.site.register(Hometest)
admin.site.register(Testing)

# Register your models here.
