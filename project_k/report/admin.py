from django.contrib import admin
from .models import CreateDGU, ReportDGU, Post, Location, ObjectKES


admin.site.register(ReportDGU)
admin.site.register(CreateDGU)
admin.site.register(ObjectKES)
admin.site.register(Location)
admin.site.register(Post)


