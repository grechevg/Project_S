from django.db import models

class DVSmodel(models.Model):
    model_dvs = models.CharField(blank=True, max_length=30, verbose_name='Модель ДВС')
    power = models.IntegerField(blank=True, verbose_name="Мощьность ДВС")
    cylinders = models.IntegerField(blank=True, verbose_name="Количество цилиндров")
    # volume = models.DecimalField(blank=True, decimal_places=2, max_digits=2,  verbose_name="Объем ДВС")
    title = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    def __str__(self):
        return f"{self.model_dvs}"
    class Meta:
        verbose_name = 'Модель ДВС'
        verbose_name_plural = 'Модель ДВС'

class DVS(models.Model):
    model_dvs = models.ForeignKey(DVSmodel, on_delete=models.SET_NULL, null=True, verbose_name="Модель ДВС")
    sn = models.CharField(max_length=50, blank=True, verbose_name='Серейный номер')
    engine_hours = models.IntegerField(blank=True, verbose_name="Моточасы")
    title = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    def __str__(self):
        return f"{self.model_dvs}"
    class Meta:
        verbose_name = 'ДВС'
        verbose_name_plural = 'ДВС'
class ObjectKES(models.Model):
    name = models.CharField(max_length=30)
    manager = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объект'


class Location(models.Model):
    name = models.CharField(max_length=30)
    object_kes = models.ForeignKey(ObjectKES, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Локация'
        verbose_name_plural = 'Локация'
    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участок'


class CreateDGU(models.Model):
    name = models.CharField(max_length=30, verbose_name="Номер Дгу")
    dvs = models.ForeignKey(DVS, on_delete=models.SET_NULL, null=True, verbose_name="Модель ДВС")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, verbose_name="Обьект")
    title = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'ДГУ'
        verbose_name_plural = 'ДГУ'


class ReportDGU(models.Model):
    dgu = models.ForeignKey(CreateDGU, on_delete=models.SET_NULL, null=True, verbose_name="Номер Дгу")
    title = models.CharField(max_length=30)
    tc = models.IntegerField()
    def __str__(self):
        return f"{self.dgu}"
    class Meta:
        verbose_name = 'Ежедневный отчет'
        verbose_name_plural = 'Ежедневный отчет'


class Post(models.Model):
    name = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, blank=True)
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пост'
