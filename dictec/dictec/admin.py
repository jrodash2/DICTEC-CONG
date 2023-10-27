
from django.contrib import admin
from .models import Dictamenfinal

class Dicadminfinal(admin.ModelAdmin):
    readonly_fields =("Creacion", )

# Register your models here.
admin.site.register(Dictamenfinal, Dicadminfinal)
