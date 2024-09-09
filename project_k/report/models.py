from django.db import models


class ObjectKES(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=250, blank=True)


class CreateDGU(models.Model):
    name = models.CharField(max_length=30)
    power = models.IntegerField()
    object_kes = models.ForeignKey(ObjectKES, on_delete=models.SET_NULL, null=True)


class ReportDGU(models.Model):
    dgu = models.ForeignKey(CreateDGU, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30)
    tc = models.IntegerField()



class Location(models.Model):
    name = models.ForeignKey(ObjectKES, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=250, blank=True)


class Post(models.Model):
    name = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, blank=True)