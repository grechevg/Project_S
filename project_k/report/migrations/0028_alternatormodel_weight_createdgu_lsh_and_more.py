# Generated by Django 4.2.14 on 2024-11-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0027_createdgu_maker_dvs'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternatormodel',
            name='weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Вес кг'),
        ),
        migrations.AddField(
            model_name='createdgu',
            name='lsh',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Длинна * Ширина * Высота '),
        ),
        migrations.AddField(
            model_name='createdgu',
            name='weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Вес кг'),
        ),
        migrations.AddField(
            model_name='dvsmodel',
            name='weight',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Вес кг'),
        ),
    ]