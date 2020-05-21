from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Form, PvmForm


admin.site.register(Form)
admin.site.register(PvmForm)
