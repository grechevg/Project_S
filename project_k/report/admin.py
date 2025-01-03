from django.contrib import admin
from .models import *


@admin.register(CreateDGU)
class CreateDGUAdmin(admin.ModelAdmin):
    list_display = ('name', 'long_name', 'post_name', 'dvs', 'location', 'work', 'status', 'paralel', 'title',)
    list_display_links = ('name',)
    list_editable = ('location',)
    list_per_page = 30
    search_fields = ['name', 'power', ]


@admin.register(DVS)
class DVSAdmin(admin.ModelAdmin):
    list_display = ('id', 'sn', 'engine_hours', 'model_dvs', 'title')
    list_display_links = ('sn', 'model_dvs',)

@admin.register(Alternator)
class AlternatorAdmin(admin.ModelAdmin):
    list_display = ('id','sn', 'hours_alternator', 'model_alternator',  'title')
    list_display_links = ('sn', 'model_alternator',)

@admin.register(Maker)
class MakerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)

@admin.register(DVSmodel)
class DVSmodelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_dvs', 'maker_dvs', 'power', 'volume', 'cylinders', 'title')
    list_display_links = ('id', 'model_dvs',)

@admin.register(AlternatorModel)
class AlternatorModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'model_alternator', 'maker_alternator', 'power_res_kva',
                    'power_res_kvt', 'power_rab_kva', 'power_rab_kvt', 'diod_most', 'diodes_1', 'diodes_2',
                    'varistor', 'resistor', 'title')
    list_display_links = ('id', 'model_alternator',)

@admin.register(ObjectKES)
class ObjectKESAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', )
    list_display_links = ('id', 'name')

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'object_kes', 'operator')
    list_display_links = ('id', 'name')
    list_editable = ('object_kes','operator')
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

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title',)
    list_display_links = ('name',)

@admin.register(TKModel)
class TKModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title',)
    list_display_links = ('id', 'name',)

@admin.register(EmkostModel)
class EmkostModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title',)
    list_display_links = ('id','name',)

@admin.register(Emkost)
class EmkostAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'meter', 'post_name',)
    list_display_links = ('id', 'number',)

@admin.register(TK)
class TKAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', )
    list_display_links = ('id', 'number',)

@admin.register(Pump_meter)
class Pump_meterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'meter')
    list_display_links = ('id', 'name',)

@admin.register(Mercury)
class MercuryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'meter')
    list_display_links = ('id', 'name',)