from django.db import models


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
    power = models.IntegerField(verbose_name="Мощьность КВт")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, verbose_name="Обьект")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'ДГУ'
        verbose_name_plural = 'ДГУ'


class ReportDGU(models.Model):
    dgu = models.ForeignKey(CreateDGU, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=30)
    tc = models.IntegerField()


class Post(models.Model):
    name = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, blank=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пост'