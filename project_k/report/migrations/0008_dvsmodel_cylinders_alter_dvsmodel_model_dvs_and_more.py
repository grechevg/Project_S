# Generated by Django 4.2.14 on 2024-09-22 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0007_dvsmodel_alter_reportdgu_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvsmodel',
            name='cylinders',
            field=models.IntegerField(blank=True, default=1, verbose_name='Количество цилиндров'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dvsmodel',
            name='model_dvs',
            field=models.CharField(blank=True, max_length=30, verbose_name='Модель ДВС'),
        ),
        migrations.AlterField(
            model_name='dvsmodel',
            name='volume',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=2, verbose_name='Объем ДВС'),
        ),
    ]
