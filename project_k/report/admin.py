from django.contrib import admin
from .models import CreateDGU, ReportDGU, Post, Location, ObjectKES


@admin.register(CreateDGU)
class CreateDGUAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'power', 'object_kes', )
    list_display_links = ('id', 'name')
    list_editable = ('object_kes',)
    list_per_page = 10
    search_fields = ['name']

@admin.register(ObjectKES)
class ObjectKESAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager')
    list_display_links = ('id', 'name')


admin.site.register(ReportDGU)
admin.site.register(Location)



