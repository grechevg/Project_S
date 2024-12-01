from datetime import datetime

from django.contrib.auth import get_user_model
from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статус'

class Maker(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производитель'

class AlternatorModel(models.Model):
    model_alternator = models.CharField(blank=True, max_length=30, verbose_name='Модель Генератора')
    maker_alternator = models.ForeignKey(Maker, on_delete=models.SET_NULL, null=True, verbose_name="Производитель")
    power_res_kva = models.IntegerField(blank=True, verbose_name="Мощьность Резервная кВа")
    power_res_kvt = models.IntegerField(blank=True, verbose_name="Мощьность Резервная кВт")
    power_rab_kva = models.IntegerField(blank=True, verbose_name="Мощьность Основная кВа")
    power_rab_kvt = models.IntegerField(blank=True, verbose_name="Мощьность Основная кВт")
    weight = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name='Вес кг')
    diod_most = models.CharField(blank=True, max_length=30, verbose_name='Диодный мост')
    diodes_1 = models.CharField(blank=True, max_length=30, verbose_name='Диод 1')
    diodes_2 = models.CharField(blank=True, max_length=30, verbose_name='Диод 2')
    varistor = models.CharField(blank=True, max_length=30, verbose_name='Варистор')
    resistor = models.CharField(blank=True, max_length=30, verbose_name='Резистор')
    title = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    def __str__(self):
        return f"{self.model_alternator, self.maker_alternator}"
    class Meta:
        verbose_name = 'Модель Генератора'
        verbose_name_plural = 'Модель Генератора'

class DVSmodel(models.Model):
    model_dvs = models.CharField(blank=True, max_length=30, verbose_name='Модель ДВС')
    maker_dvs = models.ForeignKey(Maker, on_delete=models.SET_NULL, null=True, verbose_name="Производитель")
    power = models.IntegerField(blank=True, verbose_name="Мощьность ДВС")
    cylinders = models.IntegerField(blank=True, verbose_name="Количество цилиндров")
    volume = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=2,  verbose_name="Объем ДВС")
    weight = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name='Вес кг')
    title = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    def __str__(self):
        return f"{self.model_dvs, self.maker_dvs}"
    class Meta:
        verbose_name = 'Модель ДВС'
        verbose_name_plural = 'Модель ДВС'

class DVS(models.Model):
    model_dvs = models.ForeignKey(DVSmodel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="ДВС")
    sn = models.CharField(max_length=70, blank=True, verbose_name='Серейный номер')
    engine_hours = models.IntegerField(blank=True, verbose_name="Моточасы")
    title = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    def __str__(self):
        return f"{self.sn, self.model_dvs,}"
    class Meta:
        verbose_name = 'ДВС'
        verbose_name_plural = 'ДВС'

