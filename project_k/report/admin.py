from django.contrib import admin
from .models import *


@admin.register(CreateDGU)
class CreateDGUAdmin(admin.ModelAdmin):
    list_display = ('name', 'dvs', 'location', 'title')
    list_display_links = ('name',)
    list_editable = ('location',)
    list_per_page = 10
    search_fields = ['name', 'power', ]

@admin.register(DVS)
class DVSAdmin(admin.ModelAdmin):
    list_display = ('engine_hours', 'model_dvs', 'sn', 'title')
    list_display_links = ('model_dvs',)
@admin.register(DVSmodel)
class DVSmodelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_dvs', 'power', 'cylinders', 'title')
    list_display_links = ('id', 'model_dvs',)
@admin.register(ObjectKES)
class ObjectKESAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager')
    list_display_links = ('id', 'name')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'object_kes')
    list_display_links = ('id', 'name')
    list_editable = ('object_kes',)
    list_per_page = 10
    search_fields = ['name']



admin.site.register(ReportDGU)




