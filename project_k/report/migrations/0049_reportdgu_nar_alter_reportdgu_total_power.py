# Generated by Django 4.2.14 on 2024-12-31 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0048_createdgu_total_power_reportdgu_total_power_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reportdgu',
            name='nar',
            field=models.FloatField(default=0, null=True, verbose_name='Наработка'),
        ),
        migrations.AlterField(
            model_name='reportdgu',
            name='total_power',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Общая Мощность'),
        ),
    ]
