from django.contrib import admin
from django.urls import path
from report import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path("create_dgu/", views.create_dgu, name='create_dgu'),
    path("create_report/<int:id>/", views.create_report, name='create_report'),
    path("edit_dgu/<int:id>/", views.edit_dgu, name='edit_dgu'),
    path("delete_dgu/<int:id>/", views.delete_dgu, name='delete_dgu'),
]

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "Комплексные Энерго-Системы"