from django.contrib import admin
from ctdm.models import Person, NewData


@admin.register(Person)
class AdminPerson(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')


@admin.register(NewData)
class AdminNewData(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
