# Generated by Django 4.2.14 on 2024-09-09 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='ObjectKES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='reportdgu',
            name='dgu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.createdgu'),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250)),
                ('name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='report.location')),
            ],
        ),
        migrations.AddField(
            model_name='location',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='report.objectkes'),
        ),
    ]
