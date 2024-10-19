from django.contrib import admin
from .models import *


@admin.register(CreateDGU)
class CreateDGUAdmin(admin.ModelAdmin):
    list_display = ('name', 'dvs', 'location',  'work', 'status', 'paralel', 'title',)
    list_display_links = ('name',)
    list_editable = ('location',)
    list_per_page = 10
    search_fields = ['name', 'power', ]

@admin.register(DVS)
class DVSAdmin(admin.ModelAdmin):
    list_display = ('id', 'engine_hours', 'model_dvs', 'sn', 'title')
    list_display_links = ('model_dvs',)
@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
@admin.register(DVSmodel)
class DVSmodelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_dvs', 'maker_dvs', 'power', 'volume', 'cylinders', 'title')
    list_display_links = ('id', 'model_dvs',)
@admin.register(ObjectKES)
class ObjectKESAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', )
    list_display_links = ('id', 'name')


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'object_kes')
    list_display_links = ('id', 'name')
    list_editable = ('object_kes',)
    list_per_page = 10
    search_fields = ['name']

@admin.register(ReportDGU)
class ReportDGUAdmin(admin.ModelAdmin):
    list_display = ('id', 'dgu', 'title', 'tc', 'time_create', 'time_update')
    list_display_links = ('id', 'dgu')
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    list_display_links = ('id', 'name')





