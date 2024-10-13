# Generated by Django 4.2.14 on 2024-09-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0009_remove_dvsmodel_volume'),
    ]

    operations = [
        migrations.AddField(
            model_name='dvs',
            name='engine_hours',
            field=models.IntegerField(blank=True, default=1, verbose_name='Моточасы'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dvs',
            name='sn',
            field=models.CharField(blank=True, max_length=50, verbose_name='Серейный номер'),
        ),
    ]