class Alternator(models.Model):
    model_alternator = models.ForeignKey(AlternatorModel, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Генератор")
    sn = models.CharField(max_length=70, blank=True, verbose_name='Серейный номер')
    hours_alternator = models.IntegerField(blank=True, verbose_name="Моточасы")
    title = models.CharField(max_length=250, blank=True, verbose_name='Описание')
    def __str__(self):
        return f"{self.sn, self.model_alternator,}"
    class Meta:
        verbose_name = 'Генератор'
        verbose_name_plural = 'Герератор'

class ObjectKES(models.Model):
    name = models.CharField(max_length=30)
    manager = models.ForeignKey(get_user_model(),
                               on_delete=models.SET_NULL,
                               related_name='manager_obj',
                               null=True, default=None)
    public = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объект'


class Location(models.Model):
    name = models.CharField(max_length=30)
    object_kes = models.ForeignKey(ObjectKES, on_delete=models.SET_NULL, null=True)
    operator = models.ForeignKey(get_user_model(),
                               on_delete=models.SET_NULL,
                               related_name='operator_area',
                               null=True, default=None)
    address = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return f"{self.name}"
    class Meta:
        verbose_name = 'Участок'
        verbose_name_plural = 'Участок'

class Post(models.Model):
    name = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250, blank=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пост'

class CreateDGU(models.Model):
    name = models.CharField(max_length=30, verbose_name="Номер Дгу")
    maker_dvs = models.ForeignKey(Maker, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Производитель")
    long_name = models.CharField(max_length=30, null=True, blank=True, verbose_name="Название Дгу")
    post_name = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Название поста")
    dvs = models.ForeignKey(DVS, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="ДВС")
    alternator = models.ForeignKey(Alternator, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Генератор")
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True,blank=True, verbose_name="Обьект")
    work = models.BooleanField(default=False, verbose_name='в Работе')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, verbose_name="Состояние")
    paralel = models.BooleanField(default=False, verbose_name='Паралель')
    koguch = models.BooleanField(default=False, verbose_name='Кожухное Исполнение')
    weight = models.PositiveIntegerField(null=True, blank=True, default=0, verbose_name='Вес кг')
    lsh = models.CharField(max_length=100, null=True, blank=True, verbose_name="Длинна * Ширина * Высота ")
    title = models.CharField(max_length=250, blank=True, verbose_name='Описание  проблем')
    # ТО
    data_to = models.DateField(blank=True, null=True,  verbose_name='Дата последнего ТО')
    motochas_to = models.PositiveIntegerField(null=True, blank=True,  verbose_name='Моточасы последнего ТО')
    interval_to = models.PositiveIntegerField(null=True, blank=True, default=300, verbose_name='Межсервисный интервал')


    # настройка отчета
    narabotka = models.BooleanField(default=True, verbose_name='Наработка')
    nagruzka = models.BooleanField(default=True, verbose_name='Нагрузка')
    active = models.BooleanField(default=True, verbose_name='Активная Нагрузка')
    reactive = models.BooleanField(default=True, verbose_name='Реактивная  Нагрузка')
    full_load = models.BooleanField(default=True, verbose_name='Полная  Нагрузка')
    l1 = models.BooleanField(default=True, verbose_name='L1')
    l2 = models.BooleanField(default=True, verbose_name='L2')
    l3 = models.BooleanField(default=True, verbose_name='L3')
    dmasla = models.BooleanField(default=True, verbose_name='Давление масла')
    tog = models.BooleanField(default=True, verbose_name='Темп. Охл. Жидкости')
    akb = models.BooleanField(default=True, verbose_name='АКБ')
    primechanie = models.BooleanField(default=True, verbose_name='Примечания')
    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'ДГУ'
        verbose_name_plural = 'ДГУ'


class ReportDGU(models.Model):
    dgu = models.ForeignKey(CreateDGU, on_delete=models.SET_NULL, null=True, verbose_name="Номер Дгу")
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True,
                               default=None)

    # Показатели Отчета
    narabotka = models.PositiveIntegerField(null=True, blank=True,  verbose_name='Наработка')
    nagruzka = models.PositiveIntegerField(null=True, blank=True, verbose_name='Нагрузка')
    active = models.PositiveIntegerField(null=True, blank=True,  verbose_name='Активная Нагрузка')
    reactive = models.PositiveIntegerField(null=True, blank=True,  verbose_name='Реактивная  Нагрузка')
    full_load = models.PositiveIntegerField(null=True, blank=True,  verbose_name='Полная  Нагрузка')
    l1 = models.PositiveSmallIntegerField(null=True, blank=True,  verbose_name='L1')
    l2 = models.PositiveSmallIntegerField(null=True, blank=True,  verbose_name='L2')
    l3 = models.PositiveSmallIntegerField(null=True, blank=True,  verbose_name='L3')

    dmasla = models.FloatField(blank=True, null=True, verbose_name='Давление масла')
    tc = models.FloatField(blank=True, null=True,  verbose_name='Темп. Охл. Жидкости')
    akb = models.FloatField(blank=True, null=True, verbose_name='АКБ')
    title = models.CharField(max_length=450, null=True, blank=True,  verbose_name='Замечания')

    time_create = models.DateTimeField(auto_now_add=True, blank=True, null=True,)
    time_update = models.DateTimeField(auto_now=True, blank=True, null=True,)
    def __str__(self):
        return f"{self.dgu}"
    class Meta:
        verbose_name = 'Ежедневный отчет'
        verbose_name_plural = 'Ежедневный отчет'



