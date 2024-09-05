from django.db import models

class CreateDGU(models.Model):
    name = models.CharField(max_length=30)
    power = models.IntegerField()



class ReportDGU(models.Model):
    dgu = models.ForeignKey(CreateDGU, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    tc = models.IntegerField()
