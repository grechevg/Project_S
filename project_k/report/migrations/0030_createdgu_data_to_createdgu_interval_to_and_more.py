# Generated by Django 4.2.14 on 2024-12-01 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0029_alter_alternator_model_alternator_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='createdgu',
            name='data_to',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего ТО'),
        ),
        migrations.AddField(
            model_name='createdgu',
            name='interval_to',
            field=models.PositiveIntegerField(blank=True, default=300, null=True, verbose_name='Межсервисный интервал'),
        ),
        migrations.AddField(
            model_name='createdgu',
            name='motochas_to',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Моточасы последнего ТО'),
        ),
    ]
