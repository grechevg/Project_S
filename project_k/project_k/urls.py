from django.contrib import admin
from django.urls import path, include
from report.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name='index'),
    path("create_dgu/", create_dgu, name='create_dgu'),
    path("create_report/<int:id>/", create_report, name='create_report'),
    path("edit_dgu/<int:id>/", edit_dgu, name='edit_dgu'),
    path("delete_dgu/<int:id>/", delete_dgu, name='delete_dgu'),
    path('users/', include('users.urls', namespace="users")),
]

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Комплексные Энерго-Системы"