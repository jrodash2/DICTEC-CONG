
from django.contrib import admin
from .models import Dictamen

class Dicadmin(admin.ModelAdmin):
    readonly_fields =("Creacion", )

# Register your models here.
admin.site.register(Dictamen, Dicadmin)
