# Generated by Django 4.2.14 on 2024-12-29 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0047_alter_mercury_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='createdgu',
            name='total_power',
            field=models.BooleanField(default=True, verbose_name='Общая мощность'),
        ),
        migrations.AddField(
            model_name='reportdgu',
            name='total_power',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='L3'),
        ),
        migrations.AlterField(
            model_name='reportdgu',
            name='narabotka',
            field=models.FloatField(blank=True, null=True, verbose_name='Моточасы'),
        ),
    ]
