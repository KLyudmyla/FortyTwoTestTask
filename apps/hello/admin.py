from django.contrib import admin
from apps.hello.models import Person
from django.db import models

class PersonAdmin(admin.ModelAdmin):
    list_display = [ "name" , "surname"]

admin.site.register(Person, PersonAdmin)

#admin.site.register(StudentModelForm)
# Register your models here.
